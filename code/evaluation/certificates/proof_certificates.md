# GhostTrace deletion certificates

Each case lists the completion conditions checked by the deterministic verifier. `PASS` = evidence proves the required state at `audit_at`; `FAIL` = evidence proves a violation (drives a finding); `UNKNOWN` = no admissible evidence (blocks a COMPLETE claim).

## case_33 - INCOMPLETE
- subject: `user_18`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `export_service/export_1842` [USER_EXPORT] state=`PRESENT` evidence=`evidence_18` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: export_1842:rule_09 (evidence_18)
  - UNKNOWN: account_identified (no evidence)

## case_34 - INCOMPLETE
- subject: `user_11`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5762` [USER_PROFILE] state=`PRESENT` evidence=`evidence_04` link=`identity`
  - `support_platform/support_9538` [SUPPORT_ATTACHMENT] state=`CLEAN` evidence=`evidence_04` link=`identity`
  - FAIL: account_5762:rule_01 (evidence_04)
  - FAIL: support_9538:rule_06 (evidence_04)

## case_35 - INCOMPLETE
- subject: `user_13`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `search_service/search_428` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_09` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: search_428:rule_03 (evidence_09)
  - UNKNOWN: account_identified (no evidence)

## case_36 - INCOMPLETE
- subject: `user_34`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5823` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `security_service/audit_record_2966` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `export_service/export_7689` [USER_EXPORT] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `search_service/search_5575` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - PASS: account_5823:rule_01 (evidence_03)
  - PASS: audit_record_2966:rule_12 (evidence_03)
  - FAIL: export_7689:rule_09 (evidence_03)
  - FAIL: search_5575:rule_03 (evidence_03)

## case_37 - INCOMPLETE
- subject: `user_35`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5193` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `security_service/audit_record_2019` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `integration_service/data_flow_2528` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_03` link=`identity`
  - `search_service/search_1934` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - PASS: account_5193:rule_01 (evidence_03)
  - PASS: audit_record_2019:rule_12 (evidence_03)
  - FAIL: data_flow_2528:no-rule:recreation-path (evidence_03)
  - FAIL: search_1934:rule_03 (evidence_03)

## case_38 - INCOMPLETE
- subject: `user_36`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2381` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `security_service/audit_record_633` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `integration_service/data_flow_7495` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_03` link=`identity`
  - PASS: account_2381:rule_01 (evidence_03)
  - PASS: audit_record_633:rule_12 (evidence_03)
  - FAIL: data_flow_7495:no-rule:recreation-path (evidence_03)

## case_39 - INCOMPLETE
- subject: `user_14`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `integration_service/data_flow_1121` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_14` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: data_flow_1121:no-rule:recreation-path (evidence_14)
  - UNKNOWN: account_identified (no evidence)

## case_40 - INCOMPLETE
- subject: `user_38`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1810` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `security_service/audit_record_8349` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `search_service/search_3200` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `support_platform/support_4887` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_03` link=`identity`
  - PASS: account_1810:rule_01 (evidence_03)
  - PASS: audit_record_8349:rule_12 (evidence_03)
  - FAIL: search_3200:rule_03 (evidence_03)
  - FAIL: support_4887:rule_05 (evidence_03)

## case_41 - COMPLETE
- subject: `user_39`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4051` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `analytics_platform/analytics_6830` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_03` link=`run-fingerprint`
  - `security_service/audit_record_7814` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `backup_service/backup_706` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_03` link=`identity`
  - `integration_service/data_flow_2901` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_03` link=`identity`
  - `support_platform/support_2667` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_03` link=`identity`
  - PASS: account_4051:rule_01 (evidence_03)
  - PASS: analytics_6830:rule_07 (evidence_03)
  - PASS: audit_record_7814:rule_12 (evidence_03)
  - PASS: backup_706:rule_14 (evidence_03)
  - PASS: data_flow_2901:no-rule:recreation-path (evidence_03)
  - PASS: support_2667:rule_05 (evidence_03)

## case_42 - INCOMPLETE
- subject: `user_40`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4337` [USER_PROFILE] state=`ABSENT` evidence=`evidence_03` link=`identity`
  - `security_service/audit_record_6760` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `search_service/search_7078` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_03` link=`identity`
  - `support_platform/support_7769` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_03` link=`identity`
  - PASS: account_4337:rule_01 (evidence_03)
  - PASS: audit_record_6760:rule_12 (evidence_03)
  - FAIL: search_7078:rule_03 (evidence_03)
  - FAIL: support_7769:rule_05 (evidence_03)

## case_43 - INCOMPLETE
- subject: `user_41`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8681` [USER_PROFILE] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - FAIL: account_8681:rule_01 (evidence_94)

## case_44 - COMPLETE
- subject: `user_42`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2064` [USER_PROFILE] state=`ABSENT` evidence=`evidence_94` link=`identity`
  - `analytics_platform/analytics_5589` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_94` link=`run-fingerprint`
  - `security_service/audit_record_1105` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - `backup_service/backup_6266` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_94` link=`identity`
  - `integration_service/data_flow_223` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_94` link=`identity`
  - `support_platform/support_1066` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_94` link=`identity`
  - PASS: account_2064:rule_01 (evidence_94)
  - PASS: analytics_5589:rule_07 (evidence_94)
  - PASS: audit_record_1105:rule_12 (evidence_94)
  - PASS: backup_6266:rule_14 (evidence_94)
  - PASS: data_flow_223:no-rule:recreation-path (evidence_94)
  - PASS: support_1066:rule_05 (evidence_94)

## case_45 - COMPLETE
- subject: `user_03`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `security_service/audit_record_003` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_37` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - PASS: audit_record_003:rule_12 (evidence_37)
  - UNKNOWN: account_identified (no evidence)

## case_46 - COMPLETE
- subject: `user_17`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6523` [USER_PROFILE] state=`ABSENT` evidence=`evidence_67` link=`identity`
  - `identity_service/tombstone_17` [ACCOUNT_TOMBSTONE] state=`CLEAN` evidence=`evidence_42` link=`identity`
  - PASS: account_6523:rule_01 (evidence_67)
  - PASS: tombstone_17:rule_15 (evidence_42)

## case_47 - INCOMPLETE
- subject: `user_45`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_617` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-fingerprint`
  - `search_service/search_4324` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - `support_platform/support_5742` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_94` link=`identity`
  - PASS: account_617:rule_01 (evidence_05)
  - FAIL: search_4324:rule_03 (evidence_94)
  - FAIL: support_5742:rule_05 (evidence_94)

## case_48 - INCOMPLETE
- subject: `user_46`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_483` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-fingerprint`
  - `integration_service/data_flow_7759` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_94` link=`identity`
  - `search_service/search_2127` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - PASS: account_483:rule_01 (evidence_05)
  - FAIL: data_flow_7759:no-rule:recreation-path (evidence_94)
  - FAIL: search_2127:rule_03 (evidence_94)

## case_49 - INCOMPLETE
- subject: `user_47`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_034` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-elimination`
  - `integration_service/data_flow_1043` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_94` link=`identity`
  - `search_service/search_459` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - PASS: account_034:rule_01 (evidence_05)
  - FAIL: data_flow_1043:no-rule:recreation-path (evidence_94)
  - FAIL: search_459:rule_03 (evidence_94)

## case_50 - INCOMPLETE
- subject: `user_20`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `analytics_platform/analytics_7438` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_19` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: analytics_7438:rule_07 (evidence_19)
  - UNKNOWN: account_identified (no evidence)

## case_51 - COMPLETE
- subject: `user_49`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3610` [USER_PROFILE] state=`ABSENT` evidence=`evidence_94` link=`identity`
  - `analytics_platform/analytics_2265` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_94` link=`run-fingerprint`
  - `security_service/audit_record_3308` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_94` link=`identity`
  - `backup_service/backup_7809` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_94` link=`identity`
  - `integration_service/data_flow_4713` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_94` link=`identity`
  - `support_platform/support_1097` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_94` link=`identity`
  - PASS: account_3610:rule_01 (evidence_94)
  - PASS: analytics_2265:rule_07 (evidence_94)
  - PASS: audit_record_3308:rule_12 (evidence_94)
  - PASS: backup_7809:rule_14 (evidence_94)
  - PASS: data_flow_4713:no-rule:recreation-path (evidence_94)
  - PASS: support_1097:rule_05 (evidence_94)

## case_52 - INCOMPLETE
- subject: `user_18`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `export_service/export_1260` [USER_EXPORT] state=`PRESENT` evidence=`evidence_23` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: export_1260:rule_09 (evidence_23)
  - UNKNOWN: account_identified (no evidence)

## case_53 - INCOMPLETE
- subject: `user_22`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `support_platform/support_1034` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_28` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: support_1034:rule_05 (evidence_28)
  - UNKNOWN: account_identified (no evidence)

## case_54 - INCOMPLETE
- subject: `user_52`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_6829` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-elimination`
  - `analytics_platform/analytics_1738` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_05` link=`identity`
  - `security_service/audit_record_6325` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `integration_service/data_flow_5080` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_05` link=`identity`
  - `search_service/search_3995` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `support_platform/support_835` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_05` link=`identity`
  - PASS: account_6829:rule_01 (evidence_05)
  - FAIL: analytics_1738:rule_07 (evidence_05)
  - PASS: audit_record_6325:rule_12 (evidence_05)
  - FAIL: data_flow_5080:no-rule:recreation-path (evidence_05)
  - FAIL: search_3995:rule_03 (evidence_05)
  - FAIL: support_835:rule_05 (evidence_05)

## case_55 - INCOMPLETE
- subject: `user_16`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `backup_service/backup_9287` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_32` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: backup_9287:rule_14 (evidence_32)
  - UNKNOWN: account_identified (no evidence)

## case_56 - INCOMPLETE
- subject: `user_54`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5715` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-fingerprint`
  - `analytics_platform/analytics_2572` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_05` link=`run-fingerprint`
  - `security_service/audit_record_4078` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `integration_service/data_flow_373` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_05` link=`identity`
  - PASS: account_5715:rule_01 (evidence_05)
  - PASS: analytics_2572:rule_07 (evidence_05)
  - PASS: audit_record_4078:rule_12 (evidence_05)
  - FAIL: data_flow_373:no-rule:recreation-path (evidence_05)

## case_57 - COMPLETE
- subject: `user_55`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1298` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-elimination`
  - `analytics_platform/analytics_8858` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_05` link=`run-fingerprint`
  - `security_service/audit_record_7219` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `backup_service/backup_7711` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_05` link=`identity`
  - `integration_service/data_flow_1368` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_05` link=`identity`
  - `support_platform/support_7479` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_05` link=`identity`
  - PASS: account_1298:rule_01 (evidence_05)
  - PASS: analytics_8858:rule_07 (evidence_05)
  - PASS: audit_record_7219:rule_12 (evidence_05)
  - PASS: backup_7711:rule_14 (evidence_05)
  - PASS: data_flow_1368:no-rule:recreation-path (evidence_05)
  - PASS: support_7479:rule_05 (evidence_05)

## case_58 - COMPLETE
- subject: `user_56`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_9862` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-elimination`
  - `security_service/audit_record_8465` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - PASS: account_9862:rule_01 (evidence_05)
  - PASS: audit_record_8465:rule_12 (evidence_05)

## case_59 - COMPLETE
- subject: `user_57`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_5661` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-ambiguous`
  - `security_service/audit_record_962` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - PASS: account_5661:rule_01 (evidence_05)
  - PASS: audit_record_962:rule_12 (evidence_05)

## case_60 - COMPLETE
- subject: `user_58`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_631` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-ambiguous`
  - `analytics_platform/analytics_9069` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_05` link=`run-fingerprint`
  - `security_service/audit_record_629` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - PASS: account_631:rule_01 (evidence_05)
  - PASS: analytics_9069:rule_07 (evidence_05)
  - PASS: audit_record_629:rule_12 (evidence_05)

## case_61 - INCOMPLETE
- subject: `user_07`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `object_storage/object_19` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_46` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: object_19:rule_06 (evidence_46)
  - UNKNOWN: account_identified (no evidence)

## case_62 - INCOMPLETE
- subject: `user_60`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7119` [USER_PROFILE] state=`ABSENT` evidence=`evidence_05` link=`run-elimination`
  - `analytics_platform/analytics_5715` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_05` link=`identity`
  - `security_service/audit_record_4889` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `integration_service/data_flow_108` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_05` link=`identity`
  - `search_service/search_5960` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_05` link=`identity`
  - `support_platform/support_8765` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_05` link=`identity`
  - PASS: account_7119:rule_01 (evidence_05)
  - FAIL: analytics_5715:rule_07 (evidence_05)
  - PASS: audit_record_4889:rule_12 (evidence_05)
  - FAIL: data_flow_108:no-rule:recreation-path (evidence_05)
  - FAIL: search_5960:rule_03 (evidence_05)
  - FAIL: support_8765:rule_05 (evidence_05)

## case_63 - INCOMPLETE
- subject: `user_09`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `marketing_platform/marketing_001` [MARKETING_PROFILE] state=`PRESENT` evidence=`evidence_60` link=`identity`
  - `account_service/?` [USER_PROFILE] state=`None` evidence=`-` link=`missing`
  - FAIL: marketing_001:rule_10 (evidence_60)
  - UNKNOWN: account_identified (no evidence)

## case_64 - COMPLETE
- subject: `user_62`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_565` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `analytics_platform/analytics_5718` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_93` link=`run-fingerprint`
  - `security_service/audit_record_1892` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - `backup_service/backup_3933` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_93` link=`identity`
  - `integration_service/data_flow_6846` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_93` link=`identity`
  - `support_platform/support_6334` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_93` link=`identity`
  - PASS: account_565:rule_01 (evidence_93)
  - PASS: analytics_5718:rule_07 (evidence_93)
  - PASS: audit_record_1892:rule_12 (evidence_93)
  - PASS: backup_3933:rule_14 (evidence_93)
  - PASS: data_flow_6846:no-rule:recreation-path (evidence_93)
  - PASS: support_6334:rule_05 (evidence_93)

## case_65 - INCOMPLETE
- subject: `user_63`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5488` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `analytics_platform/analytics_9246` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_1848` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_689` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - PASS: account_5488:rule_01 (evidence_93)
  - FAIL: analytics_9246:rule_07 (evidence_93)
  - UNKNOWN: audit_record_1848:observed (no evidence)
  - FAIL: search_689:rule_03 (evidence_93)

## case_66 - INCOMPLETE
- subject: `user_64`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_1602` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_184` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_4249` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_93` link=`identity`
  - PASS: account_1602:rule_01 (evidence_93)
  - UNKNOWN: audit_record_184:observed (no evidence)
  - FAIL: support_4249:rule_05 (evidence_93)

## case_67 - INCOMPLETE
- subject: `user_65`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9079` [USER_PROFILE] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_2877` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - FAIL: account_9079:rule_01 (evidence_93)
  - UNKNOWN: audit_record_2877:observed (no evidence)

## case_68 - INCOMPLETE
- subject: `user_66`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_902` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_4049` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_2406` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_93` link=`identity`
  - `search_service/search_2568` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - PASS: account_902:rule_01 (evidence_93)
  - UNKNOWN: audit_record_4049:observed (no evidence)
  - FAIL: data_flow_2406:no-rule:recreation-path (evidence_93)
  - FAIL: search_2568:rule_03 (evidence_93)

## case_69 - COMPLETE
- subject: `user_67`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_6138` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_9011` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - PASS: account_6138:rule_01 (evidence_93)
  - PASS: audit_record_9011:rule_12 (evidence_93)

## case_70 - COMPLETE
- subject: `user_68`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6633` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_1738` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - PASS: account_6633:rule_01 (evidence_93)
  - PASS: audit_record_1738:rule_12 (evidence_93)

## case_71 - INCOMPLETE
- subject: `user_69`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1378` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_1096` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_684` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - `support_platform/support_1370` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_93` link=`identity`
  - PASS: account_1378:rule_01 (evidence_93)
  - UNKNOWN: audit_record_1096:observed (no evidence)
  - FAIL: search_684:rule_03 (evidence_93)
  - FAIL: support_1370:rule_05 (evidence_93)

## case_72 - INCOMPLETE
- subject: `user_70`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7643` [USER_PROFILE] state=`ABSENT` evidence=`evidence_93` link=`identity`
  - `security_service/audit_record_1310` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_4091` [USER_EXPORT] state=`PRESENT` evidence=`evidence_93` link=`identity`
  - PASS: account_7643:rule_01 (evidence_93)
  - UNKNOWN: audit_record_1310:observed (no evidence)
  - FAIL: export_4091:rule_09 (evidence_93)

## case_73 - COMPLETE
- subject: `user_71`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6070` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `analytics_platform/analytics_1161` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_91` link=`run-fingerprint`
  - `security_service/audit_record_5710` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - PASS: account_6070:rule_01 (evidence_91)
  - PASS: analytics_1161:rule_07 (evidence_91)
  - PASS: audit_record_5710:rule_12 (evidence_91)

## case_74 - INCOMPLETE
- subject: `user_72`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9051` [USER_PROFILE] state=`ABSENT` evidence=`evidence_90` link=`run-fingerprint`
  - `security_service/audit_record_7778` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4595` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_91` link=`identity`
  - PASS: account_9051:rule_01 (evidence_90)
  - UNKNOWN: audit_record_7778:observed (no evidence)
  - FAIL: data_flow_4595:no-rule:recreation-path (evidence_91)

## case_75 - INCOMPLETE
- subject: `user_73`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1495` [USER_PROFILE] state=`ABSENT` evidence=`evidence_90` link=`run-fingerprint`
  - `security_service/audit_record_7491` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_8673` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_91` link=`identity`
  - PASS: account_1495:rule_01 (evidence_90)
  - UNKNOWN: audit_record_7491:observed (no evidence)
  - FAIL: backup_8673:rule_14 (evidence_91)

## case_76 - INCOMPLETE
- subject: `user_74`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_925` [USER_PROFILE] state=`ABSENT` evidence=`evidence_90` link=`run-elimination`
  - `security_service/audit_record_6766` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_9746` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_91` link=`identity`
  - PASS: account_925:rule_01 (evidence_90)
  - UNKNOWN: audit_record_6766:observed (no evidence)
  - FAIL: support_9746:rule_05 (evidence_91)

## case_77 - COMPLETE
- subject: `user_75`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9334` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `analytics_platform/analytics_5859` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_91` link=`run-fingerprint`
  - `security_service/audit_record_5425` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - `backup_service/backup_7303` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `integration_service/data_flow_7773` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `support_platform/support_008` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_91` link=`identity`
  - PASS: account_9334:rule_01 (evidence_91)
  - PASS: analytics_5859:rule_07 (evidence_91)
  - PASS: audit_record_5425:rule_12 (evidence_91)
  - PASS: backup_7303:rule_14 (evidence_91)
  - PASS: data_flow_7773:no-rule:recreation-path (evidence_91)
  - PASS: support_008:rule_05 (evidence_91)

## case_78 - INCOMPLETE
- subject: `user_76`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_8754` [USER_PROFILE] state=`ABSENT` evidence=`evidence_90` link=`run-elimination`
  - `security_service/audit_record_6593` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8295` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - `support_platform/support_9652` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_91` link=`identity`
  - PASS: account_8754:rule_01 (evidence_90)
  - UNKNOWN: audit_record_6593:observed (no evidence)
  - FAIL: search_8295:rule_03 (evidence_91)
  - FAIL: support_9652:rule_05 (evidence_91)

## case_79 - COMPLETE
- subject: `user_77`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5186` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `security_service/audit_record_1734` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - PASS: account_5186:rule_01 (evidence_91)
  - PASS: audit_record_1734:rule_12 (evidence_91)

## case_80 - COMPLETE
- subject: `user_78`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4006` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `security_service/audit_record_5681` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - PASS: account_4006:rule_01 (evidence_91)
  - PASS: audit_record_5681:rule_12 (evidence_91)

## case_81 - COMPLETE
- subject: `user_79`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9832` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `analytics_platform/analytics_5059` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_91` link=`run-fingerprint`
  - `security_service/audit_record_9645` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - `backup_service/backup_3332` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `integration_service/data_flow_3255` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `support_platform/support_5953` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_91` link=`identity`
  - PASS: account_9832:rule_01 (evidence_91)
  - PASS: analytics_5059:rule_07 (evidence_91)
  - PASS: audit_record_9645:rule_12 (evidence_91)
  - PASS: backup_3332:rule_14 (evidence_91)
  - PASS: data_flow_3255:no-rule:recreation-path (evidence_91)
  - PASS: support_5953:rule_05 (evidence_91)

## case_82 - COMPLETE
- subject: `user_80`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4156` [USER_PROFILE] state=`ABSENT` evidence=`evidence_91` link=`identity`
  - `analytics_platform/analytics_2176` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_91` link=`run-fingerprint`
  - `security_service/audit_record_3747` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_91` link=`identity`
  - `backup_service/backup_317` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `integration_service/data_flow_9666` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_91` link=`identity`
  - `support_platform/support_9166` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_91` link=`identity`
  - PASS: account_4156:rule_01 (evidence_91)
  - PASS: analytics_2176:rule_07 (evidence_91)
  - PASS: audit_record_3747:rule_12 (evidence_91)
  - PASS: backup_317:rule_14 (evidence_91)
  - PASS: data_flow_9666:no-rule:recreation-path (evidence_91)
  - PASS: support_9166:rule_05 (evidence_91)

## case_83 - COMPLETE
- subject: `user_81`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2449` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_2636` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - PASS: account_2449:rule_01 (evidence_08)
  - PASS: audit_record_2636:rule_12 (evidence_08)

## case_84 - COMPLETE
- subject: `user_82`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_2387` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_3787` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - PASS: account_2387:rule_01 (evidence_08)
  - PASS: audit_record_3787:rule_12 (evidence_08)

## case_85 - INCOMPLETE
- subject: `user_83`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4911` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_8094` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `integration_service/data_flow_9927` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_08` link=`identity`
  - `search_service/search_6302` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - PASS: account_4911:rule_01 (evidence_08)
  - PASS: audit_record_8094:rule_12 (evidence_08)
  - FAIL: data_flow_9927:no-rule:recreation-path (evidence_08)
  - FAIL: search_6302:rule_03 (evidence_08)

## case_86 - COMPLETE
- subject: `user_84`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8473` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `analytics_platform/analytics_9500` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_08` link=`run-fingerprint`
  - `security_service/audit_record_5580` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - PASS: account_8473:rule_01 (evidence_08)
  - PASS: analytics_9500:rule_07 (evidence_08)
  - PASS: audit_record_5580:rule_12 (evidence_08)

## case_87 - INCOMPLETE
- subject: `user_85`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8166` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_4474` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `backup_service/backup_4689` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_08` link=`identity`
  - PASS: account_8166:rule_01 (evidence_08)
  - PASS: audit_record_4474:rule_12 (evidence_08)
  - FAIL: backup_4689:rule_14 (evidence_08)

## case_88 - INCOMPLETE
- subject: `user_86`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_868` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_3825` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `support_platform/support_2967` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - PASS: account_868:rule_01 (evidence_08)
  - PASS: audit_record_3825:rule_12 (evidence_08)
  - FAIL: support_2967:rule_05 (evidence_08)

## case_89 - INCOMPLETE
- subject: `user_87`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8764` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `analytics_platform/analytics_6499` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_2539` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `search_service/search_1839` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - PASS: account_8764:rule_01 (evidence_08)
  - FAIL: analytics_6499:rule_07 (evidence_08)
  - PASS: audit_record_2539:rule_12 (evidence_08)
  - FAIL: search_1839:rule_03 (evidence_08)

## case_90 - INCOMPLETE
- subject: `user_88`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9673` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `analytics_platform/analytics_3181` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_9355` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `integration_service/data_flow_2085` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_08` link=`identity`
  - `search_service/search_5561` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `support_platform/support_7460` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - PASS: account_9673:rule_01 (evidence_08)
  - FAIL: analytics_3181:rule_07 (evidence_08)
  - PASS: audit_record_9355:rule_12 (evidence_08)
  - FAIL: data_flow_2085:no-rule:recreation-path (evidence_08)
  - FAIL: search_5561:rule_03 (evidence_08)
  - FAIL: support_7460:rule_05 (evidence_08)

## case_91 - INCOMPLETE
- subject: `user_89`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6075` [USER_PROFILE] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `analytics_platform/analytics_8539` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_8304` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `search_service/search_9156` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `support_platform/support_266` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_08` link=`identity`
  - FAIL: account_6075:rule_01 (evidence_08)
  - FAIL: analytics_8539:rule_07 (evidence_08)
  - PASS: audit_record_8304:rule_12 (evidence_08)
  - FAIL: search_9156:rule_03 (evidence_08)
  - FAIL: support_266:rule_05 (evidence_08)

## case_92 - INCOMPLETE
- subject: `user_90`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3609` [USER_PROFILE] state=`ABSENT` evidence=`evidence_08` link=`identity`
  - `security_service/audit_record_5625` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_08` link=`identity`
  - `integration_service/data_flow_7535` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_08` link=`identity`
  - PASS: account_3609:rule_01 (evidence_08)
  - PASS: audit_record_5625:rule_12 (evidence_08)
  - FAIL: data_flow_7535:no-rule:recreation-path (evidence_08)

## case_93 - INCOMPLETE
- subject: `user_91`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4421` [USER_PROFILE] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `integration_service/data_flow_047` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_89` link=`identity`
  - `search_service/search_1310` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `support_platform/support_1824` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - FAIL: account_4421:rule_01 (evidence_89)
  - FAIL: data_flow_047:no-rule:recreation-path (evidence_89)
  - FAIL: search_1310:rule_03 (evidence_89)
  - FAIL: support_1824:rule_05 (evidence_89)

## case_94 - INCOMPLETE
- subject: `user_92`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4037` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `search_service/search_7631` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `support_platform/support_7691` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - PASS: account_4037:rule_01 (evidence_10)
  - FAIL: search_7631:rule_03 (evidence_89)
  - FAIL: support_7691:rule_05 (evidence_89)

## case_95 - INCOMPLETE
- subject: `user_93`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4176` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `analytics_platform/analytics_1316` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - `search_service/search_7807` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `support_platform/support_5750` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - `support_platform/support_7311` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - PASS: account_4176:rule_01 (evidence_10)
  - FAIL: analytics_1316:rule_07 (evidence_89)
  - FAIL: search_7807:rule_03 (evidence_89)
  - FAIL: support_5750:rule_05 (evidence_89)
  - FAIL: support_7311:rule_05 (evidence_89)

## case_96 - INCOMPLETE
- subject: `user_94`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5815` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `export_service/export_8827` [USER_EXPORT] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `search_service/search_5672` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - PASS: account_5815:rule_01 (evidence_10)
  - FAIL: export_8827:rule_09 (evidence_89)
  - FAIL: search_5672:rule_03 (evidence_89)

## case_97 - COMPLETE
- subject: `user_95`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_6813` [USER_PROFILE] state=`ABSENT` evidence=`evidence_89` link=`run-elimination`
  - `analytics_platform/analytics_9103` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_89` link=`run-fingerprint`
  - `security_service/audit_record_8778` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - PASS: account_6813:rule_01 (evidence_89)
  - PASS: analytics_9103:rule_07 (evidence_89)
  - PASS: audit_record_8778:rule_12 (evidence_89)

## case_98 - INCOMPLETE
- subject: `user_96`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9511` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `integration_service/data_flow_3165` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_89` link=`identity`
  - PASS: account_9511:rule_01 (evidence_10)
  - FAIL: data_flow_3165:no-rule:recreation-path (evidence_89)

## case_99 - INCOMPLETE
- subject: `user_97`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1034` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `backup_service/backup_7804` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_89` link=`identity`
  - PASS: account_1034:rule_01 (evidence_10)
  - FAIL: backup_7804:rule_14 (evidence_89)

## case_100 - INCOMPLETE
- subject: `user_98`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7927` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `legal_service/legal_hold_668` [LEGAL_HOLD_RECORD] state=`None` evidence=`-` link=`run-ambiguous`
  - `search_service/search_018` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `support_platform/support_1630` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - PASS: account_7927:rule_01 (evidence_10)
  - UNKNOWN: legal_hold_668:observed (no evidence)
  - FAIL: search_018:rule_03 (evidence_89)
  - FAIL: support_1630:rule_05 (evidence_89)

