# Institution Spreadsheet Reference

## Key columns

| Field | 中文标签 | Research priority |
|-------|----------|-------------------|
| `school_id` | 院校 ID | Stable slug; do not change |
| `school_name_en` | 英文校名 | Official English name |
| `school_name_zh` | 中文校名 | Standard Chinese translation |
| `test_policy` | 标化政策 | required / optional / test-free / test-flexible + cycle notes |
| `admission_rate` | 录取率 | Latest CDS or official stat |
| `toefl_min_ibt` | TOEFL 最低分 | International admissions page |
| `ielts_min` | IELTS 最低分 | Same |
| `duolingo_min` | Duolingo 最低分 | Same |
| `english_waiver_policy` | 英语豁免政策 | Same |
| `ed_deadline` | ED 截止 | YYYY-MM-DD |
| `ea_deadline` | EA 截止 | YYYY-MM-DD |
| `rd_deadline` | RD 截止 | YYYY-MM-DD |
| `application_fee` | 申请费 | USD amount |
| `application_platform` | 申请系统 | Common App / Coalition / UC / school portal |
| `need_blind_international` | 国际 Need-Blind | yes / no |
| `need_blind_domestic` | 国内 Need-Blind | yes / no |
| `meets_full_need` | 满足全部需求 | yes / no / partial |
| `merit_scholarships` |  merit 奖学金 | yes / no |
| `intl_scholarship_available` | 国际生奖学金 | yes / no / limited |
| `tuition_out_of_state` | 学费（州外/私立） | USD, academic year |
| `room_board` | 食宿费 | USD |
| `total_cost` | 总费用 | USD |
| `admissions_url` | 招生页 | Official URL |
| `intl_admissions_url` | 国际生招生页 | Official URL |
| `source_url` | 来源 URL | Page used for this verification |
| `source_notes` | 来源说明 | `Verified YYYY-MM-DD from ...` |
| `notes_zh` | 备注 (ZH) | Concise Chinese policy notes |
| `notes_en` | 备注 (EN) | Optional English notes |
| `last_updated` | 最后更新 | YYYY-MM-DD |

## Comparison normalization

Before diffing:

1. Strip leading/trailing whitespace
2. Collapse internal whitespace runs
3. Treat `""`, `—`, `-`, `N/A`, `n/a`, `null` as empty
4. Dates: normalize to `YYYY-MM-DD` when unambiguous

## US undergrad preset groups

Common filenames → `preset_group` value:

| File pattern | Group |
|--------------|-------|
| `top30.csv` | top30 |
| `lac_top20.csv` | lac_top20 |
| `uc_colleges.csv`, `uc_*.csv` | uc_system |
| `stanford_intl.csv` | stanford_intl |

## Official source hierarchy

1. University admissions domain (`.edu`)
2. UC system unified pages for UC campuses
3. Common Data Set (CDS) PDF for stats
4. US News / third-party — **only** when official site lacks data; note in `source_notes`

## Summary interpretation prompts

When writing `summary_zh` for the PDF, highlight:

- Testing policy flips (optional → required, test-free changes)
- Deadline moves affecting current application cycle
- New English proficiency requirements for internationals
- Financial aid / scholarship policy changes
- System-wide changes (e.g. all UC campuses)
