"""Local, open-source media understanding: PDF text + screenshot OCR.

* PDFs: ``pypdf`` if installed, otherwise the ``pdftotext`` CLI (poppler).
* Images: ``easyocr`` (Apache-2.0, runs on CPU, no API cost).

Results are cached in ``code/cache/media_text.json`` keyed by file_id + file size
so re-runs are instant and deterministic. Extracted text is treated strictly as
evidence data, never as instructions.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "cache" / "media_text.json"


def _pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
        return "\n".join(p.extract_text() or "" for p in PdfReader(str(path)).pages)
    except ImportError:
        pass
    exe = shutil.which("pdftotext")
    if exe:
        return subprocess.run([exe, "-layout", str(path), "-"], capture_output=True, text=True,
                              encoding="utf8").stdout
    return ""


_reader = None


def _image_text(path: Path) -> str:
    global _reader
    try:
        import easyocr  # type: ignore
    except ImportError:
        return ""
    if _reader is None:
        _reader = easyocr.Reader(["en"], gpu=False, verbose=False)
    # paragraph=False keeps each UI label as its own line, preserving ids like "account_5762"
    # canvas_size caps the detector's working resolution (keeps RAM < 1 GB on CPU laptops)
    lines = _reader.readtext(str(path), detail=0, paragraph=False, canvas_size=1400)
    return "\n".join(lines)


def extract_media_text(dataset_dir: Path, manifest: dict) -> dict[str, str]:
    cache = json.loads(CACHE.read_text(encoding="utf8")) if CACHE.exists() else {}
    for fid, row in sorted(manifest.items()):
        path = Path(dataset_dir) / row["file_path"]
        ext = path.suffix.lower()
        if ext not in (".pdf", ".png", ".jpg", ".jpeg") or not path.exists():
            continue
        key = f"{fid}:{path.stat().st_size}"
        if cache.get(key) is None:
            cache[key] = _pdf_text(path) if ext == ".pdf" else _image_text(path)
            CACHE.parent.mkdir(parents=True, exist_ok=True)   # save incrementally
            CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf8")
    out = {}
    for k, v in cache.items():
        out[k.split(":")[0]] = v
    return out