## case_101 - INCOMPLETE
- subject: `user_99`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7169` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `analytics_platform/analytics_6105` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - `search_service/search_8561` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - PASS: account_7169:rule_01 (evidence_10)
  - FAIL: analytics_6105:rule_07 (evidence_89)
  - FAIL: search_8561:rule_03 (evidence_89)

## case_102 - INCOMPLETE
- subject: `user_100`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2056` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `search_service/search_4586` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_89` link=`identity`
  - `support_platform/support_345` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_89` link=`identity`
  - PASS: account_2056:rule_01 (evidence_10)
  - FAIL: search_4586:rule_03 (evidence_89)
  - FAIL: support_345:rule_05 (evidence_89)

## case_103 - COMPLETE
- subject: `user_101`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4070` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `analytics_platform/analytics_3264` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_9522` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_4070:rule_01 (evidence_10)
  - PASS: analytics_3264:rule_07 (evidence_10)
  - PASS: audit_record_9522:rule_12 (evidence_10)

## case_104 - INCOMPLETE
- subject: `user_102`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4514` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `analytics_platform/analytics_4882` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_10` link=`identity`
  - `security_service/audit_record_6230` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `integration_service/data_flow_5127` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_10` link=`identity`
  - `search_service/search_8379` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `support_platform/support_4267` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_10` link=`identity`
  - PASS: account_4514:rule_01 (evidence_10)
  - FAIL: analytics_4882:rule_07 (evidence_10)
  - PASS: audit_record_6230:rule_12 (evidence_10)
  - FAIL: data_flow_5127:no-rule:recreation-path (evidence_10)
  - FAIL: search_8379:rule_03 (evidence_10)
  - FAIL: support_4267:rule_05 (evidence_10)

## case_105 - INCOMPLETE
- subject: `user_103`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_6345` [USER_PROFILE] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `security_service/audit_record_4520` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `search_service/search_4618` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - FAIL: account_6345:rule_01 (evidence_10)
  - PASS: audit_record_4520:rule_12 (evidence_10)
  - FAIL: search_4618:rule_03 (evidence_10)

## case_106 - INCOMPLETE
- subject: `user_104`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8804` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `security_service/audit_record_8723` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `search_service/search_7223` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_8804:rule_01 (evidence_10)
  - PASS: audit_record_8723:rule_12 (evidence_10)
  - FAIL: search_7223:rule_03 (evidence_10)

## case_107 - COMPLETE
- subject: `user_105`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7510` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `analytics_platform/analytics_2777` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_7572` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_7510:rule_01 (evidence_10)
  - PASS: analytics_2777:rule_07 (evidence_10)
  - PASS: audit_record_7572:rule_12 (evidence_10)

## case_108 - COMPLETE
- subject: `user_106`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_6750` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `analytics_platform/analytics_5001` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_1469` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_6750:rule_01 (evidence_10)
  - PASS: analytics_5001:rule_07 (evidence_10)
  - PASS: audit_record_1469:rule_12 (evidence_10)

## case_109 - INCOMPLETE
- subject: `user_107`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_687` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_2718` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `integration_service/data_flow_9949` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_10` link=`identity`
  - `search_service/search_2016` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_687:rule_01 (evidence_10)
  - PASS: audit_record_2718:rule_12 (evidence_10)
  - FAIL: data_flow_9949:no-rule:recreation-path (evidence_10)
  - FAIL: search_2016:rule_03 (evidence_10)

## case_110 - INCOMPLETE
- subject: `user_108`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2259` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `analytics_platform/analytics_9875` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_10` link=`run-ambiguous`
  - `security_service/audit_record_9268` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `integration_service/data_flow_8857` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_10` link=`identity`
  - `search_service/search_3993` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_2259:rule_01 (evidence_10)
  - PASS: analytics_9875:rule_07 (evidence_10)
  - PASS: audit_record_9268:rule_12 (evidence_10)
  - FAIL: data_flow_8857:no-rule:recreation-path (evidence_10)
  - FAIL: search_3993:rule_03 (evidence_10)

## case_111 - COMPLETE
- subject: `user_109`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9314` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-elimination`
  - `analytics_platform/analytics_800` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_8933` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - PASS: account_9314:rule_01 (evidence_10)
  - PASS: analytics_800:rule_07 (evidence_10)
  - PASS: audit_record_8933:rule_12 (evidence_10)

## case_112 - COMPLETE
- subject: `user_110`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7578` [USER_PROFILE] state=`ABSENT` evidence=`evidence_10` link=`run-fingerprint`
  - `security_service/audit_record_4082` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_10` link=`identity`
  - `backup_service/backup_4863` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_10` link=`identity`
  - `integration_service/data_flow_3444` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_10` link=`identity`
  - `support_platform/support_2859` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_10` link=`identity`
  - PASS: account_7578:rule_01 (evidence_10)
  - PASS: audit_record_4082:rule_12 (evidence_10)
  - PASS: backup_4863:rule_14 (evidence_10)
  - PASS: data_flow_3444:no-rule:recreation-path (evidence_10)
  - PASS: support_2859:rule_05 (evidence_10)

## case_113 - COMPLETE
- subject: `user_111`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6697` [USER_PROFILE] state=`ABSENT` evidence=`evidence_88` link=`identity`
  - `analytics_platform/analytics_4800` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_88` link=`run-fingerprint`
  - `security_service/audit_record_1127` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_6697:rule_01 (evidence_88)
  - PASS: analytics_4800:rule_07 (evidence_88)
  - PASS: audit_record_1127:rule_12 (evidence_88)

## case_114 - INCOMPLETE
- subject: `user_112`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4833` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_6504` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5696` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - `support_platform/support_3786` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_88` link=`identity`
  - PASS: account_4833:rule_01 (evidence_12)
  - UNKNOWN: audit_record_6504:observed (no evidence)
  - FAIL: search_5696:rule_03 (evidence_88)
  - FAIL: support_3786:rule_05 (evidence_88)

## case_115 - INCOMPLETE
- subject: `user_113`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1785` [USER_PROFILE] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - `security_service/audit_record_670` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_4417` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - FAIL: account_1785:rule_01 (evidence_88)
  - UNKNOWN: audit_record_670:observed (no evidence)
  - FAIL: search_4417:rule_03 (evidence_88)

## case_116 - INCOMPLETE
- subject: `user_114`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1823` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_6007` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_6699` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_88` link=`identity`
  - `search_service/search_696` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_1823:rule_01 (evidence_12)
  - UNKNOWN: audit_record_6007:observed (no evidence)
  - FAIL: data_flow_6699:no-rule:recreation-path (evidence_88)
  - FAIL: search_696:rule_03 (evidence_88)

## case_117 - COMPLETE
- subject: `user_115`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_1220` [USER_PROFILE] state=`ABSENT` evidence=`evidence_88` link=`identity`
  - `analytics_platform/analytics_8698` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_88` link=`run-fingerprint`
  - `security_service/audit_record_1598` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_1220:rule_01 (evidence_88)
  - PASS: analytics_8698:rule_07 (evidence_88)
  - PASS: audit_record_1598:rule_12 (evidence_88)

## case_118 - INCOMPLETE
- subject: `user_116`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5785` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_2848` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9556` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - `support_platform/support_036` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_88` link=`identity`
  - PASS: account_5785:rule_01 (evidence_12)
  - UNKNOWN: audit_record_2848:observed (no evidence)
  - FAIL: search_9556:rule_03 (evidence_88)
  - FAIL: support_036:rule_05 (evidence_88)

## case_119 - INCOMPLETE
- subject: `user_117`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8058` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_9445` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5259` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - `support_platform/support_9309` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_88` link=`identity`
  - PASS: account_8058:rule_01 (evidence_12)
  - UNKNOWN: audit_record_9445:observed (no evidence)
  - FAIL: search_5259:rule_03 (evidence_88)
  - FAIL: support_9309:rule_05 (evidence_88)

## case_120 - INCOMPLETE
- subject: `user_118`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8656` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_5496` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_4289` [USER_EXPORT] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - `search_service/search_943` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_8656:rule_01 (evidence_12)
  - UNKNOWN: audit_record_5496:observed (no evidence)
  - FAIL: export_4289:rule_09 (evidence_88)
  - FAIL: search_943:rule_03 (evidence_88)

## case_121 - COMPLETE
- subject: `user_119`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_081` [USER_PROFILE] state=`ABSENT` evidence=`evidence_88` link=`identity`
  - `security_service/audit_record_2103` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_081:rule_01 (evidence_88)
  - PASS: audit_record_2103:rule_12 (evidence_88)

## case_122 - INCOMPLETE
- subject: `user_120`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_9580` [USER_PROFILE] state=`ABSENT` evidence=`evidence_12` link=`identity`
  - `security_service/audit_record_9833` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_3199` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_88` link=`identity`
  - `search_service/search_1752` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_88` link=`identity`
  - PASS: account_9580:rule_01 (evidence_12)
  - UNKNOWN: audit_record_9833:observed (no evidence)
  - FAIL: data_flow_3199:no-rule:recreation-path (evidence_88)
  - FAIL: search_1752:rule_03 (evidence_88)

## case_123 - INCOMPLETE
- subject: `user_121`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_2988` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `security_service/audit_record_5645` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_8742` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_87` link=`identity`
  - PASS: account_2988:rule_01 (evidence_87)
  - UNKNOWN: audit_record_5645:observed (no evidence)
  - FAIL: backup_8742:rule_14 (evidence_87)

## case_124 - INCOMPLETE
- subject: `user_122`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8951` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `security_service/audit_record_282` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_9126` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - PASS: account_8951:rule_01 (evidence_87)
  - UNKNOWN: audit_record_282:observed (no evidence)
  - FAIL: support_9126:rule_05 (evidence_87)

## case_125 - INCOMPLETE
- subject: `user_123`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_7637` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `analytics_platform/analytics_1103` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - `analytics_platform/analytics_7150` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_87` link=`run-ambiguous`
  - `security_service/audit_record_023` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9752` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - PASS: account_7637:rule_01 (evidence_87)
  - FAIL: analytics_1103:rule_07 (evidence_87)
  - PASS: analytics_7150:rule_07 (evidence_87)
  - UNKNOWN: audit_record_023:observed (no evidence)
  - FAIL: search_9752:rule_03 (evidence_87)

## case_126 - COMPLETE
- subject: `user_124`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_8819` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`identity`
  - `analytics_platform/analytics_1402` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_87` link=`run-fingerprint`
  - `security_service/audit_record_6884` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - PASS: account_8819:rule_01 (evidence_87)
  - PASS: analytics_1402:rule_07 (evidence_87)
  - PASS: audit_record_6884:rule_12 (evidence_87)

## case_127 - COMPLETE
- subject: `user_125`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6805` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`identity+run`
  - `security_service/audit_record_9649` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - PASS: account_6805:rule_01 (evidence_87)
  - PASS: audit_record_9649:rule_12 (evidence_87)

## case_128 - INCOMPLETE
- subject: `user_126`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7878` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `security_service/audit_record_4249` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_5550` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_87` link=`identity`
  - PASS: account_7878:rule_01 (evidence_87)
  - UNKNOWN: audit_record_4249:observed (no evidence)
  - FAIL: data_flow_5550:no-rule:recreation-path (evidence_87)

## case_129 - INCOMPLETE
- subject: `user_127`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6673` [USER_PROFILE] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - `security_service/audit_record_5606` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5148` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - FAIL: account_6673:rule_01 (evidence_87)
  - UNKNOWN: audit_record_5606:observed (no evidence)
  - FAIL: search_5148:rule_03 (evidence_87)

## case_130 - INCOMPLETE
- subject: `user_128`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8729` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `security_service/audit_record_7634` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_2364` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - `support_platform/support_187` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - PASS: account_8729:rule_01 (evidence_87)
  - UNKNOWN: audit_record_7634:observed (no evidence)
  - FAIL: search_2364:rule_03 (evidence_87)
  - FAIL: support_187:rule_05 (evidence_87)

## case_131 - INCOMPLETE
- subject: `user_129`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_426` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `analytics_platform/analytics_514` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - `security_service/audit_record_8457` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_538` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - `support_platform/support_2315` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - `support_platform/support_7208` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_87` link=`identity`
  - PASS: account_426:rule_01 (evidence_87)
  - FAIL: analytics_514:rule_07 (evidence_87)
  - UNKNOWN: audit_record_8457:observed (no evidence)
  - FAIL: search_538:rule_03 (evidence_87)
  - FAIL: support_2315:rule_05 (evidence_87)
  - FAIL: support_7208:rule_05 (evidence_87)

## case_132 - INCOMPLETE
- subject: `user_130`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4395` [USER_PROFILE] state=`ABSENT` evidence=`evidence_87` link=`run-elimination`
  - `security_service/audit_record_1424` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_9157` [USER_EXPORT] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - `search_service/search_3112` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_87` link=`identity`
  - PASS: account_4395:rule_01 (evidence_87)
  - UNKNOWN: audit_record_1424:observed (no evidence)
  - FAIL: export_9157:rule_09 (evidence_87)
  - FAIL: search_3112:rule_03 (evidence_87)

## case_133 - INCOMPLETE
- subject: `user_131`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9191` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_3130` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `integration_service/data_flow_4227` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_13` link=`identity`
  - `search_service/search_1474` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - PASS: account_9191:rule_01 (evidence_13)
  - PASS: audit_record_3130:rule_12 (evidence_13)
  - FAIL: data_flow_4227:no-rule:recreation-path (evidence_13)
  - FAIL: search_1474:rule_03 (evidence_13)

## case_134 - INCOMPLETE
- subject: `user_132`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1084` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `analytics_platform/analytics_7772` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_4064` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `integration_service/data_flow_7812` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_13` link=`identity`
  - `search_service/search_7941` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `support_platform/support_4410` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - PASS: account_1084:rule_01 (evidence_13)
  - FAIL: analytics_7772:rule_07 (evidence_13)
  - PASS: audit_record_4064:rule_12 (evidence_13)
  - FAIL: data_flow_7812:no-rule:recreation-path (evidence_13)
  - FAIL: search_7941:rule_03 (evidence_13)
  - FAIL: support_4410:rule_05 (evidence_13)

## case_135 - COMPLETE
- subject: `user_133`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1417` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_5140` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - PASS: account_1417:rule_01 (evidence_13)
  - PASS: audit_record_5140:rule_12 (evidence_13)

## case_136 - INCOMPLETE
- subject: `user_134`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4079` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_7931` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `search_service/search_1110` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `support_platform/support_4442` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - PASS: account_4079:rule_01 (evidence_13)
  - PASS: audit_record_7931:rule_12 (evidence_13)
  - FAIL: search_1110:rule_03 (evidence_13)
  - FAIL: support_4442:rule_05 (evidence_13)

## case_137 - COMPLETE
- subject: `user_135`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3734` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_6779` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - PASS: account_3734:rule_01 (evidence_13)
  - PASS: audit_record_6779:rule_12 (evidence_13)

## case_138 - INCOMPLETE
- subject: `user_136`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6452` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_122` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `search_service/search_4464` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `support_platform/support_2716` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - PASS: account_6452:rule_01 (evidence_13)
  - PASS: audit_record_122:rule_12 (evidence_13)
  - FAIL: search_4464:rule_03 (evidence_13)
  - FAIL: support_2716:rule_05 (evidence_13)

## case_139 - INCOMPLETE
- subject: `user_137`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_907` [USER_PROFILE] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_7689` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `search_service/search_6677` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - FAIL: account_907:rule_01 (evidence_13)
  - PASS: audit_record_7689:rule_12 (evidence_13)
  - FAIL: search_6677:rule_03 (evidence_13)

## case_140 - INCOMPLETE
- subject: `user_138`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_6372` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `analytics_platform/analytics_3006` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_8086` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `integration_service/data_flow_9030` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_13` link=`identity`
  - `search_service/search_7363` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `support_platform/support_5323` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - PASS: account_6372:rule_01 (evidence_13)
  - FAIL: analytics_3006:rule_07 (evidence_13)
  - PASS: audit_record_8086:rule_12 (evidence_13)
  - FAIL: data_flow_9030:no-rule:recreation-path (evidence_13)
  - FAIL: search_7363:rule_03 (evidence_13)
  - FAIL: support_5323:rule_05 (evidence_13)

## case_141 - INCOMPLETE
- subject: `user_139`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_923` [USER_PROFILE] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_5497` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `search_service/search_460` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - FAIL: account_923:rule_01 (evidence_13)
  - PASS: audit_record_5497:rule_12 (evidence_13)
  - FAIL: search_460:rule_03 (evidence_13)

## case_142 - INCOMPLETE
- subject: `user_140`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2434` [USER_PROFILE] state=`ABSENT` evidence=`evidence_13` link=`identity`
  - `security_service/audit_record_280` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `search_service/search_2024` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_13` link=`identity`
  - `support_platform/support_771` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_13` link=`identity`
  - PASS: account_2434:rule_01 (evidence_13)
  - PASS: audit_record_280:rule_12 (evidence_13)
  - FAIL: search_2024:rule_03 (evidence_13)
  - FAIL: support_771:rule_05 (evidence_13)

## case_143 - INCOMPLETE
- subject: `user_141`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_5572` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-fingerprint`
  - `search_service/search_6137` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - `support_platform/support_6560` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_86` link=`identity`
  - PASS: account_5572:rule_01 (evidence_15)
  - FAIL: search_6137:rule_03 (evidence_86)
  - FAIL: support_6560:rule_05 (evidence_86)

## case_144 - INCOMPLETE
- subject: `user_142`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_6826` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `export_service/export_7992` [USER_EXPORT] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_6826:rule_01 (evidence_15)
  - FAIL: export_7992:rule_09 (evidence_86)

## case_145 - INCOMPLETE
- subject: `user_143`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2900` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `integration_service/data_flow_7253` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_86` link=`identity`
  - `search_service/search_1725` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_2900:rule_01 (evidence_15)
  - FAIL: data_flow_7253:no-rule:recreation-path (evidence_86)
  - FAIL: search_1725:rule_03 (evidence_86)

## case_146 - INCOMPLETE
- subject: `user_144`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7864` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-fingerprint`
  - `integration_service/data_flow_4889` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_86` link=`identity`
  - `search_service/search_2262` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_7864:rule_01 (evidence_15)
  - FAIL: data_flow_4889:no-rule:recreation-path (evidence_86)
  - FAIL: search_2262:rule_03 (evidence_86)

## case_147 - INCOMPLETE
- subject: `user_145`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_8632` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-fingerprint`
  - `backup_service/backup_4244` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_86` link=`identity`
  - PASS: account_8632:rule_01 (evidence_15)
  - FAIL: backup_4244:rule_14 (evidence_86)

## case_148 - INCOMPLETE
- subject: `user_146`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5023` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-fingerprint`
  - `search_service/search_7239` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - `support_platform/support_5716` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_86` link=`identity`
  - PASS: account_5023:rule_01 (evidence_15)
  - FAIL: search_7239:rule_03 (evidence_86)
  - FAIL: support_5716:rule_05 (evidence_86)

## case_149 - INCOMPLETE
- subject: `user_147`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9505` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `analytics_platform/analytics_1626` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_86` link=`run-ambiguous`
  - `analytics_platform/analytics_5886` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_86` link=`identity`
  - `search_service/search_7672` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_9505:rule_01 (evidence_15)
  - PASS: analytics_1626:rule_07 (evidence_86)
  - FAIL: analytics_5886:rule_07 (evidence_86)
  - FAIL: search_7672:rule_03 (evidence_86)

## case_150 - COMPLETE
- subject: `user_148`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_3897` [USER_PROFILE] state=`ABSENT` evidence=`evidence_86` link=`run-elimination`
  - `analytics_platform/analytics_7254` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_86` link=`run-fingerprint`
  - `security_service/audit_record_1584` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_3897:rule_01 (evidence_86)
  - PASS: analytics_7254:rule_07 (evidence_86)
  - PASS: audit_record_1584:rule_12 (evidence_86)

## case_151 - COMPLETE
- subject: `user_149`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_874` [USER_PROFILE] state=`ABSENT` evidence=`evidence_86` link=`run-elimination`
  - `security_service/audit_record_8905` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - `backup_service/backup_9557` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_86` link=`identity`
  - `integration_service/data_flow_2437` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_86` link=`identity`
  - `support_platform/support_5400` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_86` link=`identity`
  - PASS: account_874:rule_01 (evidence_86)
  - PASS: audit_record_8905:rule_12 (evidence_86)
  - PASS: backup_9557:rule_14 (evidence_86)
  - PASS: data_flow_2437:no-rule:recreation-path (evidence_86)
  - PASS: support_5400:rule_05 (evidence_86)

## case_152 - COMPLETE
- subject: `user_150`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8854` [USER_PROFILE] state=`ABSENT` evidence=`evidence_86` link=`run-elimination`
  - `security_service/audit_record_3579` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_86` link=`identity`
  - PASS: account_8854:rule_01 (evidence_86)
  - PASS: audit_record_3579:rule_12 (evidence_86)

## case_153 - INCOMPLETE
- subject: `user_151`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8023` [USER_PROFILE] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `security_service/audit_record_5652` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `search_service/search_9831` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - FAIL: account_8023:rule_01 (evidence_15)
  - PASS: audit_record_5652:rule_12 (evidence_15)
  - FAIL: search_9831:rule_03 (evidence_15)

## case_154 - INCOMPLETE
- subject: `user_152`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7680` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_2580` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `search_service/search_1446` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_7680:rule_01 (evidence_15)
  - PASS: audit_record_2580:rule_12 (evidence_15)
  - FAIL: search_1446:rule_03 (evidence_15)

## case_155 - COMPLETE
- subject: `user_153`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1992` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-fingerprint`
  - `analytics_platform/analytics_7372` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_15` link=`run-fingerprint`
  - `security_service/audit_record_4199` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `backup_service/backup_161` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_15` link=`identity`
  - `integration_service/data_flow_4305` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_15` link=`identity`
  - `support_platform/support_7867` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_15` link=`identity`
  - PASS: account_1992:rule_01 (evidence_15)
  - PASS: analytics_7372:rule_07 (evidence_15)
  - PASS: audit_record_4199:rule_12 (evidence_15)
  - PASS: backup_161:rule_14 (evidence_15)
  - PASS: data_flow_4305:no-rule:recreation-path (evidence_15)
  - PASS: support_7867:rule_05 (evidence_15)

## case_156 - INCOMPLETE
- subject: `user_154`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_2362` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_5890` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `export_service/export_5897` [USER_EXPORT] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `search_service/search_4870` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_2362:rule_01 (evidence_15)
  - PASS: audit_record_5890:rule_12 (evidence_15)
  - FAIL: export_5897:rule_09 (evidence_15)
  - FAIL: search_4870:rule_03 (evidence_15)

## case_157 - COMPLETE
- subject: `user_155`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_2154` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `analytics_platform/analytics_8425` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_15` link=`run-fingerprint`
  - `security_service/audit_record_8821` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_2154:rule_01 (evidence_15)
  - PASS: analytics_8425:rule_07 (evidence_15)
  - PASS: audit_record_8821:rule_12 (evidence_15)

## case_158 - INCOMPLETE
- subject: `user_156`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1421` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_9665` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `integration_service/data_flow_7704` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_15` link=`identity`
  - `search_service/search_9834` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_1421:rule_01 (evidence_15)
  - PASS: audit_record_9665:rule_12 (evidence_15)
  - FAIL: data_flow_7704:no-rule:recreation-path (evidence_15)
  - FAIL: search_9834:rule_03 (evidence_15)

## case_159 - INCOMPLETE
- subject: `user_157`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_4272` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_8742` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `backup_service/backup_1214` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_15` link=`identity`
  - PASS: account_4272:rule_01 (evidence_15)
  - PASS: audit_record_8742:rule_12 (evidence_15)
  - FAIL: backup_1214:rule_14 (evidence_15)

## case_160 - INCOMPLETE
- subject: `user_158`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1688` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_9882` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - `support_platform/support_4148` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_15` link=`identity`
  - PASS: account_1688:rule_01 (evidence_15)
  - PASS: audit_record_9882:rule_12 (evidence_15)
  - FAIL: support_4148:rule_05 (evidence_15)

## case_161 - INCOMPLETE
- subject: `user_159`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5501` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `analytics_platform/analytics_2008` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_15` link=`identity`
  - `security_service/audit_record_8002` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_5501:rule_01 (evidence_15)
  - FAIL: analytics_2008:rule_07 (evidence_15)
  - PASS: audit_record_8002:rule_12 (evidence_15)

## case_162 - COMPLETE
- subject: `user_160`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_5983` [USER_PROFILE] state=`ABSENT` evidence=`evidence_15` link=`run-elimination`
  - `security_service/audit_record_6362` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_15` link=`identity`
  - PASS: account_5983:rule_01 (evidence_15)
  - PASS: audit_record_6362:rule_12 (evidence_15)

## case_163 - INCOMPLETE
- subject: `user_161`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4289` [USER_PROFILE] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - `security_service/audit_record_1053` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_4509` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - FAIL: account_4289:rule_01 (evidence_85)
  - UNKNOWN: audit_record_1053:observed (no evidence)
  - FAIL: search_4509:rule_03 (evidence_85)

## case_164 - COMPLETE
- subject: `user_162`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9549` [USER_PROFILE] state=`ABSENT` evidence=`evidence_85` link=`identity`
  - `analytics_platform/analytics_6402` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_85` link=`run-fingerprint`
  - `security_service/audit_record_6780` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - PASS: account_9549:rule_01 (evidence_85)
  - PASS: analytics_6402:rule_07 (evidence_85)
  - PASS: audit_record_6780:rule_12 (evidence_85)

## case_165 - INCOMPLETE
- subject: `user_163`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3064` [USER_PROFILE] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - `analytics_platform/analytics_2713` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_85` link=`identity`
  - `security_service/audit_record_4964` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8678` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - `support_platform/support_3586` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_85` link=`identity`
  - FAIL: account_3064:rule_01 (evidence_85)
  - FAIL: analytics_2713:rule_07 (evidence_85)
  - UNKNOWN: audit_record_4964:observed (no evidence)
  - FAIL: search_8678:rule_03 (evidence_85)
  - FAIL: support_3586:rule_05 (evidence_85)

## case_166 - INCOMPLETE
- subject: `user_164`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1837` [USER_PROFILE] state=`ABSENT` evidence=`evidence_17` link=`identity`
  - `security_service/audit_record_7082` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5261` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - `support_platform/support_3155` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_85` link=`identity`
  - PASS: account_1837:rule_01 (evidence_17)
  - UNKNOWN: audit_record_7082:observed (no evidence)
  - FAIL: search_5261:rule_03 (evidence_85)
  - FAIL: support_3155:rule_05 (evidence_85)

## case_167 - COMPLETE
- subject: `user_165`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5284` [USER_PROFILE] state=`ABSENT` evidence=`evidence_85` link=`identity`
  - `security_service/audit_record_3088` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - PASS: account_5284:rule_01 (evidence_85)
  - PASS: audit_record_3088:rule_12 (evidence_85)

## case_168 - INCOMPLETE
- subject: `user_166`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8748` [USER_PROFILE] state=`ABSENT` evidence=`evidence_17` link=`identity`
  - `security_service/audit_record_2503` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_4102` [USER_EXPORT] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - PASS: account_8748:rule_01 (evidence_17)
  - UNKNOWN: audit_record_2503:observed (no evidence)
  - FAIL: export_4102:rule_09 (evidence_85)

## case_169 - INCOMPLETE
- subject: `user_167`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7268` [USER_PROFILE] state=`ABSENT` evidence=`evidence_17` link=`identity`
  - `security_service/audit_record_5374` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_7004` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_85` link=`identity`
  - `search_service/search_2126` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - PASS: account_7268:rule_01 (evidence_17)
  - UNKNOWN: audit_record_5374:observed (no evidence)
  - FAIL: data_flow_7004:no-rule:recreation-path (evidence_85)
  - FAIL: search_2126:rule_03 (evidence_85)

## case_170 - COMPLETE
- subject: `user_168`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_665` [USER_PROFILE] state=`ABSENT` evidence=`evidence_85` link=`identity`
  - `analytics_platform/analytics_6980` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_85` link=`run-fingerprint`
  - `security_service/audit_record_4443` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - PASS: account_665:rule_01 (evidence_85)
  - PASS: analytics_6980:rule_07 (evidence_85)
  - PASS: audit_record_4443:rule_12 (evidence_85)

## case_171 - INCOMPLETE
- subject: `user_169`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_7947` [USER_PROFILE] state=`ABSENT` evidence=`evidence_17` link=`identity`
  - `security_service/audit_record_1665` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_5520` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_85` link=`identity`
  - PASS: account_7947:rule_01 (evidence_17)
  - UNKNOWN: audit_record_1665:observed (no evidence)
  - FAIL: backup_5520:rule_14 (evidence_85)

## case_172 - INCOMPLETE
- subject: `user_170`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5675` [USER_PROFILE] state=`ABSENT` evidence=`evidence_17` link=`identity`
  - `security_service/audit_record_6136` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_7102` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_85` link=`identity`
  - `support_platform/support_2322` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_85` link=`identity`
  - PASS: account_5675:rule_01 (evidence_17)
  - UNKNOWN: audit_record_6136:observed (no evidence)
  - FAIL: search_7102:rule_03 (evidence_85)
  - FAIL: support_2322:rule_05 (evidence_85)

## case_173 - INCOMPLETE
- subject: `user_171`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_6554` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `analytics_platform/analytics_6000` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - `security_service/audit_record_4126` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9523` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - PASS: account_6554:rule_01 (evidence_84)
  - FAIL: analytics_6000:rule_07 (evidence_84)
  - UNKNOWN: audit_record_4126:observed (no evidence)
  - FAIL: search_9523:rule_03 (evidence_84)

## case_174 - INCOMPLETE
- subject: `user_172`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6659` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `security_service/audit_record_7011` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_2138` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `support_platform/support_1887` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - PASS: account_6659:rule_01 (evidence_84)
  - UNKNOWN: audit_record_7011:observed (no evidence)
  - FAIL: search_2138:rule_03 (evidence_84)
  - FAIL: support_1887:rule_05 (evidence_84)

## case_175 - COMPLETE
- subject: `user_173`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_246` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`identity+run`
  - `analytics_platform/analytics_9505` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_84` link=`run-fingerprint`
  - `security_service/audit_record_7166` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `backup_service/backup_549` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_84` link=`identity`
  - `integration_service/data_flow_4319` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_84` link=`identity`
  - `support_platform/support_8164` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_84` link=`identity`
  - PASS: account_246:rule_01 (evidence_84)
  - PASS: analytics_9505:rule_07 (evidence_84)
  - PASS: audit_record_7166:rule_12 (evidence_84)
  - PASS: backup_549:rule_14 (evidence_84)
  - PASS: data_flow_4319:no-rule:recreation-path (evidence_84)
  - PASS: support_8164:rule_05 (evidence_84)

## case_176 - INCOMPLETE
- subject: `user_174`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9877` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `security_service/audit_record_1222` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_296` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_84` link=`identity`
  - `search_service/search_8860` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - PASS: account_9877:rule_01 (evidence_84)
  - UNKNOWN: audit_record_1222:observed (no evidence)
  - FAIL: data_flow_296:no-rule:recreation-path (evidence_84)
  - FAIL: search_8860:rule_03 (evidence_84)

## case_177 - INCOMPLETE
- subject: `user_175`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8423` [USER_PROFILE] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `security_service/audit_record_6729` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_3038` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - FAIL: account_8423:rule_01 (evidence_84)
  - UNKNOWN: audit_record_6729:observed (no evidence)
  - FAIL: search_3038:rule_03 (evidence_84)

## case_178 - COMPLETE
- subject: `user_176`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1090` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `analytics_platform/analytics_2414` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_84` link=`run-fingerprint`
  - `security_service/audit_record_8521` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - PASS: account_1090:rule_01 (evidence_84)
  - PASS: analytics_2414:rule_07 (evidence_84)
  - PASS: audit_record_8521:rule_12 (evidence_84)

## case_179 - INCOMPLETE
- subject: `user_177`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3482` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `security_service/audit_record_919` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_2283` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - PASS: account_3482:rule_01 (evidence_84)
  - UNKNOWN: audit_record_919:observed (no evidence)
  - FAIL: support_2283:rule_05 (evidence_84)

## case_180 - INCOMPLETE
- subject: `user_178`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9876` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `analytics_platform/analytics_1391` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - `security_service/audit_record_2207` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_7156` [USER_EXPORT] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `search_service/search_5570` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `support_platform/support_2609` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - PASS: account_9876:rule_01 (evidence_84)
  - FAIL: analytics_1391:rule_07 (evidence_84)
  - UNKNOWN: audit_record_2207:observed (no evidence)
  - FAIL: export_7156:rule_09 (evidence_84)
  - FAIL: search_5570:rule_03 (evidence_84)
  - FAIL: support_2609:rule_05 (evidence_84)

## case_181 - INCOMPLETE
- subject: `user_179`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_5309` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `security_service/audit_record_3625` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_8346` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_84` link=`identity`
  - `search_service/search_4894` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - PASS: account_5309:rule_01 (evidence_84)
  - UNKNOWN: audit_record_3625:observed (no evidence)
  - FAIL: data_flow_8346:no-rule:recreation-path (evidence_84)
  - FAIL: search_4894:rule_03 (evidence_84)

## case_182 - INCOMPLETE
- subject: `user_180`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2322` [USER_PROFILE] state=`ABSENT` evidence=`evidence_84` link=`run-elimination`
  - `analytics_platform/analytics_1522` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - `security_service/audit_record_8354` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_7450` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_84` link=`identity`
  - `search_service/search_2073` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_84` link=`identity`
  - `support_platform/support_4806` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_84` link=`identity`
  - PASS: account_2322:rule_01 (evidence_84)
  - FAIL: analytics_1522:rule_07 (evidence_84)
  - UNKNOWN: audit_record_8354:observed (no evidence)
  - FAIL: data_flow_7450:no-rule:recreation-path (evidence_84)
  - FAIL: search_2073:rule_03 (evidence_84)
  - FAIL: support_4806:rule_05 (evidence_84)

## case_183 - COMPLETE
- subject: `user_181`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_4854` [USER_PROFILE] state=`ABSENT` evidence=`evidence_83` link=`run-elimination`
  - `security_service/audit_record_3262` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - PASS: account_4854:rule_01 (evidence_83)
  - PASS: audit_record_3262:rule_12 (evidence_83)

## case_184 - INCOMPLETE
- subject: `user_182`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_9620` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `search_service/search_8680` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `support_platform/support_1892` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - PASS: account_9620:rule_01 (evidence_20)
  - FAIL: search_8680:rule_03 (evidence_83)
  - FAIL: support_1892:rule_05 (evidence_83)

## case_185 - INCOMPLETE
- subject: `user_183`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9579` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `analytics_platform/analytics_1950` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - `search_service/search_8463` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - PASS: account_9579:rule_01 (evidence_20)
  - FAIL: analytics_1950:rule_07 (evidence_83)
  - FAIL: search_8463:rule_03 (evidence_83)

## case_186 - INCOMPLETE
- subject: `user_184`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_3878` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `integration_service/data_flow_7428` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_83` link=`identity`
  - `search_service/search_4062` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - PASS: account_3878:rule_01 (evidence_20)
  - FAIL: data_flow_7428:no-rule:recreation-path (evidence_83)
  - FAIL: search_4062:rule_03 (evidence_83)

## case_187 - INCOMPLETE
- subject: `user_185`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5375` [USER_PROFILE] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `search_service/search_9921` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - FAIL: account_5375:rule_01 (evidence_83)
  - FAIL: search_9921:rule_03 (evidence_83)

## case_188 - INCOMPLETE
- subject: `user_186`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_796` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `integration_service/data_flow_707` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_83` link=`identity`
  - `search_service/search_3223` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - PASS: account_796:rule_01 (evidence_20)
  - FAIL: data_flow_707:no-rule:recreation-path (evidence_83)
  - FAIL: search_3223:rule_03 (evidence_83)

## case_189 - INCOMPLETE
- subject: `user_187`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5848` [USER_PROFILE] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `analytics_platform/analytics_1120` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - `search_service/search_4334` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `support_platform/support_8447` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - FAIL: account_5848:rule_01 (evidence_83)
  - FAIL: analytics_1120:rule_07 (evidence_83)
  - FAIL: search_4334:rule_03 (evidence_83)
  - FAIL: support_8447:rule_05 (evidence_83)

## case_190 - COMPLETE
- subject: `user_188`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7063` [USER_PROFILE] state=`ABSENT` evidence=`evidence_83` link=`run-elimination`
  - `analytics_platform/analytics_8767` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_83` link=`run-fingerprint`
  - `security_service/audit_record_4417` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - PASS: account_7063:rule_01 (evidence_83)
  - PASS: analytics_8767:rule_07 (evidence_83)
  - PASS: audit_record_4417:rule_12 (evidence_83)

## case_191 - COMPLETE
- subject: `user_189`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9317` [USER_PROFILE] state=`ABSENT` evidence=`evidence_83` link=`run-fingerprint`
  - `analytics_platform/analytics_5614` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_83` link=`run-fingerprint`
  - `security_service/audit_record_7493` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `backup_service/backup_3010` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_83` link=`identity`
  - `integration_service/data_flow_1611` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_83` link=`identity`
  - `support_platform/support_5049` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_83` link=`identity`
  - PASS: account_9317:rule_01 (evidence_83)
  - PASS: analytics_5614:rule_07 (evidence_83)
  - PASS: audit_record_7493:rule_12 (evidence_83)
  - PASS: backup_3010:rule_14 (evidence_83)
  - PASS: data_flow_1611:no-rule:recreation-path (evidence_83)
  - PASS: support_5049:rule_05 (evidence_83)

## case_192 - INCOMPLETE
- subject: `user_190`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6608` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `analytics_platform/analytics_4472` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - `export_service/export_2705` [USER_EXPORT] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `search_service/search_6680` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_83` link=`identity`
  - `support_platform/support_5493` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_83` link=`identity`
  - PASS: account_6608:rule_01 (evidence_20)
  - FAIL: analytics_4472:rule_07 (evidence_83)
  - FAIL: export_2705:rule_09 (evidence_83)
  - FAIL: search_6680:rule_03 (evidence_83)
  - FAIL: support_5493:rule_05 (evidence_83)

## case_193 - COMPLETE
- subject: `user_191`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1065` [USER_PROFILE] state=`ABSENT` evidence=`evidence_82` link=`identity`
  - `analytics_platform/analytics_8037` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_82` link=`run-fingerprint`
  - `security_service/audit_record_1839` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_1065:rule_01 (evidence_82)
  - PASS: analytics_8037:rule_07 (evidence_82)
  - PASS: audit_record_1839:rule_12 (evidence_82)

## case_194 - INCOMPLETE
- subject: `user_192`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_660` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `integration_service/data_flow_3195` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_82` link=`identity`
  - `search_service/search_8302` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_660:rule_01 (evidence_20)
  - FAIL: data_flow_3195:no-rule:recreation-path (evidence_82)
  - FAIL: search_8302:rule_03 (evidence_82)

## case_195 - COMPLETE
- subject: `user_193`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_4320` [USER_PROFILE] state=`ABSENT` evidence=`evidence_82` link=`identity`
  - `analytics_platform/analytics_3454` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_82` link=`run-fingerprint`
  - `security_service/audit_record_1524` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_4320:rule_01 (evidence_82)
  - PASS: analytics_3454:rule_07 (evidence_82)
  - PASS: audit_record_1524:rule_12 (evidence_82)

## case_196 - COMPLETE
- subject: `user_194`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5599` [USER_PROFILE] state=`ABSENT` evidence=`evidence_82` link=`identity`
  - `analytics_platform/analytics_5166` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_82` link=`run-fingerprint`
  - `security_service/audit_record_6389` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_5599:rule_01 (evidence_82)
  - PASS: analytics_5166:rule_07 (evidence_82)
  - PASS: audit_record_6389:rule_12 (evidence_82)

## case_197 - INCOMPLETE
- subject: `user_195`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2952` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `analytics_platform/analytics_6093` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_82` link=`identity`
  - `search_service/search_6762` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_2952:rule_01 (evidence_20)
  - FAIL: analytics_6093:rule_07 (evidence_82)
  - FAIL: search_6762:rule_03 (evidence_82)

## case_198 - INCOMPLETE
- subject: `user_196`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2210` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `search_service/search_1414` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - `support_platform/support_6131` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_82` link=`identity`
  - PASS: account_2210:rule_01 (evidence_20)
  - FAIL: search_1414:rule_03 (evidence_82)
  - FAIL: support_6131:rule_05 (evidence_82)

## case_199 - INCOMPLETE
- subject: `user_197`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9917` [USER_PROFILE] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - `search_service/search_9161` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - FAIL: account_9917:rule_01 (evidence_82)
  - FAIL: search_9161:rule_03 (evidence_82)

## case_200 - INCOMPLETE
- subject: `user_198`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1964` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `integration_service/data_flow_2310` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_82` link=`identity`
  - `search_service/search_7472` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_1964:rule_01 (evidence_20)
  - FAIL: data_flow_2310:no-rule:recreation-path (evidence_82)
  - FAIL: search_7472:rule_03 (evidence_82)

## case_201 - INCOMPLETE
- subject: `user_199`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_2933` [USER_PROFILE] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - `integration_service/data_flow_5688` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_82` link=`identity`
  - `search_service/search_5135` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - `support_platform/support_2863` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_82` link=`identity`
  - FAIL: account_2933:rule_01 (evidence_82)
  - FAIL: data_flow_5688:no-rule:recreation-path (evidence_82)
  - FAIL: search_5135:rule_03 (evidence_82)
  - FAIL: support_2863:rule_05 (evidence_82)

## case_202 - COMPLETE
- subject: `user_200`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5547` [USER_PROFILE] state=`ABSENT` evidence=`evidence_82` link=`identity`
  - `analytics_platform/analytics_349` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_82` link=`run-fingerprint`
  - `security_service/audit_record_5401` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_82` link=`identity`
  - PASS: account_5547:rule_01 (evidence_82)
  - PASS: analytics_349:rule_07 (evidence_82)
  - PASS: audit_record_5401:rule_12 (evidence_82)

## case_203 - INCOMPLETE
- subject: `user_201`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2399` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_1159` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `search_service/search_7542` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `support_platform/support_8903` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - PASS: account_2399:rule_01 (evidence_20)
  - PASS: audit_record_1159:rule_12 (evidence_20)
  - FAIL: search_7542:rule_03 (evidence_20)
  - FAIL: support_8903:rule_06 (evidence_20)

## case_204 - COMPLETE
- subject: `user_202`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9268` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `analytics_platform/analytics_2463` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_2736` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `backup_service/backup_9519` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_20` link=`identity`
  - `integration_service/data_flow_5877` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_20` link=`identity`
  - `support_platform/support_9505` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_20` link=`identity`
  - PASS: account_9268:rule_01 (evidence_20)
  - PASS: analytics_2463:rule_07 (evidence_20)
  - PASS: audit_record_2736:rule_12 (evidence_20)
  - PASS: backup_9519:rule_14 (evidence_20)
  - PASS: data_flow_5877:no-rule:recreation-path (evidence_20)
  - PASS: support_9505:rule_05 (evidence_20)

## case_205 - INCOMPLETE
- subject: `user_203`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6726` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_5023` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `integration_service/data_flow_3530` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_20` link=`identity`
  - `search_service/search_540` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - PASS: account_6726:rule_01 (evidence_20)
  - PASS: audit_record_5023:rule_12 (evidence_20)
  - FAIL: data_flow_3530:no-rule:recreation-path (evidence_20)
  - FAIL: search_540:rule_03 (evidence_20)

## case_206 - COMPLETE
- subject: `user_204`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4522` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `analytics_platform/analytics_9580` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_9878` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - PASS: account_4522:rule_01 (evidence_20)
  - PASS: analytics_9580:rule_07 (evidence_20)
  - PASS: audit_record_9878:rule_12 (evidence_20)

## case_207 - INCOMPLETE
- subject: `user_205`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_5678` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_3578` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `backup_service/backup_6407` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_20` link=`identity`
  - PASS: account_5678:rule_01 (evidence_20)
  - PASS: audit_record_3578:rule_12 (evidence_20)
  - FAIL: backup_6407:rule_14 (evidence_20)

## case_208 - INCOMPLETE
- subject: `user_206`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3685` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-fingerprint`
  - `security_service/audit_record_2697` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `search_service/search_1118` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `support_platform/support_2134` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_20` link=`identity`
  - PASS: account_3685:rule_01 (evidence_20)
  - PASS: audit_record_2697:rule_12 (evidence_20)
  - FAIL: search_1118:rule_03 (evidence_20)
  - FAIL: support_2134:rule_05 (evidence_20)

## case_209 - INCOMPLETE
- subject: `user_207`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6934` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `analytics_platform/analytics_3156` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_20` link=`identity`
  - `security_service/audit_record_8189` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `integration_service/data_flow_5196` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_20` link=`identity`
  - `search_service/search_7288` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `support_platform/support_8999` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_20` link=`identity`
  - PASS: account_6934:rule_01 (evidence_20)
  - FAIL: analytics_3156:rule_07 (evidence_20)
  - PASS: audit_record_8189:rule_12 (evidence_20)
  - FAIL: data_flow_5196:no-rule:recreation-path (evidence_20)
  - FAIL: search_7288:rule_03 (evidence_20)
  - FAIL: support_8999:rule_05 (evidence_20)

## case_210 - INCOMPLETE
- subject: `user_208`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4362` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `security_service/audit_record_6796` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `search_service/search_045` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `support_platform/support_4491` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_20` link=`identity`
  - PASS: account_4362:rule_01 (evidence_20)
  - PASS: audit_record_6796:rule_12 (evidence_20)
  - FAIL: search_045:rule_03 (evidence_20)
  - FAIL: support_4491:rule_05 (evidence_20)

## case_211 - INCOMPLETE
- subject: `user_209`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4348` [USER_PROFILE] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `security_service/audit_record_7804` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `search_service/search_9955` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - FAIL: account_4348:rule_01 (evidence_20)
  - PASS: audit_record_7804:rule_12 (evidence_20)
  - FAIL: search_9955:rule_03 (evidence_20)

## case_212 - INCOMPLETE
- subject: `user_210`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_418` [USER_PROFILE] state=`ABSENT` evidence=`evidence_20` link=`run-elimination`
  - `security_service/audit_record_3261` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - `integration_service/data_flow_8676` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_20` link=`identity`
  - `search_service/search_2274` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_20` link=`identity`
  - PASS: account_418:rule_01 (evidence_20)
  - PASS: audit_record_3261:rule_12 (evidence_20)
  - FAIL: data_flow_8676:no-rule:recreation-path (evidence_20)
  - FAIL: search_2274:rule_03 (evidence_20)

## case_213 - COMPLETE
- subject: `user_211`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6674` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `analytics_platform/analytics_4460` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_81` link=`run-fingerprint`
  - `security_service/audit_record_4413` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `backup_service/backup_5626` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_81` link=`identity`
  - `integration_service/data_flow_5279` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_81` link=`identity`
  - `support_platform/support_1360` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_81` link=`identity`
  - PASS: account_6674:rule_01 (evidence_81)
  - PASS: analytics_4460:rule_07 (evidence_81)
  - PASS: audit_record_4413:rule_12 (evidence_81)
  - PASS: backup_5626:rule_14 (evidence_81)
  - PASS: data_flow_5279:no-rule:recreation-path (evidence_81)
  - PASS: support_1360:rule_05 (evidence_81)

## case_214 - INCOMPLETE
- subject: `user_212`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4752` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_1666` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_7351` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `support_platform/support_1146` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_81` link=`identity`
  - PASS: account_4752:rule_01 (evidence_81)
  - UNKNOWN: audit_record_1666:observed (no evidence)
  - FAIL: search_7351:rule_03 (evidence_81)
  - FAIL: support_1146:rule_05 (evidence_81)

## case_215 - COMPLETE
- subject: `user_213`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1956` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `analytics_platform/analytics_2504` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_81` link=`run-fingerprint`
  - `security_service/audit_record_1718` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - PASS: account_1956:rule_01 (evidence_81)
  - PASS: analytics_2504:rule_07 (evidence_81)
  - PASS: audit_record_1718:rule_12 (evidence_81)

## case_216 - INCOMPLETE
- subject: `user_214`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9682` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `analytics_platform/analytics_4527` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_713` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_5351` [USER_EXPORT] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `search_service/search_5216` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `support_platform/support_8453` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_81` link=`identity`
  - PASS: account_9682:rule_01 (evidence_81)
  - FAIL: analytics_4527:rule_07 (evidence_81)
  - UNKNOWN: audit_record_713:observed (no evidence)
  - FAIL: export_5351:rule_09 (evidence_81)
  - FAIL: search_5216:rule_03 (evidence_81)
  - FAIL: support_8453:rule_05 (evidence_81)

## case_217 - INCOMPLETE
- subject: `user_215`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7030` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_188` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_1791` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_81` link=`identity`
  - `search_service/search_3120` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - PASS: account_7030:rule_01 (evidence_81)
  - UNKNOWN: audit_record_188:observed (no evidence)
  - FAIL: data_flow_1791:no-rule:recreation-path (evidence_81)
  - FAIL: search_3120:rule_03 (evidence_81)

## case_218 - COMPLETE
- subject: `user_216`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4066` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `analytics_platform/analytics_257` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_81` link=`run-fingerprint`
  - `security_service/audit_record_8792` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - PASS: account_4066:rule_01 (evidence_81)
  - PASS: analytics_257:rule_07 (evidence_81)
  - PASS: audit_record_8792:rule_12 (evidence_81)

## case_219 - COMPLETE
- subject: `user_217`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4678` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `analytics_platform/analytics_7004` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_81` link=`run-fingerprint`
  - `security_service/audit_record_3382` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - PASS: account_4678:rule_01 (evidence_81)
  - PASS: analytics_7004:rule_07 (evidence_81)
  - PASS: audit_record_3382:rule_12 (evidence_81)

## case_220 - INCOMPLETE
- subject: `user_218`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1007` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_3698` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `legal_service/legal_hold_4961` [LEGAL_HOLD_RECORD] state=`None` evidence=`-` link=`identity`
  - `search_service/search_941` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `support_platform/support_4529` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_81` link=`identity`
  - PASS: account_1007:rule_01 (evidence_81)
  - UNKNOWN: audit_record_3698:observed (no evidence)
  - UNKNOWN: legal_hold_4961:observed (no evidence)
  - FAIL: search_941:rule_03 (evidence_81)
  - FAIL: support_4529:rule_05 (evidence_81)

## case_221 - COMPLETE
- subject: `user_219`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4512` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_3880` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - PASS: account_4512:rule_01 (evidence_81)
  - PASS: audit_record_3880:rule_12 (evidence_81)

## case_222 - INCOMPLETE
- subject: `user_220`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_7237` [USER_PROFILE] state=`ABSENT` evidence=`evidence_81` link=`identity`
  - `security_service/audit_record_7211` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_6405` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_81` link=`identity`
  - `support_platform/support_111` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_81` link=`identity`
  - PASS: account_7237:rule_01 (evidence_81)
  - UNKNOWN: audit_record_7211:observed (no evidence)
  - FAIL: search_6405:rule_03 (evidence_81)
  - FAIL: support_111:rule_05 (evidence_81)

## case_223 - INCOMPLETE
- subject: `user_221`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_5479` [USER_PROFILE] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - `security_service/audit_record_234` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8764` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - FAIL: account_5479:rule_01 (evidence_80)
  - UNKNOWN: audit_record_234:observed (no evidence)
  - FAIL: search_8764:rule_03 (evidence_80)

## case_224 - INCOMPLETE
- subject: `user_222`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7605` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_6515` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_1140` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_80` link=`identity`
  - PASS: account_7605:rule_01 (evidence_78)
  - UNKNOWN: audit_record_6515:observed (no evidence)
  - FAIL: data_flow_1140:no-rule:recreation-path (evidence_80)

## case_225 - COMPLETE
- subject: `user_223`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_392` [USER_PROFILE] state=`ABSENT` evidence=`evidence_80` link=`run-ambiguous`
  - `analytics_platform/analytics_8127` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_80` link=`run-fingerprint`
  - `security_service/audit_record_9389` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - PASS: account_392:rule_01 (evidence_80)
  - PASS: analytics_8127:rule_07 (evidence_80)
  - PASS: audit_record_9389:rule_12 (evidence_80)

## case_226 - COMPLETE
- subject: `user_224`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_669` [USER_PROFILE] state=`ABSENT` evidence=`evidence_80` link=`run-ambiguous`
  - `analytics_platform/analytics_2501` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_80` link=`run-fingerprint`
  - `security_service/audit_record_9964` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - PASS: account_669:rule_01 (evidence_80)
  - PASS: analytics_2501:rule_07 (evidence_80)
  - PASS: audit_record_9964:rule_12 (evidence_80)

## case_227 - INCOMPLETE
- subject: `user_225`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5549` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_9043` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8181` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - `support_platform/support_5830` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_80` link=`identity`
  - PASS: account_5549:rule_01 (evidence_78)
  - UNKNOWN: audit_record_9043:observed (no evidence)
  - FAIL: search_8181:rule_03 (evidence_80)
  - FAIL: support_5830:rule_05 (evidence_80)

## case_228 - INCOMPLETE
- subject: `user_226`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7146` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_5029` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_3210` [USER_EXPORT] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - `search_service/search_7054` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - PASS: account_7146:rule_01 (evidence_78)
  - UNKNOWN: audit_record_5029:observed (no evidence)
  - FAIL: export_3210:rule_09 (evidence_80)
  - FAIL: search_7054:rule_03 (evidence_80)

## case_229 - INCOMPLETE
- subject: `user_227`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4552` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_4310` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_5831` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_80` link=`identity`
  - `search_service/search_3627` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - PASS: account_4552:rule_01 (evidence_78)
  - UNKNOWN: audit_record_4310:observed (no evidence)
  - FAIL: data_flow_5831:no-rule:recreation-path (evidence_80)
  - FAIL: search_3627:rule_03 (evidence_80)

## case_230 - INCOMPLETE
- subject: `user_228`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8165` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_7027` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_2516` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_80` link=`identity`
  - `search_service/search_5612` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - PASS: account_8165:rule_01 (evidence_78)
  - UNKNOWN: audit_record_7027:observed (no evidence)
  - FAIL: data_flow_2516:no-rule:recreation-path (evidence_80)
  - FAIL: search_5612:rule_03 (evidence_80)

## case_231 - COMPLETE
- subject: `user_229`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7324` [USER_PROFILE] state=`ABSENT` evidence=`evidence_80` link=`identity+run`
  - `analytics_platform/analytics_1544` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_80` link=`run-fingerprint`
  - `security_service/audit_record_4425` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_80` link=`identity`
  - `backup_service/backup_6564` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_80` link=`identity`
  - `integration_service/data_flow_2576` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_80` link=`identity`
  - `support_platform/support_3964` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_80` link=`identity`
  - PASS: account_7324:rule_01 (evidence_80)
  - PASS: analytics_1544:rule_07 (evidence_80)
  - PASS: audit_record_4425:rule_12 (evidence_80)
  - PASS: backup_6564:rule_14 (evidence_80)
  - PASS: data_flow_2576:no-rule:recreation-path (evidence_80)
  - PASS: support_3964:rule_05 (evidence_80)

## case_232 - INCOMPLETE
- subject: `user_230`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8936` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_7757` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_9862` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_80` link=`identity`
  - PASS: account_8936:rule_01 (evidence_78)
  - UNKNOWN: audit_record_7757:observed (no evidence)
  - FAIL: support_9862:rule_05 (evidence_80)

## case_233 - COMPLETE
- subject: `user_231`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5264` [USER_PROFILE] state=`ABSENT` evidence=`evidence_79` link=`identity`
  - `analytics_platform/analytics_6723` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_79` link=`run-fingerprint`
  - `security_service/audit_record_8350` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - `backup_service/backup_8162` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_79` link=`identity`
  - `integration_service/data_flow_6754` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_79` link=`identity`
  - `support_platform/support_9670` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_79` link=`identity`
  - PASS: account_5264:rule_01 (evidence_79)
  - PASS: analytics_6723:rule_07 (evidence_79)
  - PASS: audit_record_8350:rule_12 (evidence_79)
  - PASS: backup_8162:rule_14 (evidence_79)
  - PASS: data_flow_6754:no-rule:recreation-path (evidence_79)
  - PASS: support_9670:rule_05 (evidence_79)

## case_234 - INCOMPLETE
- subject: `user_232`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_2614` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`identity`
  - `security_service/audit_record_4438` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_2615` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - `support_platform/support_1254` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_79` link=`identity`
  - PASS: account_2614:rule_01 (evidence_78)
  - UNKNOWN: audit_record_4438:observed (no evidence)
  - FAIL: search_2615:rule_03 (evidence_79)
  - FAIL: support_1254:rule_05 (evidence_79)

## case_235 - COMPLETE
- subject: `user_233`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_886` [USER_PROFILE] state=`ABSENT` evidence=`evidence_79` link=`identity`
  - `analytics_platform/analytics_8565` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_79` link=`run-fingerprint`
  - `security_service/audit_record_7103` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - `backup_service/backup_2775` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_79` link=`identity`
  - `integration_service/data_flow_593` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_79` link=`identity`
  - `support_platform/support_9391` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_79` link=`identity`
  - PASS: account_886:rule_01 (evidence_79)
  - PASS: analytics_8565:rule_07 (evidence_79)
  - PASS: audit_record_7103:rule_12 (evidence_79)
  - PASS: backup_2775:rule_14 (evidence_79)
  - PASS: data_flow_593:no-rule:recreation-path (evidence_79)
  - PASS: support_9391:rule_05 (evidence_79)

## case_236 - INCOMPLETE
- subject: `user_234`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_629` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`identity`
  - `security_service/audit_record_9285` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_7352` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_79` link=`identity`
  - `search_service/search_5385` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_629:rule_01 (evidence_78)
  - UNKNOWN: audit_record_9285:observed (no evidence)
  - FAIL: data_flow_7352:no-rule:recreation-path (evidence_79)
  - FAIL: search_5385:rule_03 (evidence_79)

## case_237 - INCOMPLETE
- subject: `user_235`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2788` [USER_PROFILE] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - `security_service/audit_record_2859` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_2433` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - FAIL: account_2788:rule_01 (evidence_79)
  - UNKNOWN: audit_record_2859:observed (no evidence)
  - FAIL: search_2433:rule_03 (evidence_79)

## case_238 - COMPLETE
- subject: `user_236`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_945` [USER_PROFILE] state=`ABSENT` evidence=`evidence_79` link=`identity`
  - `security_service/audit_record_6797` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_945:rule_01 (evidence_79)
  - PASS: audit_record_6797:rule_12 (evidence_79)

## case_239 - COMPLETE
- subject: `user_237`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2838` [USER_PROFILE] state=`ABSENT` evidence=`evidence_79` link=`identity`
  - `analytics_platform/analytics_1964` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_79` link=`run-fingerprint`
  - `security_service/audit_record_4940` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_2838:rule_01 (evidence_79)
  - PASS: analytics_1964:rule_07 (evidence_79)
  - PASS: audit_record_4940:rule_12 (evidence_79)

## case_240 - INCOMPLETE
- subject: `user_238`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_6013` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`identity`
  - `security_service/audit_record_8918` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_5242` [USER_EXPORT] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - `search_service/search_9335` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_6013:rule_01 (evidence_78)
  - UNKNOWN: audit_record_8918:observed (no evidence)
  - FAIL: export_5242:rule_09 (evidence_79)
  - FAIL: search_9335:rule_03 (evidence_79)

## case_241 - INCOMPLETE
- subject: `user_239`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1789` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`identity`
  - `security_service/audit_record_436` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4568` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_79` link=`identity`
  - `search_service/search_5659` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_1789:rule_01 (evidence_78)
  - UNKNOWN: audit_record_436:observed (no evidence)
  - FAIL: data_flow_4568:no-rule:recreation-path (evidence_79)
  - FAIL: search_5659:rule_03 (evidence_79)

## case_242 - INCOMPLETE
- subject: `user_240`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3905` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`identity`
  - `security_service/audit_record_3046` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4475` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_79` link=`identity`
  - `search_service/search_2904` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_79` link=`identity`
  - PASS: account_3905:rule_01 (evidence_78)
  - UNKNOWN: audit_record_3046:observed (no evidence)
  - FAIL: data_flow_4475:no-rule:recreation-path (evidence_79)
  - FAIL: search_2904:rule_03 (evidence_79)

## case_243 - COMPLETE
- subject: `user_241`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4264` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-ambiguous`
  - `analytics_platform/analytics_9166` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_7202` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - PASS: account_4264:rule_01 (evidence_78)
  - PASS: analytics_9166:rule_07 (evidence_78)
  - PASS: audit_record_7202:rule_12 (evidence_78)

## case_244 - COMPLETE
- subject: `user_242`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7650` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-ambiguous`
  - `analytics_platform/analytics_5891` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_78` link=`run-fingerprint`
  - `security_service/audit_record_9314` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - PASS: account_7650:rule_01 (evidence_78)
  - PASS: analytics_5891:rule_07 (evidence_78)
  - PASS: audit_record_9314:rule_12 (evidence_78)

## case_245 - INCOMPLETE
- subject: `user_243`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1264` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-elimination`
  - `analytics_platform/analytics_4010` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_78` link=`identity`
  - PASS: account_1264:rule_01 (evidence_78)
  - FAIL: analytics_4010:rule_07 (evidence_78)

## case_246 - INCOMPLETE
- subject: `user_244`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2481` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `search_service/search_2725` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `support_platform/support_579` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_78` link=`identity`
  - PASS: account_2481:rule_01 (evidence_78)
  - FAIL: search_2725:rule_03 (evidence_78)
  - FAIL: support_579:rule_05 (evidence_78)

## case_247 - INCOMPLETE
- subject: `user_245`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_2981` [USER_PROFILE] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `search_service/search_9473` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - FAIL: account_2981:rule_01 (evidence_78)
  - FAIL: search_9473:rule_03 (evidence_78)

## case_248 - INCOMPLETE
- subject: `user_246`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3631` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-elimination`
  - `integration_service/data_flow_677` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_78` link=`identity`
  - PASS: account_3631:rule_01 (evidence_78)
  - FAIL: data_flow_677:no-rule:recreation-path (evidence_78)

## case_249 - INCOMPLETE
- subject: `user_247`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4181` [USER_PROFILE] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `analytics_platform/analytics_8527` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_78` link=`identity`
  - `search_service/search_8190` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `support_platform/support_1364` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_78` link=`identity`
  - FAIL: account_4181:rule_01 (evidence_78)
  - FAIL: analytics_8527:rule_07 (evidence_78)
  - FAIL: search_8190:rule_03 (evidence_78)
  - FAIL: support_1364:rule_05 (evidence_78)

## case_250 - INCOMPLETE
- subject: `user_248`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_7010` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-elimination`
  - `search_service/search_3760` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - PASS: account_7010:rule_01 (evidence_78)
  - FAIL: search_3760:rule_03 (evidence_78)

## case_251 - INCOMPLETE
- subject: `user_249`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7518` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `search_service/search_730` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `support_platform/support_4541` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_78` link=`identity`
  - PASS: account_7518:rule_01 (evidence_78)
  - FAIL: search_730:rule_03 (evidence_78)
  - FAIL: support_4541:rule_05 (evidence_78)

## case_252 - INCOMPLETE
- subject: `user_250`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4643` [USER_PROFILE] state=`ABSENT` evidence=`evidence_78` link=`run-fingerprint`
  - `export_service/export_8598` [USER_EXPORT] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - `search_service/search_2936` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_78` link=`identity`
  - PASS: account_4643:rule_01 (evidence_78)
  - FAIL: export_8598:rule_09 (evidence_78)
  - FAIL: search_2936:rule_03 (evidence_78)

## case_253 - COMPLETE
- subject: `user_251`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6073` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `analytics_platform/analytics_6136` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_24` link=`run-fingerprint`
  - `security_service/audit_record_2927` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - PASS: account_6073:rule_01 (evidence_24)
  - PASS: analytics_6136:rule_07 (evidence_24)
  - PASS: audit_record_2927:rule_12 (evidence_24)

## case_254 - INCOMPLETE
- subject: `user_252`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5047` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `security_service/audit_record_9256` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `integration_service/data_flow_6233` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_24` link=`identity`
  - `search_service/search_3011` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - PASS: account_5047:rule_01 (evidence_24)
  - PASS: audit_record_9256:rule_12 (evidence_24)
  - FAIL: data_flow_6233:no-rule:recreation-path (evidence_24)
  - FAIL: search_3011:rule_03 (evidence_24)

## case_255 - INCOMPLETE
- subject: `user_253`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5091` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `security_service/audit_record_2513` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `backup_service/backup_2427` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_24` link=`identity`
  - PASS: account_5091:rule_01 (evidence_24)
  - PASS: audit_record_2513:rule_12 (evidence_24)
  - FAIL: backup_2427:rule_14 (evidence_24)

## case_256 - INCOMPLETE
- subject: `user_254`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7542` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `security_service/audit_record_2453` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `search_service/search_4027` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `support_platform/support_3772` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_24` link=`identity`
  - PASS: account_7542:rule_01 (evidence_24)
  - PASS: audit_record_2453:rule_12 (evidence_24)
  - FAIL: search_4027:rule_03 (evidence_24)
  - FAIL: support_3772:rule_05 (evidence_24)

## case_257 - COMPLETE
- subject: `user_255`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_3601` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `analytics_platform/analytics_2977` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_24` link=`run-fingerprint`
  - `security_service/audit_record_7193` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - PASS: account_3601:rule_01 (evidence_24)
  - PASS: analytics_2977:rule_07 (evidence_24)
  - PASS: audit_record_7193:rule_12 (evidence_24)

## case_258 - INCOMPLETE
- subject: `user_256`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7942` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-fingerprint`
  - `security_service/audit_record_9890` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `search_service/search_5296` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `support_platform/support_3834` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_24` link=`identity`
  - PASS: account_7942:rule_01 (evidence_24)
  - PASS: audit_record_9890:rule_12 (evidence_24)
  - FAIL: search_5296:rule_03 (evidence_24)
  - FAIL: support_3834:rule_05 (evidence_24)

## case_259 - INCOMPLETE
- subject: `user_257`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_9608` [USER_PROFILE] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `security_service/audit_record_1421` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `search_service/search_6990` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - FAIL: account_9608:rule_01 (evidence_24)
  - PASS: audit_record_1421:rule_12 (evidence_24)
  - FAIL: search_6990:rule_03 (evidence_24)

## case_260 - COMPLETE
- subject: `user_258`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7811` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `analytics_platform/analytics_5053` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_24` link=`run-fingerprint`
  - `security_service/audit_record_1876` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - PASS: account_7811:rule_01 (evidence_24)
  - PASS: analytics_5053:rule_07 (evidence_24)
  - PASS: audit_record_1876:rule_12 (evidence_24)

## case_261 - INCOMPLETE
- subject: `user_259`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_3150` [USER_PROFILE] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `security_service/audit_record_3335` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `legal_service/legal_hold_8017` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `search_service/search_6781` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - FAIL: account_3150:rule_01 (evidence_24)
  - PASS: audit_record_3335:rule_12 (evidence_24)
  - PASS: legal_hold_8017:rule_13 (evidence_24)
  - FAIL: search_6781:rule_03 (evidence_24)

## case_262 - INCOMPLETE
- subject: `user_260`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5072` [USER_PROFILE] state=`ABSENT` evidence=`evidence_24` link=`run-elimination`
  - `security_service/audit_record_4812` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - `search_service/search_2228` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_24` link=`identity`
  - PASS: account_5072:rule_01 (evidence_24)
  - PASS: audit_record_4812:rule_12 (evidence_24)
  - FAIL: search_2228:rule_03 (evidence_24)

## case_263 - INCOMPLETE
- subject: `user_261`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_106` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `analytics_platform/analytics_515` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_6863` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `search_service/search_5331` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `support_platform/support_2498` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - `support_platform/support_5234` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - PASS: account_106:rule_01 (evidence_25)
  - FAIL: analytics_515:rule_07 (evidence_25)
  - PASS: audit_record_6863:rule_12 (evidence_25)
  - FAIL: search_5331:rule_03 (evidence_25)
  - FAIL: support_2498:rule_05 (evidence_25)
  - FAIL: support_5234:rule_06 (evidence_25)

## case_264 - COMPLETE
- subject: `user_262`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_8316` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `analytics_platform/analytics_1851` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_25` link=`run-fingerprint`
  - `security_service/audit_record_6711` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `backup_service/backup_3250` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_25` link=`identity`
  - `integration_service/data_flow_4885` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_25` link=`identity`
  - `support_platform/support_9996` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_25` link=`identity`
  - PASS: account_8316:rule_01 (evidence_25)
  - PASS: analytics_1851:rule_07 (evidence_25)
  - PASS: audit_record_6711:rule_12 (evidence_25)
  - PASS: backup_3250:rule_14 (evidence_25)
  - PASS: data_flow_4885:no-rule:recreation-path (evidence_25)
  - PASS: support_9996:rule_05 (evidence_25)

## case_265 - COMPLETE
- subject: `user_263`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5015` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_6378` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - PASS: account_5015:rule_01 (evidence_25)
  - PASS: audit_record_6378:rule_12 (evidence_25)

## case_266 - INCOMPLETE
- subject: `user_264`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1057` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_1857` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `integration_service/data_flow_8277` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_25` link=`identity`
  - `search_service/search_8935` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - PASS: account_1057:rule_01 (evidence_25)
  - PASS: audit_record_1857:rule_12 (evidence_25)
  - FAIL: data_flow_8277:no-rule:recreation-path (evidence_25)
  - FAIL: search_8935:rule_03 (evidence_25)

## case_267 - COMPLETE
- subject: `user_265`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_8384` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `analytics_platform/analytics_3793` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_25` link=`run-fingerprint`
  - `security_service/audit_record_6621` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - PASS: account_8384:rule_01 (evidence_25)
  - PASS: analytics_3793:rule_07 (evidence_25)
  - PASS: audit_record_6621:rule_12 (evidence_25)

## case_268 - INCOMPLETE
- subject: `user_266`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9179` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_4636` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `search_service/search_3000` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `support_platform/support_8215` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - PASS: account_9179:rule_01 (evidence_25)
  - PASS: audit_record_4636:rule_12 (evidence_25)
  - FAIL: search_3000:rule_03 (evidence_25)
  - FAIL: support_8215:rule_05 (evidence_25)

## case_269 - INCOMPLETE
- subject: `user_267`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_7699` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `analytics_platform/analytics_6766` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_4534` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `integration_service/data_flow_8612` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_25` link=`identity`
  - `search_service/search_1730` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `support_platform/support_8301` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - PASS: account_7699:rule_01 (evidence_25)
  - FAIL: analytics_6766:rule_07 (evidence_25)
  - PASS: audit_record_4534:rule_12 (evidence_25)
  - FAIL: data_flow_8612:no-rule:recreation-path (evidence_25)
  - FAIL: search_1730:rule_03 (evidence_25)
  - FAIL: support_8301:rule_05 (evidence_25)

## case_270 - INCOMPLETE
- subject: `user_268`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4331` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_5206` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `search_service/search_9020` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `support_platform/support_7707` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_25` link=`identity`
  - PASS: account_4331:rule_01 (evidence_25)
  - PASS: audit_record_5206:rule_12 (evidence_25)
  - FAIL: search_9020:rule_03 (evidence_25)
  - FAIL: support_7707:rule_05 (evidence_25)

## case_271 - INCOMPLETE
- subject: `user_269`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7107` [USER_PROFILE] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_2546` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `search_service/search_1390` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - FAIL: account_7107:rule_01 (evidence_25)
  - PASS: audit_record_2546:rule_12 (evidence_25)
  - FAIL: search_1390:rule_03 (evidence_25)

## case_272 - INCOMPLETE
- subject: `user_270`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_4226` [USER_PROFILE] state=`ABSENT` evidence=`evidence_25` link=`identity`
  - `security_service/audit_record_4646` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - `integration_service/data_flow_2010` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_25` link=`identity`
  - `search_service/search_3875` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_25` link=`identity`
  - PASS: account_4226:rule_01 (evidence_25)
  - PASS: audit_record_4646:rule_12 (evidence_25)
  - FAIL: data_flow_2010:no-rule:recreation-path (evidence_25)
  - FAIL: search_3875:rule_03 (evidence_25)

## case_273 - INCOMPLETE
- subject: `user_271`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_8689` [USER_PROFILE] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - `security_service/audit_record_3428` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5454` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - FAIL: account_8689:rule_01 (evidence_77)
  - UNKNOWN: audit_record_3428:observed (no evidence)
  - FAIL: search_5454:rule_03 (evidence_77)

## case_274 - COMPLETE
- subject: `user_272`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6575` [USER_PROFILE] state=`ABSENT` evidence=`evidence_77` link=`run-elimination`
  - `analytics_platform/analytics_4051` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_77` link=`run-fingerprint`
  - `security_service/audit_record_6398` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - PASS: account_6575:rule_01 (evidence_77)
  - PASS: analytics_4051:rule_07 (evidence_77)
  - PASS: audit_record_6398:rule_12 (evidence_77)

## case_275 - INCOMPLETE
- subject: `user_273`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_731` [USER_PROFILE] state=`ABSENT` evidence=`evidence_77` link=`run-fingerprint`
  - `analytics_platform/analytics_6191` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_77` link=`run-fingerprint`
  - `security_service/audit_record_4188` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5264` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - `support_platform/support_3684` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - PASS: account_731:rule_01 (evidence_77)
  - PASS: analytics_6191:rule_07 (evidence_77)
  - UNKNOWN: audit_record_4188:observed (no evidence)
  - FAIL: search_5264:rule_03 (evidence_77)
  - FAIL: support_3684:rule_05 (evidence_77)

## case_276 - COMPLETE
- subject: `user_274`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4853` [USER_PROFILE] state=`ABSENT` evidence=`evidence_77` link=`run-elimination`
  - `analytics_platform/analytics_5923` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_77` link=`run-fingerprint`
  - `security_service/audit_record_8323` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - PASS: account_4853:rule_01 (evidence_77)
  - PASS: analytics_5923:rule_07 (evidence_77)
  - PASS: audit_record_8323:rule_12 (evidence_77)

## case_277 - COMPLETE
- subject: `user_275`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2352` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `security_service/audit_record_8228` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - `backup_service/backup_9728` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_77` link=`identity`
  - `integration_service/data_flow_2439` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_77` link=`identity`
  - `support_platform/support_2036` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_77` link=`identity`
  - PASS: account_2352:rule_01 (evidence_75)
  - PASS: audit_record_8228:rule_12 (evidence_77)
  - PASS: backup_9728:rule_14 (evidence_77)
  - PASS: data_flow_2439:no-rule:recreation-path (evidence_77)
  - PASS: support_2036:rule_05 (evidence_77)

## case_278 - INCOMPLETE
- subject: `user_276`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6306` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `analytics_platform/analytics_5959` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - `security_service/audit_record_6384` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4629` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_77` link=`identity`
  - `search_service/search_8082` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - `support_platform/support_6333` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - PASS: account_6306:rule_01 (evidence_75)
  - FAIL: analytics_5959:rule_07 (evidence_77)
  - UNKNOWN: audit_record_6384:observed (no evidence)
  - FAIL: data_flow_4629:no-rule:recreation-path (evidence_77)
  - FAIL: search_8082:rule_03 (evidence_77)
  - FAIL: support_6333:rule_05 (evidence_77)

## case_279 - INCOMPLETE
- subject: `user_277`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_4664` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `security_service/audit_record_5055` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_8588` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_77` link=`identity`
  - PASS: account_4664:rule_01 (evidence_75)
  - UNKNOWN: audit_record_5055:observed (no evidence)
  - FAIL: backup_8588:rule_14 (evidence_77)

## case_280 - INCOMPLETE
- subject: `user_278`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2430` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `security_service/audit_record_1518` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_7073` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - PASS: account_2430:rule_01 (evidence_75)
  - UNKNOWN: audit_record_1518:observed (no evidence)
  - FAIL: support_7073:rule_05 (evidence_77)

## case_281 - INCOMPLETE
- subject: `user_279`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4985` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `analytics_platform/analytics_6265` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - `security_service/audit_record_111` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_9008` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_77` link=`identity`
  - `search_service/search_3364` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_77` link=`identity`
  - `support_platform/support_2757` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - PASS: account_4985:rule_01 (evidence_75)
  - FAIL: analytics_6265:rule_07 (evidence_77)
  - UNKNOWN: audit_record_111:observed (no evidence)
  - FAIL: data_flow_9008:no-rule:recreation-path (evidence_77)
  - FAIL: search_3364:rule_03 (evidence_77)
  - FAIL: support_2757:rule_05 (evidence_77)

## case_282 - INCOMPLETE
- subject: `user_280`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9763` [USER_PROFILE] state=`None` evidence=`-` link=`run-elimination`
  - `security_service/audit_record_3198` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_8370` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_77` link=`identity`
  - UNKNOWN: account_9763:observed (no evidence)
  - UNKNOWN: audit_record_3198:observed (no evidence)
  - FAIL: support_8370:rule_05 (evidence_77)

## case_283 - COMPLETE
- subject: `user_281`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_947` [USER_PROFILE] state=`ABSENT` evidence=`evidence_76` link=`identity`
  - `analytics_platform/analytics_8408` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_76` link=`run-fingerprint`
  - `security_service/audit_record_5680` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - PASS: account_947:rule_01 (evidence_76)
  - PASS: analytics_8408:rule_07 (evidence_76)
  - PASS: audit_record_5680:rule_12 (evidence_76)

## case_284 - INCOMPLETE
- subject: `user_282`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8322` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `analytics_platform/analytics_7283` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_76` link=`run-ambiguous`
  - `integration_service/data_flow_6953` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_76` link=`identity`
  - PASS: account_8322:rule_01 (evidence_75)
  - PASS: analytics_7283:rule_07 (evidence_76)
  - FAIL: data_flow_6953:no-rule:recreation-path (evidence_76)

## case_285 - INCOMPLETE
- subject: `user_283`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_285` [USER_PROFILE] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - `search_service/search_036` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - FAIL: account_285:rule_01 (evidence_76)
  - FAIL: search_036:rule_03 (evidence_76)

## case_286 - COMPLETE
- subject: `user_284`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2016` [USER_PROFILE] state=`ABSENT` evidence=`evidence_76` link=`identity`
  - `security_service/audit_record_1714` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - PASS: account_2016:rule_01 (evidence_76)
  - PASS: audit_record_1714:rule_12 (evidence_76)

## case_287 - INCOMPLETE
- subject: `user_285`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_4485` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `legal_service/legal_hold_1745` [LEGAL_HOLD_RECORD] state=`None` evidence=`-` link=`run-fingerprint`
  - `search_service/search_5705` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - `support_platform/support_7432` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_76` link=`identity`
  - PASS: account_4485:rule_01 (evidence_75)
  - UNKNOWN: legal_hold_1745:observed (no evidence)
  - FAIL: search_5705:rule_03 (evidence_76)
  - FAIL: support_7432:rule_05 (evidence_76)

## case_288 - INCOMPLETE
- subject: `user_286`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_6988` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `export_service/export_7906` [USER_EXPORT] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - PASS: account_6988:rule_01 (evidence_75)
  - FAIL: export_7906:rule_09 (evidence_76)

## case_289 - INCOMPLETE
- subject: `user_287`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4232` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `integration_service/data_flow_743` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_76` link=`identity`
  - `search_service/search_6432` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - PASS: account_4232:rule_01 (evidence_75)
  - FAIL: data_flow_743:no-rule:recreation-path (evidence_76)
  - FAIL: search_6432:rule_03 (evidence_76)

## case_290 - INCOMPLETE
- subject: `user_288`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7177` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `integration_service/data_flow_179` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_76` link=`identity`
  - `search_service/search_3144` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - PASS: account_7177:rule_01 (evidence_75)
  - FAIL: data_flow_179:no-rule:recreation-path (evidence_76)
  - FAIL: search_3144:rule_03 (evidence_76)

## case_291 - INCOMPLETE
- subject: `user_289`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8914` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `backup_service/backup_7079` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_76` link=`identity`
  - PASS: account_8914:rule_01 (evidence_75)
  - FAIL: backup_7079:rule_14 (evidence_76)

## case_292 - COMPLETE
- subject: `user_290`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1125` [USER_PROFILE] state=`ABSENT` evidence=`evidence_76` link=`identity`
  - `analytics_platform/analytics_2322` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_76` link=`run-fingerprint`
  - `security_service/audit_record_3432` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_76` link=`identity`
  - `backup_service/backup_1825` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_76` link=`identity`
  - `integration_service/data_flow_5598` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_76` link=`identity`
  - `support_platform/support_1526` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_76` link=`identity`
  - PASS: account_1125:rule_01 (evidence_76)
  - PASS: analytics_2322:rule_07 (evidence_76)
  - PASS: audit_record_3432:rule_12 (evidence_76)
  - PASS: backup_1825:rule_14 (evidence_76)
  - PASS: data_flow_5598:no-rule:recreation-path (evidence_76)
  - PASS: support_1526:rule_05 (evidence_76)

## case_293 - INCOMPLETE
- subject: `user_291`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8353` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-ambiguous`
  - `analytics_platform/analytics_5854` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_75` link=`identity`
  - PASS: account_8353:rule_01 (evidence_75)
  - FAIL: analytics_5854:rule_07 (evidence_75)

## case_294 - COMPLETE
- subject: `user_292`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6996` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-ambiguous`
  - `analytics_platform/analytics_061` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_75` link=`run-fingerprint`
  - `security_service/audit_record_4387` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_6996:rule_01 (evidence_75)
  - PASS: analytics_061:rule_07 (evidence_75)
  - PASS: audit_record_4387:rule_12 (evidence_75)

## case_295 - COMPLETE
- subject: `user_293`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9091` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-ambiguous`
  - `analytics_platform/analytics_7575` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_75` link=`run-fingerprint`
  - `security_service/audit_record_1269` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_9091:rule_01 (evidence_75)
  - PASS: analytics_7575:rule_07 (evidence_75)
  - PASS: audit_record_1269:rule_12 (evidence_75)

## case_296 - INCOMPLETE
- subject: `user_294`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_4267` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `integration_service/data_flow_085` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_75` link=`identity`
  - `search_service/search_9631` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_4267:rule_01 (evidence_75)
  - FAIL: data_flow_085:no-rule:recreation-path (evidence_75)
  - FAIL: search_9631:rule_03 (evidence_75)

## case_297 - COMPLETE
- subject: `user_295`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6023` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `analytics_platform/analytics_7164` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_75` link=`run-fingerprint`
  - `security_service/audit_record_7878` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - `backup_service/backup_7308` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_75` link=`identity`
  - `integration_service/data_flow_3391` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_75` link=`identity`
  - `support_platform/support_1983` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_75` link=`identity`
  - PASS: account_6023:rule_01 (evidence_75)
  - PASS: analytics_7164:rule_07 (evidence_75)
  - PASS: audit_record_7878:rule_12 (evidence_75)
  - PASS: backup_7308:rule_14 (evidence_75)
  - PASS: data_flow_3391:no-rule:recreation-path (evidence_75)
  - PASS: support_1983:rule_05 (evidence_75)

## case_298 - INCOMPLETE
- subject: `user_296`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_4880` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `search_service/search_6282` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - `support_platform/support_643` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_75` link=`identity`
  - PASS: account_4880:rule_01 (evidence_75)
  - FAIL: search_6282:rule_03 (evidence_75)
  - FAIL: support_643:rule_05 (evidence_75)

## case_299 - COMPLETE
- subject: `user_297`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9993` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `security_service/audit_record_5194` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_9993:rule_01 (evidence_75)
  - PASS: audit_record_5194:rule_12 (evidence_75)

## case_300 - INCOMPLETE
- subject: `user_298`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_7249` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `export_service/export_6623` [USER_EXPORT] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - `search_service/search_4299` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_7249:rule_01 (evidence_75)
  - FAIL: export_6623:rule_09 (evidence_75)
  - FAIL: search_4299:rule_03 (evidence_75)

## case_301 - INCOMPLETE
- subject: `user_299`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1618` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-fingerprint`
  - `analytics_platform/analytics_1733` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_75` link=`run-fingerprint`
  - `integration_service/data_flow_4521` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_75` link=`identity`
  - `search_service/search_5268` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - PASS: account_1618:rule_01 (evidence_75)
  - PASS: analytics_1733:rule_07 (evidence_75)
  - FAIL: data_flow_4521:no-rule:recreation-path (evidence_75)
  - FAIL: search_5268:rule_03 (evidence_75)

## case_302 - INCOMPLETE
- subject: `user_300`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4835` [USER_PROFILE] state=`ABSENT` evidence=`evidence_75` link=`run-elimination`
  - `analytics_platform/analytics_1133` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_75` link=`identity`
  - `integration_service/data_flow_7594` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_75` link=`identity`
  - `search_service/search_1033` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_75` link=`identity`
  - `support_platform/support_2983` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_75` link=`identity`
  - PASS: account_4835:rule_01 (evidence_75)
  - FAIL: analytics_1133:rule_07 (evidence_75)
  - FAIL: data_flow_7594:no-rule:recreation-path (evidence_75)
  - FAIL: search_1033:rule_03 (evidence_75)
  - FAIL: support_2983:rule_05 (evidence_75)

## case_303 - INCOMPLETE
- subject: `user_301`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_7907` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-fingerprint`
  - `security_service/audit_record_7923` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `backup_service/backup_4935` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_29` link=`identity`
  - PASS: account_7907:rule_01 (evidence_29)
  - PASS: audit_record_7923:rule_12 (evidence_29)
  - FAIL: backup_4935:rule_14 (evidence_29)

## case_304 - COMPLETE
- subject: `user_302`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_4771` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `security_service/audit_record_4759` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - PASS: account_4771:rule_01 (evidence_29)
  - PASS: audit_record_4759:rule_12 (evidence_29)

## case_305 - INCOMPLETE
- subject: `user_303`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6680` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `analytics_platform/analytics_9285` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_29` link=`identity`
  - `security_service/audit_record_507` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_4321` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - PASS: account_6680:rule_01 (evidence_29)
  - FAIL: analytics_9285:rule_07 (evidence_29)
  - PASS: audit_record_507:rule_12 (evidence_29)
  - FAIL: search_4321:rule_03 (evidence_29)

## case_306 - INCOMPLETE
- subject: `user_304`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7248` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `security_service/audit_record_9051` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_8250` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `support_platform/support_450` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_29` link=`identity`
  - PASS: account_7248:rule_01 (evidence_29)
  - PASS: audit_record_9051:rule_12 (evidence_29)
  - FAIL: search_8250:rule_03 (evidence_29)
  - FAIL: support_450:rule_05 (evidence_29)

## case_307 - INCOMPLETE
- subject: `user_305`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_585` [USER_PROFILE] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `security_service/audit_record_5129` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_7660` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - FAIL: account_585:rule_01 (evidence_29)
  - PASS: audit_record_5129:rule_12 (evidence_29)
  - FAIL: search_7660:rule_03 (evidence_29)

## case_308 - COMPLETE
- subject: `user_306`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8647` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `analytics_platform/analytics_096` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_29` link=`run-fingerprint`
  - `security_service/audit_record_3221` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `backup_service/backup_4917` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_29` link=`identity`
  - `integration_service/data_flow_8933` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_29` link=`identity`
  - `support_platform/support_6046` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_29` link=`identity`
  - PASS: account_8647:rule_01 (evidence_29)
  - PASS: analytics_096:rule_07 (evidence_29)
  - PASS: audit_record_3221:rule_12 (evidence_29)
  - PASS: backup_4917:rule_14 (evidence_29)
  - PASS: data_flow_8933:no-rule:recreation-path (evidence_29)
  - PASS: support_6046:rule_05 (evidence_29)

## case_309 - COMPLETE
- subject: `user_307`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4319` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `analytics_platform/analytics_3678` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_29` link=`run-fingerprint`
  - `security_service/audit_record_1945` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - PASS: account_4319:rule_01 (evidence_29)
  - PASS: analytics_3678:rule_07 (evidence_29)
  - PASS: audit_record_1945:rule_12 (evidence_29)

## case_310 - INCOMPLETE
- subject: `user_308`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1235` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `security_service/audit_record_5640` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_6265` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `support_platform/support_4263` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_29` link=`identity`
  - PASS: account_1235:rule_01 (evidence_29)
  - PASS: audit_record_5640:rule_12 (evidence_29)
  - FAIL: search_6265:rule_03 (evidence_29)
  - FAIL: support_4263:rule_05 (evidence_29)

## case_311 - INCOMPLETE
- subject: `user_309`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3275` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `security_service/audit_record_6245` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_3004` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `support_platform/support_4952` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - PASS: account_3275:rule_01 (evidence_29)
  - PASS: audit_record_6245:rule_12 (evidence_29)
  - FAIL: search_3004:rule_03 (evidence_29)
  - FAIL: support_4952:rule_06 (evidence_29)

## case_312 - INCOMPLETE
- subject: `user_310`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_4718` [USER_PROFILE] state=`ABSENT` evidence=`evidence_29` link=`run-elimination`
  - `security_service/audit_record_6559` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `export_service/export_9860` [USER_EXPORT] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - `search_service/search_6805` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_29` link=`identity`
  - PASS: account_4718:rule_01 (evidence_29)
  - PASS: audit_record_6559:rule_12 (evidence_29)
  - FAIL: export_9860:rule_09 (evidence_29)
  - FAIL: search_6805:rule_03 (evidence_29)

## case_313 - COMPLETE
- subject: `user_311`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8264` [USER_PROFILE] state=`ABSENT` evidence=`evidence_74` link=`identity`
  - `analytics_platform/analytics_6099` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_74` link=`run-fingerprint`
  - `security_service/audit_record_7020` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_8264:rule_01 (evidence_74)
  - PASS: analytics_6099:rule_07 (evidence_74)
  - PASS: audit_record_7020:rule_12 (evidence_74)

## case_314 - COMPLETE
- subject: `user_312`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_591` [USER_PROFILE] state=`ABSENT` evidence=`evidence_74` link=`identity`
  - `analytics_platform/analytics_5532` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_74` link=`run-fingerprint`
  - `security_service/audit_record_7893` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_591:rule_01 (evidence_74)
  - PASS: analytics_5532:rule_07 (evidence_74)
  - PASS: audit_record_7893:rule_12 (evidence_74)

## case_315 - INCOMPLETE
- subject: `user_313`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_782` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `security_service/audit_record_2407` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_7421` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_74` link=`identity`
  - PASS: account_782:rule_01 (evidence_31)
  - UNKNOWN: audit_record_2407:observed (no evidence)
  - FAIL: backup_7421:rule_14 (evidence_74)

## case_316 - INCOMPLETE
- subject: `user_314`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_9523` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `security_service/audit_record_4286` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8583` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - `support_platform/support_1176` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_74` link=`identity`
  - PASS: account_9523:rule_01 (evidence_31)
  - UNKNOWN: audit_record_4286:observed (no evidence)
  - FAIL: search_8583:rule_03 (evidence_74)
  - FAIL: support_1176:rule_05 (evidence_74)

## case_317 - INCOMPLETE
- subject: `user_315`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_1972` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `analytics_platform/analytics_1488` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_74` link=`identity`
  - `security_service/audit_record_6170` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_3064` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_74` link=`identity`
  - `search_service/search_8665` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - `support_platform/support_4439` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_74` link=`identity`
  - PASS: account_1972:rule_01 (evidence_31)
  - FAIL: analytics_1488:rule_07 (evidence_74)
  - UNKNOWN: audit_record_6170:observed (no evidence)
  - FAIL: data_flow_3064:no-rule:recreation-path (evidence_74)
  - FAIL: search_8665:rule_03 (evidence_74)
  - FAIL: support_4439:rule_05 (evidence_74)

## case_318 - INCOMPLETE
- subject: `user_316`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_1530` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `security_service/audit_record_6708` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5472` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - `support_platform/support_7995` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_74` link=`identity`
  - PASS: account_1530:rule_01 (evidence_31)
  - UNKNOWN: audit_record_6708:observed (no evidence)
  - FAIL: search_5472:rule_03 (evidence_74)
  - FAIL: support_7995:rule_05 (evidence_74)

## case_319 - COMPLETE
- subject: `user_317`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2088` [USER_PROFILE] state=`ABSENT` evidence=`evidence_74` link=`identity`
  - `analytics_platform/analytics_2601` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_74` link=`run-fingerprint`
  - `security_service/audit_record_7337` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_2088:rule_01 (evidence_74)
  - PASS: analytics_2601:rule_07 (evidence_74)
  - PASS: audit_record_7337:rule_12 (evidence_74)

## case_320 - INCOMPLETE
- subject: `user_318`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9178` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `security_service/audit_record_1409` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_8828` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_74` link=`identity`
  - `search_service/search_2256` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_9178:rule_01 (evidence_31)
  - UNKNOWN: audit_record_1409:observed (no evidence)
  - FAIL: data_flow_8828:no-rule:recreation-path (evidence_74)
  - FAIL: search_2256:rule_03 (evidence_74)

## case_321 - INCOMPLETE
- subject: `user_319`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3525` [USER_PROFILE] state=`ABSENT` evidence=`evidence_31` link=`identity`
  - `security_service/audit_record_5151` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4964` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_74` link=`identity`
  - `search_service/search_3667` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_3525:rule_01 (evidence_31)
  - UNKNOWN: audit_record_5151:observed (no evidence)
  - FAIL: data_flow_4964:no-rule:recreation-path (evidence_74)
  - FAIL: search_3667:rule_03 (evidence_74)

## case_322 - COMPLETE
- subject: `user_320`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9354` [USER_PROFILE] state=`ABSENT` evidence=`evidence_74` link=`identity`
  - `analytics_platform/analytics_4229` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_74` link=`run-fingerprint`
  - `security_service/audit_record_3201` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_74` link=`identity`
  - PASS: account_9354:rule_01 (evidence_74)
  - PASS: analytics_4229:rule_07 (evidence_74)
  - PASS: audit_record_3201:rule_12 (evidence_74)

## case_323 - COMPLETE
- subject: `user_321`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2917` [USER_PROFILE] state=`ABSENT` evidence=`evidence_73` link=`identity`
  - `security_service/audit_record_3338` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - PASS: account_2917:rule_01 (evidence_73)
  - PASS: audit_record_3338:rule_12 (evidence_73)

## case_324 - COMPLETE
- subject: `user_322`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1242` [USER_PROFILE] state=`ABSENT` evidence=`evidence_73` link=`identity`
  - `analytics_platform/analytics_136` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_73` link=`run-fingerprint`
  - `security_service/audit_record_4466` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - `backup_service/backup_6458` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `integration_service/data_flow_4769` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `support_platform/support_7249` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_73` link=`identity`
  - PASS: account_1242:rule_01 (evidence_73)
  - PASS: analytics_136:rule_07 (evidence_73)
  - PASS: audit_record_4466:rule_12 (evidence_73)
  - PASS: backup_6458:rule_14 (evidence_73)
  - PASS: data_flow_4769:no-rule:recreation-path (evidence_73)
  - PASS: support_7249:rule_05 (evidence_73)

## case_325 - INCOMPLETE
- subject: `user_323`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_2595` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`run-elimination`
  - `security_service/audit_record_2236` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_9962` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_73` link=`identity`
  - `search_service/search_4054` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - PASS: account_2595:rule_01 (evidence_72)
  - UNKNOWN: audit_record_2236:observed (no evidence)
  - FAIL: data_flow_9962:no-rule:recreation-path (evidence_73)
  - FAIL: search_4054:rule_03 (evidence_73)

## case_326 - COMPLETE
- subject: `user_324`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_3785` [USER_PROFILE] state=`ABSENT` evidence=`evidence_73` link=`identity`
  - `analytics_platform/analytics_2072` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_73` link=`run-fingerprint`
  - `security_service/audit_record_1219` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - `backup_service/backup_2894` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `integration_service/data_flow_2468` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `support_platform/support_305` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_73` link=`identity`
  - PASS: account_3785:rule_01 (evidence_73)
  - PASS: analytics_2072:rule_07 (evidence_73)
  - PASS: audit_record_1219:rule_12 (evidence_73)
  - PASS: backup_2894:rule_14 (evidence_73)
  - PASS: data_flow_2468:no-rule:recreation-path (evidence_73)
  - PASS: support_305:rule_05 (evidence_73)

## case_327 - COMPLETE
- subject: `user_325`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4606` [USER_PROFILE] state=`ABSENT` evidence=`evidence_73` link=`identity`
  - `analytics_platform/analytics_9681` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_73` link=`run-fingerprint`
  - `security_service/audit_record_461` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - PASS: account_4606:rule_01 (evidence_73)
  - PASS: analytics_9681:rule_07 (evidence_73)
  - PASS: audit_record_461:rule_12 (evidence_73)

## case_328 - INCOMPLETE
- subject: `user_326`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_206` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`run-elimination`
  - `security_service/audit_record_5012` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9107` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - `support_platform/support_7926` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_73` link=`identity`
  - PASS: account_206:rule_01 (evidence_72)
  - UNKNOWN: audit_record_5012:observed (no evidence)
  - FAIL: search_9107:rule_03 (evidence_73)
  - FAIL: support_7926:rule_05 (evidence_73)

## case_329 - INCOMPLETE
- subject: `user_327`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6301` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`run-elimination`
  - `analytics_platform/analytics_671` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_73` link=`identity`
  - `security_service/audit_record_3525` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5226` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - PASS: account_6301:rule_01 (evidence_72)
  - FAIL: analytics_671:rule_07 (evidence_73)
  - UNKNOWN: audit_record_3525:observed (no evidence)
  - FAIL: search_5226:rule_03 (evidence_73)

## case_330 - INCOMPLETE
- subject: `user_328`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2583` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`run-elimination`
  - `security_service/audit_record_6629` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_4560` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - `support_platform/support_4851` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_73` link=`identity`
  - PASS: account_2583:rule_01 (evidence_72)
  - UNKNOWN: audit_record_6629:observed (no evidence)
  - FAIL: search_4560:rule_03 (evidence_73)
  - FAIL: support_4851:rule_05 (evidence_73)

## case_331 - COMPLETE
- subject: `user_329`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6814` [USER_PROFILE] state=`ABSENT` evidence=`evidence_73` link=`identity`
  - `analytics_platform/analytics_2022` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_73` link=`run-fingerprint`
  - `security_service/audit_record_6731` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - `backup_service/backup_9376` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `integration_service/data_flow_8534` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_73` link=`identity`
  - `support_platform/support_1403` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_73` link=`identity`
  - PASS: account_6814:rule_01 (evidence_73)
  - PASS: analytics_2022:rule_07 (evidence_73)
  - PASS: audit_record_6731:rule_12 (evidence_73)
  - PASS: backup_9376:rule_14 (evidence_73)
  - PASS: data_flow_8534:no-rule:recreation-path (evidence_73)
  - PASS: support_1403:rule_05 (evidence_73)

## case_332 - INCOMPLETE
- subject: `user_330`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5992` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`run-elimination`
  - `security_service/audit_record_8914` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_4392` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_73` link=`identity`
  - `search_service/search_049` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_73` link=`identity`
  - PASS: account_5992:rule_01 (evidence_72)
  - UNKNOWN: audit_record_8914:observed (no evidence)
  - FAIL: data_flow_4392:no-rule:recreation-path (evidence_73)
  - FAIL: search_049:rule_03 (evidence_73)

## case_333 - INCOMPLETE
- subject: `user_331`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_2475` [USER_PROFILE] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_4647` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_5970` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - FAIL: account_2475:rule_01 (evidence_72)
  - UNKNOWN: audit_record_4647:observed (no evidence)
  - FAIL: search_5970:rule_03 (evidence_72)

## case_334 - INCOMPLETE
- subject: `user_332`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_2255` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_8558` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_7348` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - `support_platform/support_214` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_72` link=`identity`
  - PASS: account_2255:rule_01 (evidence_72)
  - UNKNOWN: audit_record_8558:observed (no evidence)
  - FAIL: search_7348:rule_03 (evidence_72)
  - FAIL: support_214:rule_05 (evidence_72)

## case_335 - COMPLETE
- subject: `user_333`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8892` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `analytics_platform/analytics_3108` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_72` link=`run-fingerprint`
  - `security_service/audit_record_711` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - `backup_service/backup_3136` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_72` link=`identity`
  - `integration_service/data_flow_7452` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_72` link=`identity`
  - `support_platform/support_4712` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_72` link=`identity`
  - PASS: account_8892:rule_01 (evidence_72)
  - PASS: analytics_3108:rule_07 (evidence_72)
  - PASS: audit_record_711:rule_12 (evidence_72)
  - PASS: backup_3136:rule_14 (evidence_72)
  - PASS: data_flow_7452:no-rule:recreation-path (evidence_72)
  - PASS: support_4712:rule_05 (evidence_72)

## case_336 - COMPLETE
- subject: `user_334`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2282` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_5022` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_2282:rule_01 (evidence_72)
  - PASS: audit_record_5022:rule_12 (evidence_72)

## case_337 - INCOMPLETE
- subject: `user_335`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_767` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_1961` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_5200` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_72` link=`identity`
  - `search_service/search_3773` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_767:rule_01 (evidence_72)
  - UNKNOWN: audit_record_1961:observed (no evidence)
  - FAIL: data_flow_5200:no-rule:recreation-path (evidence_72)
  - FAIL: search_3773:rule_03 (evidence_72)

## case_338 - INCOMPLETE
- subject: `user_336`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4231` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_9226` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_9392` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_72` link=`identity`
  - `search_service/search_1392` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_4231:rule_01 (evidence_72)
  - UNKNOWN: audit_record_9226:observed (no evidence)
  - FAIL: data_flow_9392:no-rule:recreation-path (evidence_72)
  - FAIL: search_1392:rule_03 (evidence_72)

## case_339 - COMPLETE
- subject: `user_337`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_1340` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `analytics_platform/analytics_2079` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_72` link=`run-fingerprint`
  - `security_service/audit_record_2922` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_1340:rule_01 (evidence_72)
  - PASS: analytics_2079:rule_07 (evidence_72)
  - PASS: audit_record_2922:rule_12 (evidence_72)

## case_340 - INCOMPLETE
- subject: `user_338`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1015` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_3872` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_5916` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_72` link=`identity`
  - `search_service/search_5411` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_1015:rule_01 (evidence_72)
  - UNKNOWN: audit_record_3872:observed (no evidence)
  - FAIL: data_flow_5916:no-rule:recreation-path (evidence_72)
  - FAIL: search_5411:rule_03 (evidence_72)

## case_341 - INCOMPLETE
- subject: `user_339`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4377` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `analytics_platform/analytics_183` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_2862` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_7367` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_72` link=`identity`
  - PASS: account_4377:rule_01 (evidence_72)
  - FAIL: analytics_183:rule_07 (evidence_72)
  - UNKNOWN: audit_record_2862:observed (no evidence)
  - FAIL: search_7367:rule_03 (evidence_72)

## case_342 - INCOMPLETE
- subject: `user_340`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_614` [USER_PROFILE] state=`ABSENT` evidence=`evidence_72` link=`identity`
  - `security_service/audit_record_4058` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_3399` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_72` link=`identity`
  - PASS: account_614:rule_01 (evidence_72)
  - UNKNOWN: audit_record_4058:observed (no evidence)
  - FAIL: support_3399:rule_05 (evidence_72)

## case_343 - COMPLETE
- subject: `user_341`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1949` [USER_PROFILE] state=`ABSENT` evidence=`evidence_71` link=`run-elimination`
  - `analytics_platform/analytics_4751` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_71` link=`run-fingerprint`
  - `security_service/audit_record_9233` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - PASS: account_1949:rule_01 (evidence_71)
  - PASS: analytics_4751:rule_07 (evidence_71)
  - PASS: audit_record_9233:rule_12 (evidence_71)

## case_344 - INCOMPLETE
- subject: `user_342`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_486` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `integration_service/data_flow_5544` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_71` link=`identity`
  - `search_service/search_5267` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - PASS: account_486:rule_01 (evidence_33)
  - FAIL: data_flow_5544:no-rule:recreation-path (evidence_71)
  - FAIL: search_5267:rule_03 (evidence_71)

## case_345 - COMPLETE
- subject: `user_343`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_5214` [USER_PROFILE] state=`ABSENT` evidence=`evidence_71` link=`run-ambiguous`
  - `analytics_platform/analytics_7102` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_71` link=`run-fingerprint`
  - `security_service/audit_record_454` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - PASS: account_5214:rule_01 (evidence_71)
  - PASS: analytics_7102:rule_07 (evidence_71)
  - PASS: audit_record_454:rule_12 (evidence_71)

## case_346 - COMPLETE
- subject: `user_344`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8834` [USER_PROFILE] state=`ABSENT` evidence=`evidence_71` link=`run-ambiguous`
  - `analytics_platform/analytics_3990` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_71` link=`run-fingerprint`
  - `security_service/audit_record_1700` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - PASS: account_8834:rule_01 (evidence_71)
  - PASS: analytics_3990:rule_07 (evidence_71)
  - PASS: audit_record_1700:rule_12 (evidence_71)

## case_347 - INCOMPLETE
- subject: `user_345`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3372` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-fingerprint`
  - `search_service/search_8185` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - `support_platform/support_9474` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_71` link=`identity`
  - PASS: account_3372:rule_01 (evidence_33)
  - FAIL: search_8185:rule_03 (evidence_71)
  - FAIL: support_9474:rule_05 (evidence_71)

## case_348 - INCOMPLETE
- subject: `user_346`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_421` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `analytics_platform/analytics_9196` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_71` link=`identity`
  - `export_service/export_4871` [USER_EXPORT] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - `search_service/search_6170` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - `support_platform/support_2897` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_71` link=`identity`
  - PASS: account_421:rule_01 (evidence_33)
  - FAIL: analytics_9196:rule_07 (evidence_71)
  - FAIL: export_4871:rule_09 (evidence_71)
  - FAIL: search_6170:rule_03 (evidence_71)
  - FAIL: support_2897:rule_05 (evidence_71)

## case_349 - INCOMPLETE
- subject: `user_347`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9881` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-fingerprint`
  - `integration_service/data_flow_3178` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_71` link=`identity`
  - `search_service/search_3944` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - PASS: account_9881:rule_01 (evidence_33)
  - FAIL: data_flow_3178:no-rule:recreation-path (evidence_71)
  - FAIL: search_3944:rule_03 (evidence_71)

## case_350 - INCOMPLETE
- subject: `user_348`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5202` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `integration_service/data_flow_9775` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_71` link=`identity`
  - PASS: account_5202:rule_01 (evidence_33)
  - FAIL: data_flow_9775:no-rule:recreation-path (evidence_71)

## case_351 - COMPLETE
- subject: `user_349`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_5059` [USER_PROFILE] state=`ABSENT` evidence=`evidence_71` link=`run-elimination`
  - `analytics_platform/analytics_1072` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_71` link=`run-fingerprint`
  - `security_service/audit_record_8787` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - `backup_service/backup_024` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_71` link=`identity`
  - `integration_service/data_flow_4323` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_71` link=`identity`
  - `support_platform/support_7137` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_71` link=`identity`
  - PASS: account_5059:rule_01 (evidence_71)
  - PASS: analytics_1072:rule_07 (evidence_71)
  - PASS: audit_record_8787:rule_12 (evidence_71)
  - PASS: backup_024:rule_14 (evidence_71)
  - PASS: data_flow_4323:no-rule:recreation-path (evidence_71)
  - PASS: support_7137:rule_05 (evidence_71)

## case_352 - INCOMPLETE
- subject: `user_350`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6215` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `search_service/search_5685` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_71` link=`identity`
  - `support_platform/support_3980` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_71` link=`identity`
  - PASS: account_6215:rule_01 (evidence_33)
  - FAIL: search_5685:rule_03 (evidence_71)
  - FAIL: support_3980:rule_05 (evidence_71)

## case_353 - INCOMPLETE
- subject: `user_351`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9056` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `analytics_platform/analytics_8011` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_33` link=`identity`
  - `security_service/audit_record_5773` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `integration_service/data_flow_3180` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_33` link=`identity`
  - `search_service/search_495` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `support_platform/support_2406` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_33` link=`identity`
  - PASS: account_9056:rule_01 (evidence_33)
  - FAIL: analytics_8011:rule_07 (evidence_33)
  - PASS: audit_record_5773:rule_12 (evidence_33)
  - FAIL: data_flow_3180:no-rule:recreation-path (evidence_33)
  - FAIL: search_495:rule_03 (evidence_33)
  - FAIL: support_2406:rule_05 (evidence_33)

## case_354 - COMPLETE
- subject: `user_352`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3918` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `analytics_platform/analytics_439` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_33` link=`run-fingerprint`
  - `security_service/audit_record_9286` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - PASS: account_3918:rule_01 (evidence_33)
  - PASS: analytics_439:rule_07 (evidence_33)
  - PASS: audit_record_9286:rule_12 (evidence_33)

## case_355 - INCOMPLETE
- subject: `user_353`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6539` [USER_PROFILE] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `security_service/audit_record_1151` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - FAIL: account_6539:rule_01 (evidence_33)
  - PASS: audit_record_1151:rule_12 (evidence_33)

## case_356 - INCOMPLETE
- subject: `user_354`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6093` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `analytics_platform/analytics_5413` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_33` link=`identity`
  - `security_service/audit_record_771` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `integration_service/data_flow_4472` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_33` link=`identity`
  - `search_service/search_5025` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `support_platform/support_6224` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_33` link=`identity`
  - PASS: account_6093:rule_01 (evidence_33)
  - FAIL: analytics_5413:rule_07 (evidence_33)
  - PASS: audit_record_771:rule_12 (evidence_33)
  - FAIL: data_flow_4472:no-rule:recreation-path (evidence_33)
  - FAIL: search_5025:rule_03 (evidence_33)
  - FAIL: support_6224:rule_05 (evidence_33)

## case_357 - INCOMPLETE
- subject: `user_355`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_8105` [USER_PROFILE] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `security_service/audit_record_350` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `search_service/search_6828` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - FAIL: account_8105:rule_01 (evidence_33)
  - PASS: audit_record_350:rule_12 (evidence_33)
  - FAIL: search_6828:rule_03 (evidence_33)

## case_358 - INCOMPLETE
- subject: `user_356`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1850` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `security_service/audit_record_1395` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `search_service/search_4067` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `support_platform/support_1846` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_33` link=`identity`
  - PASS: account_1850:rule_01 (evidence_33)
  - PASS: audit_record_1395:rule_12 (evidence_33)
  - FAIL: search_4067:rule_03 (evidence_33)
  - FAIL: support_1846:rule_05 (evidence_33)

## case_359 - INCOMPLETE
- subject: `user_357`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6445` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-fingerprint`
  - `security_service/audit_record_2641` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `search_service/search_2492` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `support_platform/support_2537` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - PASS: account_6445:rule_01 (evidence_33)
  - PASS: audit_record_2641:rule_12 (evidence_33)
  - FAIL: search_2492:rule_03 (evidence_33)
  - FAIL: support_2537:rule_06 (evidence_33)

## case_360 - INCOMPLETE
- subject: `user_358`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6312` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `security_service/audit_record_2605` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `export_service/export_350` [USER_EXPORT] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `search_service/search_957` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - PASS: account_6312:rule_01 (evidence_33)
  - PASS: audit_record_2605:rule_12 (evidence_33)
  - FAIL: export_350:rule_09 (evidence_33)
  - FAIL: search_957:rule_03 (evidence_33)

## case_361 - INCOMPLETE
- subject: `user_359`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7118` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-fingerprint`
  - `security_service/audit_record_7587` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - `integration_service/data_flow_3052` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_33` link=`identity`
  - `search_service/search_496` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - PASS: account_7118:rule_01 (evidence_33)
  - PASS: audit_record_7587:rule_12 (evidence_33)
  - FAIL: data_flow_3052:no-rule:recreation-path (evidence_33)
  - FAIL: search_496:rule_03 (evidence_33)

## case_362 - COMPLETE
- subject: `user_360`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_507` [USER_PROFILE] state=`ABSENT` evidence=`evidence_33` link=`run-elimination`
  - `analytics_platform/analytics_4273` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_33` link=`run-fingerprint`
  - `security_service/audit_record_8638` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_33` link=`identity`
  - PASS: account_507:rule_01 (evidence_33)
  - PASS: analytics_4273:rule_07 (evidence_33)
  - PASS: audit_record_8638:rule_12 (evidence_33)

## case_363 - INCOMPLETE
- subject: `user_361`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9205` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_9777` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `backup_service/backup_7253` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_34` link=`identity`
  - PASS: account_9205:rule_01 (evidence_34)
  - PASS: audit_record_9777:rule_12 (evidence_34)
  - FAIL: backup_7253:rule_14 (evidence_34)

## case_364 - INCOMPLETE
- subject: `user_362`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7653` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_7136` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `search_service/search_8198` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_9699` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - PASS: account_7653:rule_01 (evidence_34)
  - PASS: audit_record_7136:rule_12 (evidence_34)
  - FAIL: search_8198:rule_03 (evidence_34)
  - FAIL: support_9699:rule_05 (evidence_34)

## case_365 - INCOMPLETE
- subject: `user_363`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3016` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `analytics_platform/analytics_547` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_5798` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `integration_service/data_flow_1021` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_34` link=`identity`
  - `search_service/search_6311` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_3294` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - PASS: account_3016:rule_01 (evidence_34)
  - FAIL: analytics_547:rule_07 (evidence_34)
  - PASS: audit_record_5798:rule_12 (evidence_34)
  - FAIL: data_flow_1021:no-rule:recreation-path (evidence_34)
  - FAIL: search_6311:rule_03 (evidence_34)
  - FAIL: support_3294:rule_05 (evidence_34)

## case_366 - INCOMPLETE
- subject: `user_364`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4788` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `analytics_platform/analytics_8593` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_4655` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `integration_service/data_flow_8256` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_34` link=`identity`
  - `search_service/search_5301` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_5609` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - PASS: account_4788:rule_01 (evidence_34)
  - FAIL: analytics_8593:rule_07 (evidence_34)
  - PASS: audit_record_4655:rule_12 (evidence_34)
  - FAIL: data_flow_8256:no-rule:recreation-path (evidence_34)
  - FAIL: search_5301:rule_03 (evidence_34)
  - FAIL: support_5609:rule_05 (evidence_34)

## case_367 - INCOMPLETE
- subject: `user_365`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3204` [USER_PROFILE] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `analytics_platform/analytics_946` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_9082` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `search_service/search_9950` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_4691` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - FAIL: account_3204:rule_01 (evidence_34)
  - FAIL: analytics_946:rule_07 (evidence_34)
  - PASS: audit_record_9082:rule_12 (evidence_34)
  - FAIL: search_9950:rule_03 (evidence_34)
  - FAIL: support_4691:rule_05 (evidence_34)

## case_368 - INCOMPLETE
- subject: `user_366`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9570` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_3738` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `integration_service/data_flow_8293` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_34` link=`identity`
  - `search_service/search_4359` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - PASS: account_9570:rule_01 (evidence_34)
  - PASS: audit_record_3738:rule_12 (evidence_34)
  - FAIL: data_flow_8293:no-rule:recreation-path (evidence_34)
  - FAIL: search_4359:rule_03 (evidence_34)

## case_369 - COMPLETE
- subject: `user_367`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8590` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `analytics_platform/analytics_2807` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_34` link=`run-fingerprint`
  - `security_service/audit_record_337` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - PASS: account_8590:rule_01 (evidence_34)
  - PASS: analytics_2807:rule_07 (evidence_34)
  - PASS: audit_record_337:rule_12 (evidence_34)

## case_370 - INCOMPLETE
- subject: `user_368`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6567` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `analytics_platform/analytics_7215` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_9696` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `integration_service/data_flow_5608` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_34` link=`identity`
  - `search_service/search_9365` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_6949` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_34` link=`identity`
  - PASS: account_6567:rule_01 (evidence_34)
  - FAIL: analytics_7215:rule_07 (evidence_34)
  - PASS: audit_record_9696:rule_12 (evidence_34)
  - FAIL: data_flow_5608:no-rule:recreation-path (evidence_34)
  - FAIL: search_9365:rule_03 (evidence_34)
  - FAIL: support_6949:rule_05 (evidence_34)

## case_371 - INCOMPLETE
- subject: `user_369`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5896` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_689` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `search_service/search_6847` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `support_platform/support_3110` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - PASS: account_5896:rule_01 (evidence_34)
  - PASS: audit_record_689:rule_12 (evidence_34)
  - FAIL: search_6847:rule_03 (evidence_34)
  - FAIL: support_3110:rule_06 (evidence_34)

## case_372 - INCOMPLETE
- subject: `user_370`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2062` [USER_PROFILE] state=`ABSENT` evidence=`evidence_34` link=`identity`
  - `security_service/audit_record_5705` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - `export_service/export_5081` [USER_EXPORT] state=`PRESENT` evidence=`evidence_34` link=`identity`
  - PASS: account_2062:rule_01 (evidence_34)
  - PASS: audit_record_5705:rule_12 (evidence_34)
  - FAIL: export_5081:rule_09 (evidence_34)

## case_373 - INCOMPLETE
- subject: `user_371`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8684` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `security_service/audit_record_9163` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_2984` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_70` link=`identity`
  - `search_service/search_7859` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - PASS: account_8684:rule_01 (evidence_69)
  - UNKNOWN: audit_record_9163:observed (no evidence)
  - FAIL: data_flow_2984:no-rule:recreation-path (evidence_70)
  - FAIL: search_7859:rule_03 (evidence_70)

## case_374 - COMPLETE
- subject: `user_372`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8598` [USER_PROFILE] state=`ABSENT` evidence=`evidence_70` link=`identity`
  - `analytics_platform/analytics_9394` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_70` link=`run-fingerprint`
  - `security_service/audit_record_5137` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - PASS: account_8598:rule_01 (evidence_70)
  - PASS: analytics_9394:rule_07 (evidence_70)
  - PASS: audit_record_5137:rule_12 (evidence_70)

## case_375 - COMPLETE
- subject: `user_373`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2854` [USER_PROFILE] state=`ABSENT` evidence=`evidence_70` link=`identity`
  - `analytics_platform/analytics_5779` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_70` link=`run-fingerprint`
  - `security_service/audit_record_6359` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - PASS: account_2854:rule_01 (evidence_70)
  - PASS: analytics_5779:rule_07 (evidence_70)
  - PASS: audit_record_6359:rule_12 (evidence_70)

## case_376 - INCOMPLETE
- subject: `user_374`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5454` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `security_service/audit_record_4137` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_3126` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - `support_platform/support_475` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_70` link=`identity`
  - PASS: account_5454:rule_01 (evidence_69)
  - UNKNOWN: audit_record_4137:observed (no evidence)
  - FAIL: search_3126:rule_03 (evidence_70)
  - FAIL: support_475:rule_05 (evidence_70)

## case_377 - INCOMPLETE
- subject: `user_375`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1824` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `analytics_platform/analytics_3651` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_70` link=`identity`
  - `security_service/audit_record_3685` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - PASS: account_1824:rule_01 (evidence_69)
  - FAIL: analytics_3651:rule_07 (evidence_70)
  - UNKNOWN: audit_record_3685:observed (no evidence)

## case_378 - COMPLETE
- subject: `user_376`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_976` [USER_PROFILE] state=`ABSENT` evidence=`evidence_70` link=`identity`
  - `analytics_platform/analytics_3234` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_70` link=`run-fingerprint`
  - `security_service/audit_record_7312` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - PASS: account_976:rule_01 (evidence_70)
  - PASS: analytics_3234:rule_07 (evidence_70)
  - PASS: audit_record_7312:rule_12 (evidence_70)

## case_379 - INCOMPLETE
- subject: `user_377`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6246` [USER_PROFILE] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - `security_service/audit_record_8830` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9124` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - FAIL: account_6246:rule_01 (evidence_70)
  - UNKNOWN: audit_record_8830:observed (no evidence)
  - FAIL: search_9124:rule_03 (evidence_70)

## case_380 - COMPLETE
- subject: `user_378`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4001` [USER_PROFILE] state=`ABSENT` evidence=`evidence_70` link=`identity`
  - `analytics_platform/analytics_9326` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_70` link=`run-fingerprint`
  - `security_service/audit_record_4489` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - PASS: account_4001:rule_01 (evidence_70)
  - PASS: analytics_9326:rule_07 (evidence_70)
  - PASS: audit_record_4489:rule_12 (evidence_70)

## case_381 - INCOMPLETE
- subject: `user_379`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_6784` [USER_PROFILE] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - `security_service/audit_record_6833` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - FAIL: account_6784:rule_01 (evidence_70)
  - UNKNOWN: audit_record_6833:observed (no evidence)

## case_382 - INCOMPLETE
- subject: `user_380`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2041` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `analytics_platform/analytics_9918` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_70` link=`identity`
  - `security_service/audit_record_6238` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_6090` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_70` link=`identity`
  - `search_service/search_8171` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_70` link=`identity`
  - `support_platform/support_5071` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_70` link=`identity`
  - PASS: account_2041:rule_01 (evidence_69)
  - FAIL: analytics_9918:rule_07 (evidence_70)
  - UNKNOWN: audit_record_6238:observed (no evidence)
  - FAIL: data_flow_6090:no-rule:recreation-path (evidence_70)
  - FAIL: search_8171:rule_03 (evidence_70)
  - FAIL: support_5071:rule_05 (evidence_70)

## case_383 - COMPLETE
- subject: `user_381`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_5043` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `analytics_platform/analytics_9702` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_36` link=`run-fingerprint`
  - `security_service/audit_record_989` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - PASS: account_5043:rule_01 (evidence_36)
  - PASS: analytics_9702:rule_07 (evidence_36)
  - PASS: audit_record_989:rule_12 (evidence_36)

## case_384 - INCOMPLETE
- subject: `user_382`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4441` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_2342` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `export_service/export_9989` [USER_EXPORT] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `search_service/search_7562` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - PASS: account_4441:rule_01 (evidence_36)
  - PASS: audit_record_2342:rule_12 (evidence_36)
  - FAIL: export_9989:rule_09 (evidence_36)
  - FAIL: search_7562:rule_03 (evidence_36)

## case_385 - INCOMPLETE
- subject: `user_383`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_4844` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_3007` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `integration_service/data_flow_3913` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_36` link=`identity`
  - `search_service/search_3355` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - PASS: account_4844:rule_01 (evidence_36)
  - PASS: audit_record_3007:rule_12 (evidence_36)
  - FAIL: data_flow_3913:no-rule:recreation-path (evidence_36)
  - FAIL: search_3355:rule_03 (evidence_36)

## case_386 - INCOMPLETE
- subject: `user_384`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_807` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `analytics_platform/analytics_4420` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_8245` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `integration_service/data_flow_7623` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_36` link=`identity`
  - `search_service/search_3630` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `support_platform/support_1693` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_36` link=`identity`
  - PASS: account_807:rule_01 (evidence_36)
  - FAIL: analytics_4420:rule_07 (evidence_36)
  - PASS: audit_record_8245:rule_12 (evidence_36)
  - FAIL: data_flow_7623:no-rule:recreation-path (evidence_36)
  - FAIL: search_3630:rule_03 (evidence_36)
  - FAIL: support_1693:rule_05 (evidence_36)

## case_387 - INCOMPLETE
- subject: `user_385`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3978` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_2536` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `backup_service/backup_1668` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_36` link=`identity`
  - PASS: account_3978:rule_01 (evidence_36)
  - PASS: audit_record_2536:rule_12 (evidence_36)
  - FAIL: backup_1668:rule_14 (evidence_36)

## case_388 - INCOMPLETE
- subject: `user_386`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_8186` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `analytics_platform/analytics_2784` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_8683` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `integration_service/data_flow_3250` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_36` link=`identity`
  - `search_service/search_182` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `support_platform/support_8378` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_36` link=`identity`
  - PASS: account_8186:rule_01 (evidence_36)
  - FAIL: analytics_2784:rule_07 (evidence_36)
  - PASS: audit_record_8683:rule_12 (evidence_36)
  - FAIL: data_flow_3250:no-rule:recreation-path (evidence_36)
  - FAIL: search_182:rule_03 (evidence_36)
  - FAIL: support_8378:rule_05 (evidence_36)

## case_389 - INCOMPLETE
- subject: `user_387`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3206` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `analytics_platform/analytics_5354` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_9005` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `search_service/search_2794` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - PASS: account_3206:rule_01 (evidence_36)
  - FAIL: analytics_5354:rule_07 (evidence_36)
  - PASS: audit_record_9005:rule_12 (evidence_36)
  - FAIL: search_2794:rule_03 (evidence_36)

## case_390 - COMPLETE
- subject: `user_388`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_7618` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_101` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `backup_service/backup_5165` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_36` link=`identity`
  - `integration_service/data_flow_5737` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_36` link=`identity`
  - `legal_service/legal_hold_8049` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `support_platform/support_5720` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_36` link=`identity`
  - PASS: account_7618:rule_01 (evidence_36)
  - PASS: audit_record_101:rule_12 (evidence_36)
  - PASS: backup_5165:rule_14 (evidence_36)
  - PASS: data_flow_5737:no-rule:recreation-path (evidence_36)
  - PASS: legal_hold_8049:rule_13 (evidence_36)
  - PASS: support_5720:rule_05 (evidence_36)

## case_391 - INCOMPLETE
- subject: `user_389`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4446` [USER_PROFILE] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `security_service/audit_record_5007` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - `search_service/search_9470` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - FAIL: account_4446:rule_01 (evidence_36)
  - PASS: audit_record_5007:rule_12 (evidence_36)
  - FAIL: search_9470:rule_03 (evidence_36)

## case_392 - COMPLETE
- subject: `user_390`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1718` [USER_PROFILE] state=`ABSENT` evidence=`evidence_36` link=`identity`
  - `analytics_platform/analytics_4328` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_36` link=`run-fingerprint`
  - `security_service/audit_record_7510` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_36` link=`identity`
  - PASS: account_1718:rule_01 (evidence_36)
  - PASS: analytics_4328:rule_07 (evidence_36)
  - PASS: audit_record_7510:rule_12 (evidence_36)

## case_393 - COMPLETE
- subject: `user_391`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1093` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `security_service/audit_record_7330` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_1093:rule_01 (evidence_69)
  - PASS: audit_record_7330:rule_12 (evidence_69)

## case_394 - INCOMPLETE
- subject: `user_392`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2191` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `search_service/search_195` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_2191:rule_01 (evidence_69)
  - FAIL: search_195:rule_03 (evidence_69)

## case_395 - COMPLETE
- subject: `user_393`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2464` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `security_service/audit_record_2839` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_2464:rule_01 (evidence_69)
  - PASS: audit_record_2839:rule_12 (evidence_69)

## case_396 - INCOMPLETE
- subject: `user_394`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_3492` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-fingerprint`
  - `export_service/export_4664` [USER_EXPORT] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - `search_service/search_7293` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_3492:rule_01 (evidence_69)
  - FAIL: export_4664:rule_09 (evidence_69)
  - FAIL: search_7293:rule_03 (evidence_69)

## case_397 - INCOMPLETE
- subject: `user_395`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6443` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-fingerprint`
  - `analytics_platform/analytics_4651` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_69` link=`run-fingerprint`
  - `integration_service/data_flow_626` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_69` link=`identity`
  - `search_service/search_3232` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_6443:rule_01 (evidence_69)
  - PASS: analytics_4651:rule_07 (evidence_69)
  - FAIL: data_flow_626:no-rule:recreation-path (evidence_69)
  - FAIL: search_3232:rule_03 (evidence_69)

## case_398 - COMPLETE
- subject: `user_396`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1140` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `analytics_platform/analytics_4455` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_69` link=`run-fingerprint`
  - `security_service/audit_record_7361` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - PASS: account_1140:rule_01 (evidence_69)
  - PASS: analytics_4455:rule_07 (evidence_69)
  - PASS: audit_record_7361:rule_12 (evidence_69)

## case_399 - INCOMPLETE
- subject: `user_397`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2138` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-fingerprint`
  - `backup_service/backup_2642` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_69` link=`identity`
  - PASS: account_2138:rule_01 (evidence_69)
  - FAIL: backup_2642:rule_14 (evidence_69)

## case_400 - INCOMPLETE
- subject: `user_398`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_928` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `search_service/search_4649` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - `support_platform/support_4521` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_69` link=`identity`
  - PASS: account_928:rule_01 (evidence_69)
  - FAIL: search_4649:rule_03 (evidence_69)
  - FAIL: support_4521:rule_05 (evidence_69)

## case_401 - INCOMPLETE
- subject: `user_399`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9820` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `analytics_platform/analytics_6872` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_69` link=`identity`
  - PASS: account_9820:rule_01 (evidence_69)
  - FAIL: analytics_6872:rule_07 (evidence_69)

## case_402 - INCOMPLETE
- subject: `user_400`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3370` [USER_PROFILE] state=`ABSENT` evidence=`evidence_69` link=`run-elimination`
  - `analytics_platform/analytics_5811` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_69` link=`identity`
  - `integration_service/data_flow_9411` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_69` link=`identity`
  - `search_service/search_1338` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_69` link=`identity`
  - `support_platform/support_4290` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_69` link=`identity`
  - PASS: account_3370:rule_01 (evidence_69)
  - FAIL: analytics_5811:rule_07 (evidence_69)
  - FAIL: data_flow_9411:no-rule:recreation-path (evidence_69)
  - FAIL: search_1338:rule_03 (evidence_69)
  - FAIL: support_4290:rule_05 (evidence_69)

## case_403 - COMPLETE
- subject: `user_401`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1246` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-elimination`
  - `analytics_platform/analytics_7090` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_38` link=`run-fingerprint`
  - `security_service/audit_record_4733` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_1246:rule_01 (evidence_38)
  - PASS: analytics_7090:rule_07 (evidence_38)
  - PASS: audit_record_4733:rule_12 (evidence_38)

## case_404 - INCOMPLETE
- subject: `user_402`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1759` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-fingerprint`
  - `analytics_platform/analytics_1792` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_38` link=`identity`
  - `security_service/audit_record_6099` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `integration_service/data_flow_8093` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_38` link=`identity`
  - `search_service/search_7022` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `support_platform/support_880` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_38` link=`identity`
  - PASS: account_1759:rule_01 (evidence_38)
  - FAIL: analytics_1792:rule_07 (evidence_38)
  - PASS: audit_record_6099:rule_12 (evidence_38)
  - FAIL: data_flow_8093:no-rule:recreation-path (evidence_38)
  - FAIL: search_7022:rule_03 (evidence_38)
  - FAIL: support_880:rule_05 (evidence_38)

## case_405 - INCOMPLETE
- subject: `user_403`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_5389` [USER_PROFILE] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `security_service/audit_record_4522` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `search_service/search_1606` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - FAIL: account_5389:rule_01 (evidence_38)
  - PASS: audit_record_4522:rule_12 (evidence_38)
  - FAIL: search_1606:rule_03 (evidence_38)

## case_406 - INCOMPLETE
- subject: `user_404`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8997` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-elimination`
  - `security_service/audit_record_5455` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `search_service/search_2804` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `support_platform/support_6047` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_38` link=`identity`
  - PASS: account_8997:rule_01 (evidence_38)
  - PASS: audit_record_5455:rule_12 (evidence_38)
  - FAIL: search_2804:rule_03 (evidence_38)
  - FAIL: support_6047:rule_05 (evidence_38)

## case_407 - INCOMPLETE
- subject: `user_405`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9087` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-elimination`
  - `analytics_platform/analytics_1922` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_38` link=`identity`
  - `security_service/audit_record_6152` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `search_service/search_5146` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `support_platform/support_3802` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `support_platform/support_6569` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_38` link=`identity`
  - PASS: account_9087:rule_01 (evidence_38)
  - FAIL: analytics_1922:rule_07 (evidence_38)
  - PASS: audit_record_6152:rule_12 (evidence_38)
  - FAIL: search_5146:rule_03 (evidence_38)
  - FAIL: support_3802:rule_06 (evidence_38)
  - FAIL: support_6569:rule_05 (evidence_38)

## case_408 - COMPLETE
- subject: `user_406`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7174` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-ambiguous`
  - `analytics_platform/analytics_542` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_38` link=`run-fingerprint`
  - `security_service/audit_record_4216` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_7174:rule_01 (evidence_38)
  - PASS: analytics_542:rule_07 (evidence_38)
  - PASS: audit_record_4216:rule_12 (evidence_38)

## case_409 - COMPLETE
- subject: `user_407`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5754` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-ambiguous`
  - `analytics_platform/analytics_8973` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_38` link=`run-fingerprint`
  - `security_service/audit_record_2559` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_5754:rule_01 (evidence_38)
  - PASS: analytics_8973:rule_07 (evidence_38)
  - PASS: audit_record_2559:rule_12 (evidence_38)

## case_410 - INCOMPLETE
- subject: `user_408`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_163` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-fingerprint`
  - `security_service/audit_record_896` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - `integration_service/data_flow_8300` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_38` link=`identity`
  - `search_service/search_9987` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_163:rule_01 (evidence_38)
  - PASS: audit_record_896:rule_12 (evidence_38)
  - FAIL: data_flow_8300:no-rule:recreation-path (evidence_38)
  - FAIL: search_9987:rule_03 (evidence_38)

## case_411 - COMPLETE
- subject: `user_409`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_8985` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-ambiguous`
  - `analytics_platform/analytics_298` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_38` link=`run-fingerprint`
  - `security_service/audit_record_4330` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_8985:rule_01 (evidence_38)
  - PASS: analytics_298:rule_07 (evidence_38)
  - PASS: audit_record_4330:rule_12 (evidence_38)

## case_412 - COMPLETE
- subject: `user_410`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2775` [USER_PROFILE] state=`ABSENT` evidence=`evidence_38` link=`run-ambiguous`
  - `security_service/audit_record_5637` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_38` link=`identity`
  - PASS: account_2775:rule_01 (evidence_38)
  - PASS: audit_record_5637:rule_12 (evidence_38)

## case_413 - INCOMPLETE
- subject: `user_411`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_563` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `analytics_platform/analytics_4523` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_9099` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_6162` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_563:rule_01 (evidence_39)
  - FAIL: analytics_4523:rule_07 (evidence_39)
  - PASS: audit_record_9099:rule_12 (evidence_39)
  - FAIL: search_6162:rule_03 (evidence_39)

## case_414 - INCOMPLETE
- subject: `user_412`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5260` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_3768` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_8770` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `support_platform/support_3768` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_39` link=`identity`
  - PASS: account_5260:rule_01 (evidence_39)
  - PASS: audit_record_3768:rule_12 (evidence_39)
  - FAIL: search_8770:rule_03 (evidence_39)
  - FAIL: support_3768:rule_05 (evidence_39)

## case_415 - INCOMPLETE
- subject: `user_413`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9975` [USER_PROFILE] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `analytics_platform/analytics_2102` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_6154` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_3864` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `support_platform/support_1993` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_39` link=`identity`
  - FAIL: account_9975:rule_01 (evidence_39)
  - FAIL: analytics_2102:rule_07 (evidence_39)
  - PASS: audit_record_6154:rule_12 (evidence_39)
  - FAIL: search_3864:rule_03 (evidence_39)
  - FAIL: support_1993:rule_05 (evidence_39)

## case_416 - INCOMPLETE
- subject: `user_414`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3075` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_8832` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `integration_service/data_flow_1412` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_39` link=`identity`
  - `search_service/search_6600` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_3075:rule_01 (evidence_39)
  - PASS: audit_record_8832:rule_12 (evidence_39)
  - FAIL: data_flow_1412:no-rule:recreation-path (evidence_39)
  - FAIL: search_6600:rule_03 (evidence_39)

## case_417 - INCOMPLETE
- subject: `user_415`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_4921` [USER_PROFILE] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_7959` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_5479` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - FAIL: account_4921:rule_01 (evidence_39)
  - PASS: audit_record_7959:rule_12 (evidence_39)
  - FAIL: search_5479:rule_03 (evidence_39)

## case_418 - INCOMPLETE
- subject: `user_416`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_9120` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_5493` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_8686` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `support_platform/support_9464` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_39` link=`identity`
  - PASS: account_9120:rule_01 (evidence_39)
  - PASS: audit_record_5493:rule_12 (evidence_39)
  - FAIL: search_8686:rule_03 (evidence_39)
  - FAIL: support_9464:rule_05 (evidence_39)

## case_419 - INCOMPLETE
- subject: `user_417`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1966` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_7716` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_5797` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `support_platform/support_2944` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_1966:rule_01 (evidence_39)
  - PASS: audit_record_7716:rule_12 (evidence_39)
  - FAIL: search_5797:rule_03 (evidence_39)
  - FAIL: support_2944:rule_06 (evidence_39)

## case_420 - INCOMPLETE
- subject: `user_418`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_7606` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_9687` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `export_service/export_389` [USER_EXPORT] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `search_service/search_8472` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_7606:rule_01 (evidence_39)
  - PASS: audit_record_9687:rule_12 (evidence_39)
  - FAIL: export_389:rule_09 (evidence_39)
  - FAIL: search_8472:rule_03 (evidence_39)

## case_421 - INCOMPLETE
- subject: `user_419`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_8482` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_1256` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `integration_service/data_flow_4750` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_39` link=`identity`
  - `search_service/search_3251` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_8482:rule_01 (evidence_39)
  - PASS: audit_record_1256:rule_12 (evidence_39)
  - FAIL: data_flow_4750:no-rule:recreation-path (evidence_39)
  - FAIL: search_3251:rule_03 (evidence_39)

## case_422 - INCOMPLETE
- subject: `user_420`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4087` [USER_PROFILE] state=`ABSENT` evidence=`evidence_39` link=`identity`
  - `security_service/audit_record_4218` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - `integration_service/data_flow_8871` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_39` link=`identity`
  - `search_service/search_7614` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_39` link=`identity`
  - PASS: account_4087:rule_01 (evidence_39)
  - PASS: audit_record_4218:rule_12 (evidence_39)
  - FAIL: data_flow_8871:no-rule:recreation-path (evidence_39)
  - FAIL: search_7614:rule_03 (evidence_39)

## case_423 - COMPLETE
- subject: `user_421`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2420` [USER_PROFILE] state=`ABSENT` evidence=`evidence_68` link=`identity+run`
  - `analytics_platform/analytics_6249` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_68` link=`run-fingerprint`
  - `security_service/audit_record_8082` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_2420:rule_01 (evidence_68)
  - PASS: analytics_6249:rule_07 (evidence_68)
  - PASS: audit_record_8082:rule_12 (evidence_68)

## case_424 - COMPLETE
- subject: `user_422`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_2696` [USER_PROFILE] state=`ABSENT` evidence=`evidence_68` link=`run-elimination`
  - `analytics_platform/analytics_3845` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_68` link=`run-fingerprint`
  - `security_service/audit_record_1474` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_2696:rule_01 (evidence_68)
  - PASS: analytics_3845:rule_07 (evidence_68)
  - PASS: audit_record_1474:rule_12 (evidence_68)

## case_425 - INCOMPLETE
- subject: `user_423`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9633` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-fingerprint`
  - `analytics_platform/analytics_891` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_68` link=`identity`
  - `security_service/audit_record_4863` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_7718` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_68` link=`identity`
  - `search_service/search_9072` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - `support_platform/support_1662` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_68` link=`identity`
  - PASS: account_9633:rule_01 (evidence_66)
  - FAIL: analytics_891:rule_07 (evidence_68)
  - UNKNOWN: audit_record_4863:observed (no evidence)
  - FAIL: data_flow_7718:no-rule:recreation-path (evidence_68)
  - FAIL: search_9072:rule_03 (evidence_68)
  - FAIL: support_1662:rule_05 (evidence_68)

## case_426 - INCOMPLETE
- subject: `user_424`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1576` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-fingerprint`
  - `security_service/audit_record_5472` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_2635` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - `support_platform/support_9212` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_68` link=`identity`
  - PASS: account_1576:rule_01 (evidence_66)
  - UNKNOWN: audit_record_5472:observed (no evidence)
  - FAIL: search_2635:rule_03 (evidence_68)
  - FAIL: support_9212:rule_05 (evidence_68)

## case_427 - COMPLETE
- subject: `user_425`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8461` [USER_PROFILE] state=`ABSENT` evidence=`evidence_68` link=`run-elimination`
  - `analytics_platform/analytics_8091` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_68` link=`run-fingerprint`
  - `security_service/audit_record_999` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_8461:rule_01 (evidence_68)
  - PASS: analytics_8091:rule_07 (evidence_68)
  - PASS: audit_record_999:rule_12 (evidence_68)

## case_428 - INCOMPLETE
- subject: `user_426`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2157` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `security_service/audit_record_7557` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_2107` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_68` link=`identity`
  - `search_service/search_2625` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_2157:rule_01 (evidence_66)
  - UNKNOWN: audit_record_7557:observed (no evidence)
  - FAIL: data_flow_2107:no-rule:recreation-path (evidence_68)
  - FAIL: search_2625:rule_03 (evidence_68)

## case_429 - INCOMPLETE
- subject: `user_427`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_4204` [USER_PROFILE] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - `security_service/audit_record_9805` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_1449` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - FAIL: account_4204:rule_01 (evidence_68)
  - UNKNOWN: audit_record_9805:observed (no evidence)
  - FAIL: search_1449:rule_03 (evidence_68)

## case_430 - COMPLETE
- subject: `user_428`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6006` [USER_PROFILE] state=`ABSENT` evidence=`evidence_68` link=`identity`
  - `security_service/audit_record_5292` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_6006:rule_01 (evidence_68)
  - PASS: audit_record_5292:rule_12 (evidence_68)

## case_431 - INCOMPLETE
- subject: `user_429`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6101` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `security_service/audit_record_3236` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_7427` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - `support_platform/support_3615` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_68` link=`identity`
  - PASS: account_6101:rule_01 (evidence_66)
  - UNKNOWN: audit_record_3236:observed (no evidence)
  - FAIL: search_7427:rule_03 (evidence_68)
  - FAIL: support_3615:rule_05 (evidence_68)

## case_432 - INCOMPLETE
- subject: `user_430`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6489` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `security_service/audit_record_3548` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_9343` [USER_EXPORT] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - `legal_service/legal_hold_438` [LEGAL_HOLD_RECORD] state=`None` evidence=`-` link=`identity`
  - `search_service/search_3844` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_68` link=`identity`
  - PASS: account_6489:rule_01 (evidence_66)
  - UNKNOWN: audit_record_3548:observed (no evidence)
  - FAIL: export_9343:rule_09 (evidence_68)
  - UNKNOWN: legal_hold_438:observed (no evidence)
  - FAIL: search_3844:rule_03 (evidence_68)

## case_433 - INCOMPLETE
- subject: `user_431`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5817` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_6665` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `integration_service/data_flow_1283` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_41` link=`identity`
  - `search_service/search_9100` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - PASS: account_5817:rule_01 (evidence_41)
  - PASS: audit_record_6665:rule_12 (evidence_41)
  - FAIL: data_flow_1283:no-rule:recreation-path (evidence_41)
  - FAIL: search_9100:rule_03 (evidence_41)

## case_434 - INCOMPLETE
- subject: `user_432`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4813` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `analytics_platform/analytics_2354` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_4043` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `integration_service/data_flow_9854` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_41` link=`identity`
  - `search_service/search_5626` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `support_platform/support_3364` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - PASS: account_4813:rule_01 (evidence_41)
  - FAIL: analytics_2354:rule_07 (evidence_41)
  - PASS: audit_record_4043:rule_12 (evidence_41)
  - FAIL: data_flow_9854:no-rule:recreation-path (evidence_41)
  - FAIL: search_5626:rule_03 (evidence_41)
  - FAIL: support_3364:rule_05 (evidence_41)

## case_435 - INCOMPLETE
- subject: `user_433`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_9194` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_9695` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `backup_service/backup_5237` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_41` link=`identity`
  - PASS: account_9194:rule_01 (evidence_41)
  - PASS: audit_record_9695:rule_12 (evidence_41)
  - FAIL: backup_5237:rule_14 (evidence_41)

## case_436 - INCOMPLETE
- subject: `user_434`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3078` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_2748` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `search_service/search_6599` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `support_platform/support_165` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - PASS: account_3078:rule_01 (evidence_41)
  - PASS: audit_record_2748:rule_12 (evidence_41)
  - FAIL: search_6599:rule_03 (evidence_41)
  - FAIL: support_165:rule_05 (evidence_41)

## case_437 - INCOMPLETE
- subject: `user_435`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_022` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `analytics_platform/analytics_6172` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_6846` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - PASS: account_022:rule_01 (evidence_41)
  - FAIL: analytics_6172:rule_07 (evidence_41)
  - PASS: audit_record_6846:rule_12 (evidence_41)

## case_438 - INCOMPLETE
- subject: `user_436`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1680` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `analytics_platform/analytics_6528` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_1366` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `integration_service/data_flow_3226` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_41` link=`identity`
  - `search_service/search_2052` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `support_platform/support_6688` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - PASS: account_1680:rule_01 (evidence_41)
  - FAIL: analytics_6528:rule_07 (evidence_41)
  - PASS: audit_record_1366:rule_12 (evidence_41)
  - FAIL: data_flow_3226:no-rule:recreation-path (evidence_41)
  - FAIL: search_2052:rule_03 (evidence_41)
  - FAIL: support_6688:rule_05 (evidence_41)

## case_439 - INCOMPLETE
- subject: `user_437`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3002` [USER_PROFILE] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_1149` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - FAIL: account_3002:rule_01 (evidence_41)
  - PASS: audit_record_1149:rule_12 (evidence_41)

## case_440 - INCOMPLETE
- subject: `user_438`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_790` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_5488` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `integration_service/data_flow_5967` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_41` link=`identity`
  - `search_service/search_2922` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - PASS: account_790:rule_01 (evidence_41)
  - PASS: audit_record_5488:rule_12 (evidence_41)
  - FAIL: data_flow_5967:no-rule:recreation-path (evidence_41)
  - FAIL: search_2922:rule_03 (evidence_41)

## case_441 - INCOMPLETE
- subject: `user_439`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1538` [USER_PROFILE] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_7313` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `search_service/search_3058` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - FAIL: account_1538:rule_01 (evidence_41)
  - PASS: audit_record_7313:rule_12 (evidence_41)
  - FAIL: search_3058:rule_03 (evidence_41)

## case_442 - INCOMPLETE
- subject: `user_440`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1897` [USER_PROFILE] state=`ABSENT` evidence=`evidence_41` link=`identity`
  - `security_service/audit_record_4839` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `search_service/search_1194` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_41` link=`identity`
  - `support_platform/support_4123` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_41` link=`identity`
  - PASS: account_1897:rule_01 (evidence_41)
  - PASS: audit_record_4839:rule_12 (evidence_41)
  - FAIL: search_1194:rule_03 (evidence_41)
  - FAIL: support_4123:rule_05 (evidence_41)

## case_443 - INCOMPLETE
- subject: `user_441`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1776` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-fingerprint`
  - `search_service/search_4925` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - `support_platform/support_8341` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - PASS: account_1776:rule_01 (evidence_66)
  - FAIL: search_4925:rule_03 (evidence_66)
  - FAIL: support_8341:rule_05 (evidence_66)

## case_444 - INCOMPLETE
- subject: `user_442`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_4042` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-fingerprint`
  - `export_service/export_4293` [USER_EXPORT] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - `search_service/search_3250` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_4042:rule_01 (evidence_66)
  - FAIL: export_4293:rule_09 (evidence_66)
  - FAIL: search_3250:rule_03 (evidence_66)

## case_445 - INCOMPLETE
- subject: `user_443`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1736` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `integration_service/data_flow_7584` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_66` link=`identity`
  - `search_service/search_2886` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_1736:rule_01 (evidence_66)
  - FAIL: data_flow_7584:no-rule:recreation-path (evidence_66)
  - FAIL: search_2886:rule_03 (evidence_66)

## case_446 - INCOMPLETE
- subject: `user_444`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3827` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `analytics_platform/analytics_195` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - `analytics_platform/analytics_7270` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_66` link=`run-fingerprint`
  - `integration_service/data_flow_1068` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_66` link=`identity`
  - `search_service/search_3780` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - `support_platform/support_9938` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - PASS: account_3827:rule_01 (evidence_66)
  - FAIL: analytics_195:rule_07 (evidence_66)
  - PASS: analytics_7270:rule_07 (evidence_66)
  - FAIL: data_flow_1068:no-rule:recreation-path (evidence_66)
  - FAIL: search_3780:rule_03 (evidence_66)
  - FAIL: support_9938:rule_05 (evidence_66)

## case_447 - INCOMPLETE
- subject: `user_445`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7340` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-fingerprint`
  - `backup_service/backup_5192` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_66` link=`identity`
  - PASS: account_7340:rule_01 (evidence_66)
  - FAIL: backup_5192:rule_14 (evidence_66)

## case_448 - COMPLETE
- subject: `user_446`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6635` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `security_service/audit_record_753` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_6635:rule_01 (evidence_66)
  - PASS: audit_record_753:rule_12 (evidence_66)

## case_449 - INCOMPLETE
- subject: `user_447`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5718` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `analytics_platform/analytics_1138` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - `search_service/search_1685` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_5718:rule_01 (evidence_66)
  - FAIL: analytics_1138:rule_07 (evidence_66)
  - FAIL: search_1685:rule_03 (evidence_66)

## case_450 - INCOMPLETE
- subject: `user_448`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9275` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `analytics_platform/analytics_8202` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - `integration_service/data_flow_9755` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_66` link=`identity`
  - `search_service/search_2365` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - `support_platform/support_7245` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_66` link=`identity`
  - PASS: account_9275:rule_01 (evidence_66)
  - FAIL: analytics_8202:rule_07 (evidence_66)
  - FAIL: data_flow_9755:no-rule:recreation-path (evidence_66)
  - FAIL: search_2365:rule_03 (evidence_66)
  - FAIL: support_7245:rule_05 (evidence_66)

## case_451 - INCOMPLETE
- subject: `user_449`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1895` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `integration_service/data_flow_7263` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_66` link=`identity`
  - `search_service/search_360` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_1895:rule_01 (evidence_66)
  - FAIL: data_flow_7263:no-rule:recreation-path (evidence_66)
  - FAIL: search_360:rule_03 (evidence_66)

## case_452 - COMPLETE
- subject: `user_450`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_6294` [USER_PROFILE] state=`ABSENT` evidence=`evidence_66` link=`run-elimination`
  - `analytics_platform/analytics_4031` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_66` link=`run-fingerprint`
  - `security_service/audit_record_8608` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_66` link=`identity`
  - PASS: account_6294:rule_01 (evidence_66)
  - PASS: analytics_4031:rule_07 (evidence_66)
  - PASS: audit_record_8608:rule_12 (evidence_66)

## case_453 - INCOMPLETE
- subject: `user_451`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3183` [USER_PROFILE] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `security_service/audit_record_3600` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `search_service/search_1317` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - FAIL: account_3183:rule_01 (evidence_43)
  - PASS: audit_record_3600:rule_12 (evidence_43)
  - FAIL: search_1317:rule_03 (evidence_43)

## case_454 - INCOMPLETE
- subject: `user_452`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3024` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `security_service/audit_record_2775` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `search_service/search_892` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_3024:rule_01 (evidence_43)
  - PASS: audit_record_2775:rule_12 (evidence_43)
  - FAIL: search_892:rule_03 (evidence_43)

## case_455 - INCOMPLETE
- subject: `user_453`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6373` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-fingerprint`
  - `analytics_platform/analytics_1126` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_43` link=`run-ambiguous`
  - `security_service/audit_record_2788` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `search_service/search_887` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `support_platform/support_2055` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_6373:rule_01 (evidence_43)
  - PASS: analytics_1126:rule_07 (evidence_43)
  - PASS: audit_record_2788:rule_12 (evidence_43)
  - FAIL: search_887:rule_03 (evidence_43)
  - FAIL: support_2055:rule_06 (evidence_43)

## case_456 - COMPLETE
- subject: `user_454`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_3584` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `analytics_platform/analytics_6750` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_43` link=`run-fingerprint`
  - `security_service/audit_record_8176` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_3584:rule_01 (evidence_43)
  - PASS: analytics_6750:rule_07 (evidence_43)
  - PASS: audit_record_8176:rule_12 (evidence_43)

## case_457 - COMPLETE
- subject: `user_455`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2761` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `security_service/audit_record_1171` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_2761:rule_01 (evidence_43)
  - PASS: audit_record_1171:rule_12 (evidence_43)

## case_458 - COMPLETE
- subject: `user_456`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_077` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `analytics_platform/analytics_5221` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_43` link=`run-fingerprint`
  - `security_service/audit_record_6750` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_077:rule_01 (evidence_43)
  - PASS: analytics_5221:rule_07 (evidence_43)
  - PASS: audit_record_6750:rule_12 (evidence_43)

## case_459 - INCOMPLETE
- subject: `user_457`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_5892` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `security_service/audit_record_6171` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `backup_service/backup_1140` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_43` link=`identity`
  - PASS: account_5892:rule_01 (evidence_43)
  - PASS: audit_record_6171:rule_12 (evidence_43)
  - FAIL: backup_1140:rule_14 (evidence_43)

## case_460 - INCOMPLETE
- subject: `user_458`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5167` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `security_service/audit_record_1369` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `legal_service/legal_hold_5622` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `support_platform/support_4146` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_43` link=`identity`
  - PASS: account_5167:rule_01 (evidence_43)
  - PASS: audit_record_1369:rule_12 (evidence_43)
  - PASS: legal_hold_5622:rule_13 (evidence_43)
  - FAIL: support_4146:rule_05 (evidence_43)

## case_461 - INCOMPLETE
- subject: `user_459`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4490` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `analytics_platform/analytics_8403` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_43` link=`identity`
  - `security_service/audit_record_3883` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `integration_service/data_flow_4612` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_43` link=`identity`
  - `search_service/search_9014` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - `support_platform/support_3901` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_43` link=`identity`
  - PASS: account_4490:rule_01 (evidence_43)
  - FAIL: analytics_8403:rule_07 (evidence_43)
  - PASS: audit_record_3883:rule_12 (evidence_43)
  - FAIL: data_flow_4612:no-rule:recreation-path (evidence_43)
  - FAIL: search_9014:rule_03 (evidence_43)
  - FAIL: support_3901:rule_05 (evidence_43)

## case_462 - COMPLETE
- subject: `user_460`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1881` [USER_PROFILE] state=`ABSENT` evidence=`evidence_43` link=`run-elimination`
  - `security_service/audit_record_641` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_43` link=`identity`
  - PASS: account_1881:rule_01 (evidence_43)
  - PASS: audit_record_641:rule_12 (evidence_43)

## case_463 - COMPLETE
- subject: `user_461`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1698` [USER_PROFILE] state=`ABSENT` evidence=`evidence_65` link=`identity`
  - `analytics_platform/analytics_689` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_65` link=`run-fingerprint`
  - `security_service/audit_record_8444` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - `backup_service/backup_2005` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_65` link=`identity`
  - `integration_service/data_flow_8024` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_65` link=`identity`
  - `support_platform/support_2659` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_65` link=`identity`
  - PASS: account_1698:rule_01 (evidence_65)
  - PASS: analytics_689:rule_07 (evidence_65)
  - PASS: audit_record_8444:rule_12 (evidence_65)
  - PASS: backup_2005:rule_14 (evidence_65)
  - PASS: data_flow_8024:no-rule:recreation-path (evidence_65)
  - PASS: support_2659:rule_05 (evidence_65)

## case_464 - COMPLETE
- subject: `user_462`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2480` [USER_PROFILE] state=`ABSENT` evidence=`evidence_65` link=`identity`
  - `analytics_platform/analytics_8746` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_65` link=`run-fingerprint`
  - `security_service/audit_record_5183` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - `backup_service/backup_7400` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_65` link=`identity`
  - `integration_service/data_flow_1344` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_65` link=`identity`
  - `support_platform/support_5586` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_65` link=`identity`
  - PASS: account_2480:rule_01 (evidence_65)
  - PASS: analytics_8746:rule_07 (evidence_65)
  - PASS: audit_record_5183:rule_12 (evidence_65)
  - PASS: backup_7400:rule_14 (evidence_65)
  - PASS: data_flow_1344:no-rule:recreation-path (evidence_65)
  - PASS: support_5586:rule_05 (evidence_65)

## case_465 - INCOMPLETE
- subject: `user_463`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3653` [USER_PROFILE] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - `security_service/audit_record_7099` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_728` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - FAIL: account_3653:rule_01 (evidence_65)
  - UNKNOWN: audit_record_7099:observed (no evidence)
  - FAIL: search_728:rule_03 (evidence_65)

## case_466 - INCOMPLETE
- subject: `user_464`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_7503` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_8892` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_8417` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - PASS: account_7503:rule_01 (evidence_45)
  - UNKNOWN: audit_record_8892:observed (no evidence)
  - FAIL: search_8417:rule_03 (evidence_65)

## case_467 - COMPLETE
- subject: `user_465`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2437` [USER_PROFILE] state=`ABSENT` evidence=`evidence_65` link=`identity`
  - `security_service/audit_record_8992` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - PASS: account_2437:rule_01 (evidence_65)
  - PASS: audit_record_8992:rule_12 (evidence_65)

## case_468 - INCOMPLETE
- subject: `user_466`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_641` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_307` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_9399` [USER_EXPORT] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - `search_service/search_9827` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - PASS: account_641:rule_01 (evidence_45)
  - UNKNOWN: audit_record_307:observed (no evidence)
  - FAIL: export_9399:rule_09 (evidence_65)
  - FAIL: search_9827:rule_03 (evidence_65)

## case_469 - INCOMPLETE
- subject: `user_467`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6645` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_7723` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_8730` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_65` link=`identity`
  - `search_service/search_8450` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - PASS: account_6645:rule_01 (evidence_45)
  - UNKNOWN: audit_record_7723:observed (no evidence)
  - FAIL: data_flow_8730:no-rule:recreation-path (evidence_65)
  - FAIL: search_8450:rule_03 (evidence_65)

## case_470 - COMPLETE
- subject: `user_468`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7023` [USER_PROFILE] state=`ABSENT` evidence=`evidence_65` link=`identity`
  - `analytics_platform/analytics_4066` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_65` link=`run-fingerprint`
  - `security_service/audit_record_2706` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - PASS: account_7023:rule_01 (evidence_65)
  - PASS: analytics_4066:rule_07 (evidence_65)
  - PASS: audit_record_2706:rule_12 (evidence_65)

## case_471 - INCOMPLETE
- subject: `user_469`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9034` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_3862` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_7543` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_65` link=`identity`
  - PASS: account_9034:rule_01 (evidence_45)
  - UNKNOWN: audit_record_3862:observed (no evidence)
  - FAIL: backup_7543:rule_14 (evidence_65)

## case_472 - INCOMPLETE
- subject: `user_470`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1957` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_157` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9152` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_65` link=`identity`
  - `support_platform/support_6987` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_65` link=`identity`
  - PASS: account_1957:rule_01 (evidence_45)
  - UNKNOWN: audit_record_157:observed (no evidence)
  - FAIL: search_9152:rule_03 (evidence_65)
  - FAIL: support_6987:rule_05 (evidence_65)

## case_473 - INCOMPLETE
- subject: `user_471`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6474` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `analytics_platform/analytics_8577` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_519` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `legal_service/legal_hold_4743` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `search_service/search_7375` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - PASS: account_6474:rule_01 (evidence_45)
  - FAIL: analytics_8577:rule_07 (evidence_45)
  - PASS: audit_record_519:rule_12 (evidence_45)
  - PASS: legal_hold_4743:rule_13 (evidence_45)
  - FAIL: search_7375:rule_03 (evidence_45)

## case_474 - INCOMPLETE
- subject: `user_472`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_9904` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `security_service/audit_record_712` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `search_service/search_9925` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `support_platform/support_4509` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_45` link=`identity`
  - PASS: account_9904:rule_01 (evidence_45)
  - PASS: audit_record_712:rule_12 (evidence_45)
  - FAIL: search_9925:rule_03 (evidence_45)
  - FAIL: support_4509:rule_05 (evidence_45)

## case_475 - INCOMPLETE
- subject: `user_473`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3205` [USER_PROFILE] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_5667` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - FAIL: account_3205:rule_01 (evidence_45)
  - PASS: audit_record_5667:rule_12 (evidence_45)

## case_476 - INCOMPLETE
- subject: `user_474`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3510` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `security_service/audit_record_4197` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `integration_service/data_flow_8899` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_45` link=`identity`
  - `search_service/search_3759` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - PASS: account_3510:rule_01 (evidence_45)
  - PASS: audit_record_4197:rule_12 (evidence_45)
  - FAIL: data_flow_8899:no-rule:recreation-path (evidence_45)
  - FAIL: search_3759:rule_03 (evidence_45)

## case_477 - INCOMPLETE
- subject: `user_475`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3119` [USER_PROFILE] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `security_service/audit_record_6405` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `search_service/search_5052` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - FAIL: account_3119:rule_01 (evidence_45)
  - PASS: audit_record_6405:rule_12 (evidence_45)
  - FAIL: search_5052:rule_03 (evidence_45)

## case_478 - INCOMPLETE
- subject: `user_476`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5934` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `security_service/audit_record_8754` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `search_service/search_5412` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `support_platform/support_3824` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_45` link=`identity`
  - PASS: account_5934:rule_01 (evidence_45)
  - PASS: audit_record_8754:rule_12 (evidence_45)
  - FAIL: search_5412:rule_03 (evidence_45)
  - FAIL: support_3824:rule_05 (evidence_45)

## case_479 - INCOMPLETE
- subject: `user_477`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5582` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `security_service/audit_record_5745` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `support_platform/support_4665` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - PASS: account_5582:rule_01 (evidence_45)
  - PASS: audit_record_5745:rule_12 (evidence_45)
  - FAIL: support_4665:rule_06 (evidence_45)

## case_480 - COMPLETE
- subject: `user_478`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2465` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-fingerprint`
  - `analytics_platform/analytics_1794` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_45` link=`run-fingerprint`
  - `security_service/audit_record_7742` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `backup_service/backup_7706` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_45` link=`identity`
  - `integration_service/data_flow_2893` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_45` link=`identity`
  - `support_platform/support_5854` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_45` link=`identity`
  - PASS: account_2465:rule_01 (evidence_45)
  - PASS: analytics_1794:rule_07 (evidence_45)
  - PASS: audit_record_7742:rule_12 (evidence_45)
  - PASS: backup_7706:rule_14 (evidence_45)
  - PASS: data_flow_2893:no-rule:recreation-path (evidence_45)
  - PASS: support_5854:rule_05 (evidence_45)

## case_481 - INCOMPLETE
- subject: `user_479`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_9449` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-fingerprint`
  - `security_service/audit_record_9025` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `integration_service/data_flow_173` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_45` link=`identity`
  - `search_service/search_8587` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - PASS: account_9449:rule_01 (evidence_45)
  - PASS: audit_record_9025:rule_12 (evidence_45)
  - FAIL: data_flow_173:no-rule:recreation-path (evidence_45)
  - FAIL: search_8587:rule_03 (evidence_45)

## case_482 - INCOMPLETE
- subject: `user_480`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9394` [USER_PROFILE] state=`ABSENT` evidence=`evidence_45` link=`run-elimination`
  - `security_service/audit_record_2180` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - `integration_service/data_flow_8519` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_45` link=`identity`
  - `search_service/search_3728` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_45` link=`identity`
  - PASS: account_9394:rule_01 (evidence_45)
  - PASS: audit_record_2180:rule_12 (evidence_45)
  - FAIL: data_flow_8519:no-rule:recreation-path (evidence_45)
  - FAIL: search_3728:rule_03 (evidence_45)

## case_483 - INCOMPLETE
- subject: `user_481`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_9398` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `security_service/audit_record_4738` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_4600` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_64` link=`identity`
  - `integration_service/data_flow_3669` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_64` link=`identity`
  - `search_service/search_1613` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `support_platform/support_4364` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - PASS: account_9398:rule_01 (evidence_63)
  - UNKNOWN: audit_record_4738:observed (no evidence)
  - FAIL: backup_4600:rule_14 (evidence_64)
  - FAIL: data_flow_3669:no-rule:recreation-path (evidence_64)
  - FAIL: search_1613:rule_03 (evidence_64)
  - FAIL: support_4364:rule_05 (evidence_64)

## case_484 - INCOMPLETE
- subject: `user_482`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2961` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `security_service/audit_record_5270` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `support_platform/support_7973` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - PASS: account_2961:rule_01 (evidence_63)
  - UNKNOWN: audit_record_5270:observed (no evidence)
  - FAIL: support_7973:rule_05 (evidence_64)

## case_485 - INCOMPLETE
- subject: `user_483`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3378` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `analytics_platform/analytics_1981` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - `security_service/audit_record_4405` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_3582` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - PASS: account_3378:rule_01 (evidence_63)
  - FAIL: analytics_1981:rule_07 (evidence_64)
  - UNKNOWN: audit_record_4405:observed (no evidence)
  - FAIL: search_3582:rule_03 (evidence_64)

## case_486 - COMPLETE
- subject: `user_484`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9031` [USER_PROFILE] state=`ABSENT` evidence=`evidence_64` link=`identity`
  - `analytics_platform/analytics_5948` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_64` link=`run-fingerprint`
  - `security_service/audit_record_5451` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - PASS: account_9031:rule_01 (evidence_64)
  - PASS: analytics_5948:rule_07 (evidence_64)
  - PASS: audit_record_5451:rule_12 (evidence_64)

## case_487 - INCOMPLETE
- subject: `user_485`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5293` [USER_PROFILE] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `analytics_platform/analytics_7818` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - `security_service/audit_record_1039` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_901` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `support_platform/support_5361` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - FAIL: account_5293:rule_01 (evidence_64)
  - FAIL: analytics_7818:rule_07 (evidence_64)
  - UNKNOWN: audit_record_1039:observed (no evidence)
  - FAIL: search_901:rule_03 (evidence_64)
  - FAIL: support_5361:rule_05 (evidence_64)

## case_488 - INCOMPLETE
- subject: `user_486`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_1433` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `security_service/audit_record_6252` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_3755` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_64` link=`identity`
  - `search_service/search_4216` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - PASS: account_1433:rule_01 (evidence_63)
  - UNKNOWN: audit_record_6252:observed (no evidence)
  - FAIL: data_flow_3755:no-rule:recreation-path (evidence_64)
  - FAIL: search_4216:rule_03 (evidence_64)

## case_489 - INCOMPLETE
- subject: `user_487`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6654` [USER_PROFILE] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `security_service/audit_record_1372` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_3426` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - FAIL: account_6654:rule_01 (evidence_64)
  - UNKNOWN: audit_record_1372:observed (no evidence)
  - FAIL: search_3426:rule_03 (evidence_64)

## case_490 - INCOMPLETE
- subject: `user_488`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4036` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `security_service/audit_record_5868` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9931` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `support_platform/support_4247` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - PASS: account_4036:rule_01 (evidence_63)
  - UNKNOWN: audit_record_5868:observed (no evidence)
  - FAIL: search_9931:rule_03 (evidence_64)
  - FAIL: support_4247:rule_05 (evidence_64)

## case_491 - COMPLETE
- subject: `user_489`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7455` [USER_PROFILE] state=`ABSENT` evidence=`evidence_64` link=`identity`
  - `security_service/audit_record_7073` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - PASS: account_7455:rule_01 (evidence_64)
  - PASS: audit_record_7073:rule_12 (evidence_64)

## case_492 - INCOMPLETE
- subject: `user_490`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3589` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`identity`
  - `analytics_platform/analytics_1575` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - `security_service/audit_record_9341` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_6406` [USER_EXPORT] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `search_service/search_9733` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_64` link=`identity`
  - `support_platform/support_6737` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_64` link=`identity`
  - PASS: account_3589:rule_01 (evidence_63)
  - FAIL: analytics_1575:rule_07 (evidence_64)
  - UNKNOWN: audit_record_9341:observed (no evidence)
  - FAIL: export_6406:rule_09 (evidence_64)
  - FAIL: search_9733:rule_03 (evidence_64)
  - FAIL: support_6737:rule_05 (evidence_64)

## case_493 - COMPLETE
- subject: `user_491`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_7766` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `analytics_platform/analytics_5893` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_63` link=`run-fingerprint`
  - `security_service/audit_record_730` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - PASS: account_7766:rule_01 (evidence_63)
  - PASS: analytics_5893:rule_07 (evidence_63)
  - PASS: audit_record_730:rule_12 (evidence_63)

## case_494 - COMPLETE
- subject: `user_492`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3479` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `analytics_platform/analytics_5443` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_63` link=`run-fingerprint`
  - `security_service/audit_record_1112` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - PASS: account_3479:rule_01 (evidence_63)
  - PASS: analytics_5443:rule_07 (evidence_63)
  - PASS: audit_record_1112:rule_12 (evidence_63)

## case_495 - INCOMPLETE
- subject: `user_493`; intent: rules+llm agree (deletion cue: 삭제; llm conf 0.95)
  - `account_service/account_9784` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `backup_service/backup_5061` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_63` link=`identity`
  - PASS: account_9784:rule_01 (evidence_63)
  - FAIL: backup_5061:rule_14 (evidence_63)

## case_496 - INCOMPLETE
- subject: `user_494`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2512` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `search_service/search_3169` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - `support_platform/support_6391` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_63` link=`identity`
  - PASS: account_2512:rule_01 (evidence_63)
  - FAIL: search_3169:rule_03 (evidence_63)
  - FAIL: support_6391:rule_05 (evidence_63)

## case_497 - COMPLETE
- subject: `user_495`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5281` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `analytics_platform/analytics_6565` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_63` link=`run-fingerprint`
  - `security_service/audit_record_9796` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - PASS: account_5281:rule_01 (evidence_63)
  - PASS: analytics_6565:rule_07 (evidence_63)
  - PASS: audit_record_9796:rule_12 (evidence_63)

## case_498 - INCOMPLETE
- subject: `user_496`; intent: rules+llm agree (deletion cue: eliminaci[oó]n; llm conf 0.95)
  - `account_service/account_282` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `search_service/search_6093` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - `support_platform/support_9075` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_63` link=`identity`
  - PASS: account_282:rule_01 (evidence_63)
  - FAIL: search_6093:rule_03 (evidence_63)
  - FAIL: support_9075:rule_05 (evidence_63)

## case_499 - INCOMPLETE
- subject: `user_497`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_3626` [USER_PROFILE] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - FAIL: account_3626:rule_01 (evidence_63)

## case_500 - INCOMPLETE
- subject: `user_498`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_5738` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `integration_service/data_flow_006` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_63` link=`identity`
  - `search_service/search_6092` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - PASS: account_5738:rule_01 (evidence_63)
  - FAIL: data_flow_006:no-rule:recreation-path (evidence_63)
  - FAIL: search_6092:rule_03 (evidence_63)

## case_501 - INCOMPLETE
- subject: `user_499`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_634` [USER_PROFILE] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - `search_service/search_2799` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - FAIL: account_634:rule_01 (evidence_63)
  - FAIL: search_2799:rule_03 (evidence_63)

## case_502 - COMPLETE
- subject: `user_500`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_2554` [USER_PROFILE] state=`ABSENT` evidence=`evidence_63` link=`run-elimination`
  - `security_service/audit_record_5238` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_63` link=`identity`
  - PASS: account_2554:rule_01 (evidence_63)
  - PASS: audit_record_5238:rule_12 (evidence_63)

## case_503 - INCOMPLETE
- subject: `user_501`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 1.0)
  - `account_service/account_5394` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `security_service/audit_record_5454` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `support_platform/support_2295` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_5394:rule_01 (evidence_47)
  - PASS: audit_record_5454:rule_12 (evidence_47)
  - FAIL: support_2295:rule_06 (evidence_47)

## case_504 - INCOMPLETE
- subject: `user_502`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7244` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-fingerprint`
  - `security_service/audit_record_3733` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `export_service/export_3120` [USER_EXPORT] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_7244:rule_01 (evidence_47)
  - PASS: audit_record_3733:rule_12 (evidence_47)
  - FAIL: export_3120:rule_09 (evidence_47)

## case_505 - INCOMPLETE
- subject: `user_503`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8136` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-fingerprint`
  - `security_service/audit_record_3441` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `integration_service/data_flow_5281` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_47` link=`identity`
  - `legal_service/legal_hold_2227` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `search_service/search_2591` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_8136:rule_01 (evidence_47)
  - PASS: audit_record_3441:rule_12 (evidence_47)
  - FAIL: data_flow_5281:no-rule:recreation-path (evidence_47)
  - PASS: legal_hold_2227:rule_13 (evidence_47)
  - FAIL: search_2591:rule_03 (evidence_47)

## case_506 - COMPLETE
- subject: `user_504`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6161` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `security_service/audit_record_1361` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_6161:rule_01 (evidence_47)
  - PASS: audit_record_1361:rule_12 (evidence_47)

## case_507 - INCOMPLETE
- subject: `user_505`; intent: rules+llm agree (deletion cue: 削除; llm conf 0.95)
  - `account_service/account_3772` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `security_service/audit_record_7627` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `backup_service/backup_369` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_47` link=`identity`
  - PASS: account_3772:rule_01 (evidence_47)
  - PASS: audit_record_7627:rule_12 (evidence_47)
  - FAIL: backup_369:rule_14 (evidence_47)

## case_508 - INCOMPLETE
- subject: `user_506`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_5423` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `security_service/audit_record_8154` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `support_platform/support_2691` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_47` link=`identity`
  - PASS: account_5423:rule_01 (evidence_47)
  - PASS: audit_record_8154:rule_12 (evidence_47)
  - FAIL: support_2691:rule_05 (evidence_47)

## case_509 - INCOMPLETE
- subject: `user_507`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6623` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `analytics_platform/analytics_784` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_47` link=`identity`
  - `security_service/audit_record_2323` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `search_service/search_6246` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_6623:rule_01 (evidence_47)
  - FAIL: analytics_784:rule_07 (evidence_47)
  - PASS: audit_record_2323:rule_12 (evidence_47)
  - FAIL: search_6246:rule_03 (evidence_47)

## case_510 - INCOMPLETE
- subject: `user_508`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6049` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `security_service/audit_record_4266` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `search_service/search_6147` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `support_platform/support_9648` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_47` link=`identity`
  - PASS: account_6049:rule_01 (evidence_47)
  - PASS: audit_record_4266:rule_12 (evidence_47)
  - FAIL: search_6147:rule_03 (evidence_47)
  - FAIL: support_9648:rule_05 (evidence_47)

## case_511 - INCOMPLETE
- subject: `user_509`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1035` [USER_PROFILE] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `security_service/audit_record_4883` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - `legal_service/legal_hold_4887` [LEGAL_HOLD_RECORD] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - FAIL: account_1035:rule_01 (evidence_47)
  - PASS: audit_record_4883:rule_12 (evidence_47)
  - PASS: legal_hold_4887:rule_13 (evidence_47)

## case_512 - COMPLETE
- subject: `user_510`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_445` [USER_PROFILE] state=`ABSENT` evidence=`evidence_47` link=`run-elimination`
  - `analytics_platform/analytics_1558` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_47` link=`run-fingerprint`
  - `security_service/audit_record_4219` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_47` link=`identity`
  - PASS: account_445:rule_01 (evidence_47)
  - PASS: analytics_1558:rule_07 (evidence_47)
  - PASS: audit_record_4219:rule_12 (evidence_47)

## case_513 - INCOMPLETE
- subject: `user_511`; intent: rules+llm agree (deletion cue: suppression; llm conf 0.95)
  - `account_service/account_1334` [USER_PROFILE] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_2044` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `search_service/search_4739` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - FAIL: account_1334:rule_01 (evidence_48)
  - PASS: audit_record_2044:rule_12 (evidence_48)
  - FAIL: search_4739:rule_03 (evidence_48)

## case_514 - INCOMPLETE
- subject: `user_512`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6473` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `analytics_platform/analytics_9920` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_1967` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `integration_service/data_flow_9556` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_48` link=`identity`
  - `search_service/search_2715` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `support_platform/support_3982` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_48` link=`identity`
  - PASS: account_6473:rule_01 (evidence_48)
  - FAIL: analytics_9920:rule_07 (evidence_48)
  - PASS: audit_record_1967:rule_12 (evidence_48)
  - FAIL: data_flow_9556:no-rule:recreation-path (evidence_48)
  - FAIL: search_2715:rule_03 (evidence_48)
  - FAIL: support_3982:rule_05 (evidence_48)

## case_515 - INCOMPLETE
- subject: `user_513`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3411` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_7062` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `search_service/search_1928` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `support_platform/support_4533` [SUPPORT_ATTACHMENT] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - PASS: account_3411:rule_01 (evidence_48)
  - PASS: audit_record_7062:rule_12 (evidence_48)
  - FAIL: search_1928:rule_03 (evidence_48)
  - FAIL: support_4533:rule_06 (evidence_48)

## case_516 - COMPLETE
- subject: `user_514`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_141` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `analytics_platform/analytics_4804` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_48` link=`run-fingerprint`
  - `security_service/audit_record_3777` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - PASS: account_141:rule_01 (evidence_48)
  - PASS: analytics_4804:rule_07 (evidence_48)
  - PASS: audit_record_3777:rule_12 (evidence_48)

## case_517 - INCOMPLETE
- subject: `user_515`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3407` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_946` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `integration_service/data_flow_8165` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_48` link=`identity`
  - `search_service/search_2818` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - PASS: account_3407:rule_01 (evidence_48)
  - PASS: audit_record_946:rule_12 (evidence_48)
  - FAIL: data_flow_8165:no-rule:recreation-path (evidence_48)
  - FAIL: search_2818:rule_03 (evidence_48)

## case_518 - INCOMPLETE
- subject: `user_516`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9641` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_5572` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `integration_service/data_flow_3518` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_48` link=`identity`
  - `search_service/search_6401` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - PASS: account_9641:rule_01 (evidence_48)
  - PASS: audit_record_5572:rule_12 (evidence_48)
  - FAIL: data_flow_3518:no-rule:recreation-path (evidence_48)
  - FAIL: search_6401:rule_03 (evidence_48)

## case_519 - INCOMPLETE
- subject: `user_517`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1506` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_4027` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `backup_service/backup_8264` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_48` link=`identity`
  - PASS: account_1506:rule_01 (evidence_48)
  - PASS: audit_record_4027:rule_12 (evidence_48)
  - FAIL: backup_8264:rule_14 (evidence_48)

## case_520 - INCOMPLETE
- subject: `user_518`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4979` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_9504` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `support_platform/support_9251` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_48` link=`identity`
  - PASS: account_4979:rule_01 (evidence_48)
  - PASS: audit_record_9504:rule_12 (evidence_48)
  - FAIL: support_9251:rule_05 (evidence_48)

## case_521 - COMPLETE
- subject: `user_519`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1482` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `analytics_platform/analytics_7277` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_48` link=`run-fingerprint`
  - `security_service/audit_record_3567` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - PASS: account_1482:rule_01 (evidence_48)
  - PASS: analytics_7277:rule_07 (evidence_48)
  - PASS: audit_record_3567:rule_12 (evidence_48)

## case_522 - INCOMPLETE
- subject: `user_520`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_1096` [USER_PROFILE] state=`ABSENT` evidence=`evidence_48` link=`identity`
  - `security_service/audit_record_5513` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_48` link=`identity`
  - `support_platform/support_8538` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_48` link=`identity`
  - PASS: account_1096:rule_01 (evidence_48)
  - PASS: audit_record_5513:rule_12 (evidence_48)
  - FAIL: support_8538:rule_05 (evidence_48)

## case_523 - INCOMPLETE
- subject: `user_521`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_2424` [USER_PROFILE] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `security_service/audit_record_2172` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_9075` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - FAIL: account_2424:rule_01 (evidence_62)
  - UNKNOWN: audit_record_2172:observed (no evidence)
  - FAIL: search_9075:rule_03 (evidence_62)

## case_524 - COMPLETE
- subject: `user_522`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_704` [USER_PROFILE] state=`ABSENT` evidence=`evidence_62` link=`run-elimination`
  - `security_service/audit_record_5429` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - PASS: account_704:rule_01 (evidence_62)
  - PASS: audit_record_5429:rule_12 (evidence_62)

## case_525 - INCOMPLETE
- subject: `user_523`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_4974` [USER_PROFILE] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `security_service/audit_record_3803` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - FAIL: account_4974:rule_01 (evidence_62)
  - UNKNOWN: audit_record_3803:observed (no evidence)

## case_526 - INCOMPLETE
- subject: `user_524`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1400` [USER_PROFILE] state=`None` evidence=`-` link=`run-elimination`
  - `analytics_platform/analytics_131` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - `security_service/audit_record_5792` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_2263` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_62` link=`identity`
  - `search_service/search_3879` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `support_platform/support_1191` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - UNKNOWN: account_1400:observed (no evidence)
  - FAIL: analytics_131:rule_07 (evidence_62)
  - UNKNOWN: audit_record_5792:observed (no evidence)
  - FAIL: data_flow_2263:no-rule:recreation-path (evidence_62)
  - FAIL: search_3879:rule_03 (evidence_62)
  - FAIL: support_1191:rule_05 (evidence_62)

## case_527 - INCOMPLETE
- subject: `user_525`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_3693` [USER_PROFILE] state=`None` evidence=`-` link=`run-fingerprint`
  - `analytics_platform/analytics_7468` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - `security_service/audit_record_2758` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `search_service/search_1091` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `support_platform/support_3896` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - `support_platform/support_9832` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - UNKNOWN: account_3693:observed (no evidence)
  - FAIL: analytics_7468:rule_07 (evidence_62)
  - UNKNOWN: audit_record_2758:observed (no evidence)
  - FAIL: search_1091:rule_03 (evidence_62)
  - FAIL: support_3896:rule_05 (evidence_62)
  - FAIL: support_9832:rule_05 (evidence_62)

## case_528 - INCOMPLETE
- subject: `user_526`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_1184` [USER_PROFILE] state=`None` evidence=`-` link=`run-elimination`
  - `analytics_platform/analytics_8476` [ANALYTICS_PROFILE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - `security_service/audit_record_2284` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `export_service/export_9388` [USER_EXPORT] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `search_service/search_1429` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `support_platform/support_193` [SUPPORT_MESSAGE] state=`IDENTIFIABLE` evidence=`evidence_62` link=`identity`
  - UNKNOWN: account_1184:observed (no evidence)
  - FAIL: analytics_8476:rule_07 (evidence_62)
  - UNKNOWN: audit_record_2284:observed (no evidence)
  - FAIL: export_9388:rule_09 (evidence_62)
  - FAIL: search_1429:rule_03 (evidence_62)
  - FAIL: support_193:rule_05 (evidence_62)

## case_529 - INCOMPLETE
- subject: `user_527`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4063` [USER_PROFILE] state=`None` evidence=`-` link=`run-fingerprint`
  - `security_service/audit_record_4542` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `integration_service/data_flow_6588` [DATA_FLOW] state=`ACTIVE` evidence=`evidence_62` link=`identity`
  - `search_service/search_3382` [SEARCH_INDEX_ENTRY] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - UNKNOWN: account_4063:observed (no evidence)
  - UNKNOWN: audit_record_4542:observed (no evidence)
  - FAIL: data_flow_6588:no-rule:recreation-path (evidence_62)
  - FAIL: search_3382:rule_03 (evidence_62)

## case_530 - COMPLETE
- subject: `user_528`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_6169` [USER_PROFILE] state=`ABSENT` evidence=`evidence_62` link=`run-elimination`
  - `analytics_platform/analytics_893` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_62` link=`run-fingerprint`
  - `security_service/audit_record_2152` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - PASS: account_6169:rule_01 (evidence_62)
  - PASS: analytics_893:rule_07 (evidence_62)
  - PASS: audit_record_2152:rule_12 (evidence_62)

## case_531 - INCOMPLETE
- subject: `user_529`; intent: rules+llm agree (deletion cue: \berase; llm conf 0.95)
  - `account_service/account_3146` [USER_PROFILE] state=`None` evidence=`-` link=`run-elimination`
  - `security_service/audit_record_8556` [SECURITY_AUDIT_LOG] state=`None` evidence=`-` link=`identity`
  - `backup_service/backup_3382` [BACKUP_ARCHIVE] state=`ACTIVE` evidence=`evidence_62` link=`identity`
  - UNKNOWN: account_3146:observed (no evidence)
  - UNKNOWN: audit_record_8556:observed (no evidence)
  - FAIL: backup_3382:rule_14 (evidence_62)

## case_532 - COMPLETE
- subject: `user_530`; intent: rules+llm agree (deletion cue: \bremove (?:my|the|this) (?:account|profile); llm conf 0.95)
  - `account_service/account_470` [USER_PROFILE] state=`ABSENT` evidence=`evidence_62` link=`run-elimination`
  - `analytics_platform/analytics_3744` [ANALYTICS_PROFILE] state=`CLEAN` evidence=`evidence_62` link=`run-fingerprint`
  - `security_service/audit_record_4828` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_62` link=`identity`
  - `backup_service/backup_6344` [BACKUP_ARCHIVE] state=`INACTIVE` evidence=`evidence_62` link=`identity`
  - `integration_service/data_flow_6987` [DATA_FLOW] state=`INACTIVE` evidence=`evidence_62` link=`identity`
  - `support_platform/support_7724` [SUPPORT_MESSAGE] state=`CLEAN` evidence=`evidence_62` link=`identity`
  - PASS: account_470:rule_01 (evidence_62)
  - PASS: analytics_3744:rule_07 (evidence_62)
  - PASS: audit_record_4828:rule_12 (evidence_62)
  - PASS: backup_6344:rule_14 (evidence_62)
  - PASS: data_flow_6987:no-rule:recreation-path (evidence_62)
  - PASS: support_7724:rule_05 (evidence_62)

## case_533 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \bout of date\b; llm conf 1.0)

## case_534 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: promotional e-?mails; llm conf 1.0)

## case_535 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \b(?:copy|download|portable|export) (?:of )?(?:my|the)? ?(?:account )?(?:information|data); llm conf 1.0)

## case_536 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \breset(?:ting)? the login; llm conf 1.0)

## case_537 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \bmisspelled\b; llm conf 1.0)

## case_538 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: marketing lists? only; llm conf 1.0)

## case_539 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: what personal information; llm conf 1.0)

## case_540 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \binvoices?\b; llm conf 0.95)

## case_541 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: change the email address; llm conf 1.0)

## case_542 - NOT_APPLICABLE
- subject: `n/a`; request does not authorise deletion; intent: rules+llm agree (non-deletion cue: \b(?:copy|download|portable|export) (?:of )?(?:my|the)? ?(?:account )?(?:information|data); llm conf 1.0)

## case_543 - COMPLETE
- subject: `user_543`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_8931` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-fingerprint`
  - `security_service/audit_record_6244` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_205` [ACCOUNT_TOMBSTONE] state=`CLEAN` evidence=`evidence_52` link=`identity`
  - PASS: account_8931:rule_01 (evidence_02)
  - PASS: audit_record_6244:rule_12 (evidence_52)
  - PASS: tombstone_205:rule_15 (evidence_52)

## case_544 - INCOMPLETE
- subject: `user_544`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7320` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-elimination`
  - `security_service/audit_record_1037` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_8648` [ACCOUNT_TOMBSTONE] state=`IDENTIFIABLE` evidence=`evidence_52` link=`identity`
  - PASS: account_7320:rule_01 (evidence_02)
  - PASS: audit_record_1037:rule_12 (evidence_52)
  - FAIL: tombstone_8648:rule_15 (evidence_52)

## case_545 - COMPLETE
- subject: `user_545`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_2577` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-elimination`
  - `security_service/audit_record_5041` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_946` [ACCOUNT_TOMBSTONE] state=`CLEAN` evidence=`evidence_52` link=`identity`
  - PASS: account_2577:rule_01 (evidence_02)
  - PASS: audit_record_5041:rule_12 (evidence_52)
  - PASS: tombstone_946:rule_15 (evidence_52)

## case_546 - INCOMPLETE
- subject: `user_546`; intent: rules+llm agree (deletion cue: exclus[aã]o; llm conf 0.95)
  - `account_service/account_294` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-elimination`
  - `security_service/audit_record_518` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_8095` [ACCOUNT_TOMBSTONE] state=`IDENTIFIABLE` evidence=`evidence_52` link=`identity`
  - PASS: account_294:rule_01 (evidence_02)
  - PASS: audit_record_518:rule_12 (evidence_52)
  - FAIL: tombstone_8095:rule_15 (evidence_52)

## case_547 - COMPLETE
- subject: `user_547`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_9155` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-fingerprint`
  - `security_service/audit_record_7352` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_8774` [ACCOUNT_TOMBSTONE] state=`CLEAN` evidence=`evidence_52` link=`identity`
  - PASS: account_9155:rule_01 (evidence_02)
  - PASS: audit_record_7352:rule_12 (evidence_52)
  - PASS: tombstone_8774:rule_15 (evidence_52)

## case_548 - INCOMPLETE
- subject: `user_548`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7015` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-elimination`
  - `security_service/audit_record_6970` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_3745` [ACCOUNT_TOMBSTONE] state=`IDENTIFIABLE` evidence=`evidence_52` link=`identity`
  - PASS: account_7015:rule_01 (evidence_02)
  - PASS: audit_record_6970:rule_12 (evidence_52)
  - FAIL: tombstone_3745:rule_15 (evidence_52)

## case_549 - COMPLETE
- subject: `user_549`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_4842` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-fingerprint`
  - `security_service/audit_record_1491` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_3963` [ACCOUNT_TOMBSTONE] state=`CLEAN` evidence=`evidence_52` link=`identity`
  - PASS: account_4842:rule_01 (evidence_02)
  - PASS: audit_record_1491:rule_12 (evidence_52)
  - PASS: tombstone_3963:rule_15 (evidence_52)

## case_550 - INCOMPLETE
- subject: `user_550`; intent: rules+llm agree (deletion cue: \bdelet; llm conf 0.95)
  - `account_service/account_7225` [USER_PROFILE] state=`ABSENT` evidence=`evidence_02` link=`run-elimination`
  - `security_service/audit_record_3831` [SECURITY_AUDIT_LOG] state=`PRESENT` evidence=`evidence_52` link=`identity`
  - `identity_service/tombstone_7389` [ACCOUNT_TOMBSTONE] state=`IDENTIFIABLE` evidence=`evidence_52` link=`identity`
  - PASS: account_7225:rule_01 (evidence_02)
  - PASS: audit_record_3831:rule_12 (evidence_52)
  - FAIL: tombstone_7389:rule_15 (evidence_52)
