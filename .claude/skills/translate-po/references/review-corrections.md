# Common Review Corrections

What reviewers of this repo most often ask translators to fix, mined from
merged PRs. Use it as a pre-PR checklist: the top sections are the most
frequent corrections. Counts are relative frequency, not exact figures.
Each rule says whether README.rst / the other references already cover it.

Open question: #860 asked for 打印→列印, while `forbidden-terms.md` maps
打印→印出. Follow `forbidden-terms.md` until maintainers decide.

## Sample

- **Source:** the 150 most recent merged PRs that had reviewer inline comments. Bot, dependabot, `app/*` and "sync"/"bump" PRs were skipped, and so were the PR author's own replies.
- **PR range:** #763 – #1246, merged 2023-12-20 → 2026-10-05.
- **Comments analysed:** 1,552 inline review comments. 1,074 of them are ```` ```suggestion ```` blocks, which were diffed against the original line in `diff_hunk`. Also analysed: 83 non-trivial review summaries.
- **Method:** each suggestion was diffed at character level and auto-tagged (spacing, `\\ `, punctuation, roles, term swaps, CJK→Latin). The free-text notes were keyword-classified, then spot-read by hand. One comment can fall into several categories. Counts are therefore approximate: read them as *relative* frequency, not exact figures.
- **Coverage:** "Coverage" says whether a rule is already in `README.rst` (翻譯守則, lines ~240-377) or `.claude/skills/*/references/*.md`. Values are **NEW**, **ALREADY-COVERED** or **PARTIAL** (the base rule is covered; the specific sub-rule is new).

---

## 1. Awkward, literal or inaccurate phrasing (翻譯腔 / meaning)

**Rule:** the msgstr must read like natural Chinese and say exactly what the source says. Reviewers rewrite English sentence order, stacked 的, needless 被 passives, and wrong subject/object.

- **Count:** ~508 suggestion rewrites in 109 PRs (CJK changes beyond a term swap). Of these, 100 notes say "meaning wrong / 原文想表達…" (55 PRs) and 68 say "不通順 / 不流暢 / 像英文句型" (43 PRs).
- **Coverage:** NEW. The skills have no guidance on phrasing or on checking meaning.

**Typical fixes:**
- Wrong object of the verb:
  - Before: `將 *iterable* 中的內容擴展至 *list*`
  - After: `以 *iterable* 中的內容擴展 *list*`
  - Reviewer note: 「擴展」的受詞應該是 list. (#1178)
- English clause order rewritten:
  - Before: `在 Unicode Technical Standard #18 中的嵌套集合與集合操作可能會在未來添加支援`
  - After: `未來可能會支援 Unicode Technical Standard #18 中的嵌套集合與集合操作` (#1147)
- Literal "just":
  - Before: `而不是僅被引入時執行`
  - After: `而不會在被引入時就執行` (#1126)
- Other recurring notes:
  - "nit: too many 的?" (#1190)
  - 「的」好像有點過多 (#1010)
  - 修改後最後一句還是比較像是英文句型的結構 (#876)
  - 原文是 *is now* 而非 *is not* (#1029)
  - 「一般也比較常聽到『不支援 64 位元作業系統』而不是『…不被支援』」, i.e. prefer the active voice (#828)

## 2. Terminology: wrong term or a zh_CN term

**Rule:** use the project term list (wiki 術語列表, `glossary.po`), not zh_CN vocabulary or ad-hoc choices.

- **Count:** ~348 comments in 93 PRs. A full breakdown is in the table at the end.
- **Coverage:**
  - PARTIAL. Most zh_CN swaps are in `forbidden-terms.md` and `terminology.md`.
  - Several frequently enforced pairs are missing (marked NEW in the table): 傳回, 拋出, 通過, 協議, 命令行, 客戶端, 清單 vs 串列, 檔案 vs 文件, and more.

**Examples:**
- 參數 → 引數 for *argument*: 28 comments in 16 PRs, the single most frequent fix.
  - Before: `參數 *start*，*stop* 和 *step* 會被計算多次`
  - After: `引數 *start*、*stop* 和 *step*…` (#1149)
  - The reverse also happens: *parameter* must be 參數 (#1095, #1048).
- C API wording. "raise" is 引發, but "sets an exception" is 設定例外, not 拋出異常.
  - Before: `並拋出 :exc:\`IndexError\` 異常`
  - After: `並設定 :exc:\`IndexError\` 例外` (#1164)
- Python list vs a generic list:
  - "當原文指稱的是 Python list 時我們習慣翻譯成「串列」，但如果不是 Python list 那大多時候就會翻譯成「清單」" (#1076; also #1052 and #1115)

## 3. CJK–Latin spacing and stray spaces

**Rule:**
- One half-width space between CJK and Latin letters, digits or inline markup.
- **No** space between a full-width punctuation mark and its neighbour.
- No space between two CJK characters, and no space after `。`.

- **Count:** ~243 comments in 78 PRs.
  - Missing CJK–Latin space: 132 comments in 63 PRs.
  - Space beside full-width punctuation removed: 97 comments in 35 PRs.
- **Coverage:**
  - The base CJK–Latin rule is ALREADY-COVERED (README; validation-rules).
  - "No space next to full-width punctuation, even when the neighbour is markup or English" is PARTIAL (README only says 符號英文間不用).
  - "No space after 。 / between CJK chars" is NEW.

**Examples:**
- `你可以在Python 3.14+` → `你可以在 Python 3.14+` (#1242)
- `Class method會基於數字` → `Class method 會基於數字` (#1229)
- ```__annotations__`` 。` → ```__annotations__``。` (#1242)
- Notes:
  - "句號後面不用空格" (#1095)
  - "中文字間不留空白" (#1057, #1054)
  - "英文與中式標點符號間不用留空格" (#828)

## 4. `\\ ` zero-width separator misuse

**Rule:**
- Put `\\ ` between a CJK character and a reST role, `*emphasis*` or link, where the markup needs a boundary.
- Do **not** put it next to full-width `，。、：；）「」`. A `（` that directly follows markup is the risky case: it can break the build.
- Plain spaces never need escaping.

- **Count:** 115 comments in 48 PRs.
  - Separators added: 62 comments in 33 PRs.
  - Separators removed: 53 comments in 20 PRs; 15 of those were next to full-width punctuation.
- **Coverage:**
  - Adding `\\ ` before roles is ALREADY-COVERED (README; rst-cheatsheet).
  - "Remove `\\ ` next to full-width punctuation", "both `\\ ` and `\\` work, prefer `\\ `" and "spaces need no escape" are NEW.

**Examples:**
- Added:
  - Before: `請見\ :ref:\`安裝 IDLE <…>\``
  - After: `請見\\ :ref:\`安裝 IDLE <…>\`` (#1203: single backslash is wrong in PO)
  - Before: `包含一個 :term:\`路徑條目 <path entry>\` 的串列`
  - After: `包含一個\\ :term:\`路徑條目 <path entry>\`\\ 的串列` (#1190)
- Removed:
  - Before: `規格（\\ ``__spec__``\\ ）`
  - After: `規格（``__spec__``）` (#1190)
  - Review #941: 在（除了括號以外的）全形標點符號旁不用放 `\\ `
  - Review #808: 把 `\\ 、\\ ` 都改成 `、`
- Notes:
  - "實際上 `\\ ` 與 `\\` 效果相同…目前專案大多用前者" (#1175)
  - "空白不用 escape" (#820)

## 5. Punctuation

**Rule:**
- Chinese sentences use full-width `，。：；（）`.
- Use `、` to separate enumerated items.
- A trailing `::` becomes `： ::`.
- Keep `...` exactly as in the source (do not convert it to `…`).
- Use 「」 for emphasis quotes. Keep straight `"..."` when the quoted text is a literal value or name.

- **Count:** ~119 comments in 47 PRs.
  - Half-width `()` changed to full-width: 31 comments in 11 PRs.
  - `： ::` fixes: 16 comments in 11 PRs.
  - 「」 added: 8. 「」 reverted to `"…"`: 7.
  - `，` changed to `、`: 5. Ellipsis: 2.
- **Coverage:**
  - Full/half width, parentheses and `： ::` are ALREADY-COVERED.
  - `、` for lists, `...` kept as in the source, and "literal values keep ASCII quotes" are NEW.

**Examples:**
- `中 :：` → `中： ::` (#1149)
- `錯誤時回傳 ``-1``，並無異常設定 (除非…)` → `…並無例外設定（除非…）` (#1149)
- `十六進位，八進位，還有二進位` → `十六進位、八進位，還有二進位` (#1205). Other `、` comments: 宜改頓號 / 改頓號？ (#945)
- `套用「default」動作` → `套用 \"default\" 動作` (#1115). Note: double quotes that wrap untranslated literals stay ASCII (#1108).
- `時鐘每秒只\\ “跳” 50 次` → `只「跳」50 次` (#908)
- `…` → `...` (#1175: "和原文使用相同符號")

## 6. reST roles and inline markup

**Rule:**
- Keep every role, ``literal`` and link intact.
- Translate the *display text* of `:ref:`, `:term:`, `:source:` and `:option:` as `譯文 <target>`.
- Re-add ``…`` markup when the source has it; Poedit does not carry it over.
- Never break the backticks.

- **Count:** ~107 comments in 49 PRs.
  - ``literal`` markup added back: 31 comments in 18 PRs.
  - Role display text translated: 13 comments in 8 PRs.
- **Coverage:**
  - Role preservation and display-text translation are ALREADY-COVERED (rst-cheatsheet).
  - "Re-add ``literal`` markup that is missing in msgstr" and "check that backticks are balanced" are NEW.

**Examples:**
- `:ref:\`keyword <keywords>\`` → `:ref:\`關鍵字 <keywords>\`` (#1175)
- `:ref:\`non-blocking <ssl-nonblocking>\`` → `\\ :ref:\`非阻塞的 <ssl-nonblocking>\`\\ ` (#953)
- `傳遞旗標 strict=False` → `傳遞旗標 ``strict=False``` (#1169: 「程式碼」標記 poedit 不會自動帶上)
- `` `-PY_SSIZE_T_MAX`` `` (unbalanced) → ```` ``-PY_SSIZE_T_MAX`` ```` (#1149)

## 7. Consistency within a file

**Rule:** within one page, the same English term gets the same rendering. Search the existing translations (pogrep / GitHub search) before you coin a new term. Different pages may differ.

- **Count:** 99 comments in 56 PRs.
- **Coverage:** PARTIAL. validation-rules has an "Inconsistent term" check, but nothing says to search the existing translations or that the scope is one page.

**Examples:**
- "這行出現兩個 parse 但翻譯不同" (#921)
- "timeout 前面有翻成「超時」，要選擇其中一個統一用詞" (#953)
- "lookahead / lookbehind 已經在 library/re 中被翻譯成「預查」與「回查」，希望能統一用詞" (#1175)
- Reviewers once used 時間戳 and 時間戳記 in the same file; they asked for one. They also asked for 產生 over 生成, to match the existing text (#1213).
- "單篇文章內盡量統一，不同文章不一樣的話我覺得沒關係" (#921)

## 8. Annotate rare or ambiguous terms with the original English, first occurrence only

**Rule:** if a term has no settled zh_TW translation, could be confused with another term, or would be hard to map back to English, add `譯文 (English)` at its first occurrence on the page only.

- **Count:** 59 comments in 37 PRs.
- **Coverage:** ALREADY-COVERED (README rule 6). Reviewers still enforce it very often, so it is worth a checklist line.

**Examples:**
- `用於降低DoS攻擊的風險` → `用於降低阻斷服務 (DoS) 攻擊的風險` (#1205)
- `就地初始化` → `原地 (in place) 初始化` (#1164)
- `點號參照` → `點號參照 (dotted reference)` (#1126)
- Terms reviewers asked to annotate: pickle, peer, transaction, hook, introspection, magic number, segmentation fault, real-time, finder/loader/importer.
- "原文附註只要在第一次出現的地方就好" (#777, #797; also #828)

## 9. Untranslated English left in msgstr (should translate)

**Rule:** translate ordinary English words and phrases, including role display text and comments inside code samples. Leave identifiers and string literals in code unchanged.

- **Count:** 54 comments in 35 PRs.
- **Coverage:** NEW. The skills list what to *keep*, but not that leftover English is a defect.

**Examples:**
- `以 :ref:\`debug mode <debug-build>\`` → `以\\ :ref:\`偵錯模式 <debug-build>\`\\ ` (#1178)
- `Callable` → `可呼叫` (#905)
- `Application Note` → `應用簡記` (#1079)
- Notes:
  - "displayed text 需翻譯" (#1190)
  - "docstring 應翻譯" (#1050)
  - "目前慣例是 code comment 也需要翻譯" (#1246)
- Counterpoint: An automated review flagged a translated string literal inside a `property()` example (#1222). Translate comments; leave literals in code alone.

## 10. Omissions (missing words, clauses or segments)

**Rule:** every clause, qualifier ("optional", "numeric", "original", "usually") and parenthetical in the source must appear in the msgstr.

- **Count:** 44 comments in 26 PRs.
- **Coverage:** NEW.

**Examples:**
- "(which identifies the rule that's being defined) 這句話好像沒翻譯到", fixed by adding `（用來識別被定義的規則）` (#1175)
- "漏翻第二個 community" (#1203)
- "沒翻到 optional", "漏翻 operands" (#876)
- "原文 'decode to text' 沒有翻譯到" (#1029)
- "`PythonFinalizationError` 這行目前原文有、譯文沒有" (#1010)

## 11. Do not translate (keep English)

**Rule:** keep in English:
- `socket`, `runtime`, `yield`, `token`
- library or module names such as itertools
- literal option values
- words that are really parameter names (`*input_charset*`, `using`, `buffer`, `bytes`)

`pickle` and similar words may be translated only if the original is added.

- **Count:** 38 comments in 31 PRs.
- **Coverage:**
  - PARTIAL. keep-in-english.md covers runtime, pickle, yield, keywords and modules.
  - socket, token, "library names", and "words that refer to a parameter" are NEW.

**Examples:**
- `執行時` → ` runtime` (#1190). "runtime 我們通常就不翻譯" (#1057)
- "socket 應該直接原文就好" (#857, #938)
- "我自己是希望 library name 都不要翻譯" (#950)
- `字元集合` → `*input_charset*` (#989)
- `緩衝` → `buffer` "指 parameter" (#953)
- "yield 和 generate 容易搞混，所以我們 yield 通常不翻或會附註原文" (#876, #916)

## 12. Over-translation (additions not in the source)

**Rule:** do not add explanations, qualifiers or facts that the source does not state (超譯).

- **Count:** 23 comments in 17 PRs.
- **Coverage:** NEW.

**Examples:**
- "「對於整數型別的操作數」原文好像沒有這句" (#876)
- "原文沒有提到「預設參數」" (#1029)
- "它是 generator 沒錯，但會不會補充過多資訊呢？…希望忠實表達原意" (#945)
- "翻譯成「特性」感覺超譯了" → 功能 (#1175)

## 13. Second person: 你, not 您

**Rule:** always address the reader with 你.

- **Count:** 19 comments in 11 PRs.
- **Coverage:** NEW.

**Examples:**
- `若您使用 Linux` → `若你是使用 Linux` (#1203)
- "我們 convention 是統一用「你」不用「您」" (#941)
- "請都把「您」改成「你」" (#770)

## 14. PO and PR mechanics

**Rules:**
- Never edit msgid or its line breaks.
- Run `powrap` after editing.
- Don't just delete `#, fuzzy`: update the translation to match the changed msgid.
- No trailing whitespace and no stray `+` from diffs.
- Don't commit unrelated files.
- Index-only entries start with the English term and put the translation in parentheses.
- Delete commented-out obsolete translations.

- **Count:** 20 comments in 12 PRs, plus several review summaries.
- **Coverage:**
  - msgid and powrap are ALREADY-COVERED.
  - fuzzy handling, the index-entry format, trailing whitespace and unrelated files are NEW.

**Examples:**
- "這個還有差異不能直接刪 fuzzy 標記，要把原文 copy 過去" (#1010)
- "We normally do not modify the original strings (including how it places the line break)" (#1066)
- "數個原文的逗號被改到了，要改回來" (#1149)
- "此行有尾隨空白…" and "delete the `+`" (#1213)
- "看起來你不小心 commit 到這個檔案了" (#1178)
- Index entries: "建議翻譯內容是以原文開頭、後面括號附註譯文，以保持該詞彙在索引表列中的位置" (#860)
- "最後面 comment out 的翻譯可以都刪掉" (#906)

## 15. Code blocks and formulas

**Rule:** copy code blocks and math or formula syntax verbatim. Translate only comments. Use full-width punctuation inside translated comments.

- **Count:** 12 comments in 10 PRs.
- **Coverage:** PARTIAL. rst-cheatsheet says "Only translate comments if needed".

**Examples:**
- "code block 直接將原文複製到譯文部分即可" (#1149)
- "此處公式語法希望還是從原文直接搬過來" (#872)
- `# 去除P的公因數。 (但若m和n互質…)` → `# 去除 P 的公因數。（但若 m 和 n 互質…）` (#1229)
- "註解的標點符號很多沒有改成全形" (#1128)

---

## Terminology enforced by reviewers

Counts are suggestion edits where the rejected form disappears and the required form appears, plus explicit notes. "PRs" is the number of distinct PRs. "Cov" says whether the pair is in `forbidden-terms.md` / `terminology.md` / `validation-rules.md`.

| English | Required zh_TW | Rejected | Count (PRs) | Example PR | Cov |
|---|---|---|---|---|---|
| argument | 引數 | 參數 | 28 (16) | #1149, #1066, #860 | COVERED (terminology.md) |
| return | 回傳 | 傳回 | 21 (9) | #1164, #1097 | **NEW** (only 返回 is listed) |
| you | 你 | 您 | 18 (10) + notes | #1203, #941 | **NEW** |
| support | 支援 | 支持 | 14 (9) | #1175, #855 | COVERED |
| return | 回傳 | 返回 | 13 (9) | #1092, #1074 | COVERED |
| function (programming) | 函式 | 函數 (math only) | 13 (8) | #966, #876 | COVERED |
| call | 呼叫 | 調用 | 13 (8) | #953, #889 | COVERED |
| exception | 例外 | 異常 | 12 (7) | #1164, #1066 | COVERED |
| implement | 實作 | 實現 | 11 (5) | #876, #1066 | COVERED |
| list (Python list) | 串列 | 清單 (OK for a non-Python list) | 9 (6) | #1095, #1076 | **NEW** (conditional rule) |
| protocol | 協定 | 協議 | 9 (4) | #868, #855 | **NEW** as a forbidden term |
| parse | 剖析 (resolve = 解析) | 解析 | 8 (7) | #1147, #908, #1068 | COVERED |
| string | 字串 | 字符串 | 8 (3) | #1074 | COVERED |
| via / through | 透過 | 通過 | 7 (6) | #983, #950 | **NEW** |
| create | 建立 | 創建 | 7 (4) | #953, #860 | COVERED |
| client | 用戶端 (user = 使用者) | 客戶端 | 7 (4) | #1164, #1128, #1074 | **NEW** |
| line (command line, line no.) | 列 (命令列) | 行 (命令行) | 7+5 (4+2) | #1062, #1027, #885 | **NEW** |
| file | 檔案 (document = 文件) | 文件 | 7 (3) | #1068, #860 | **NEW** (only document→文件 listed) |
| default | 預設 | 默認 | 7 (3) | #876 | COVERED |
| set an exception (C API) | 設定例外 | 拋出異常 | 6 (1) | #1164 | **NEW** |
| raise | 引發 | 拋出 / 產生 | 5 (4) + notes | #1074, #828 | **NEW** (only in keep-in-english as a keyword) |
| reference | 參照 | 引用 | 4 (3) | #1147, #867 | COVERED (via glossary) |
| iterate | 疊代 | 迭代 | 4 (3) | #1027, #795 | COVERED |
| statement | 陳述式 | 語句 | 4 (2) | #1095, #966 | COVERED |
| object | 物件 | 對象 | 4 (2) | #1066, #953 | COVERED |
| data | 資料 | 數據 | 4 (2) | #1074, #956 | COVERED |
| blocking / non-blocking | 阻塞 / 非阻塞 | 阻擋 | 4 (2) | #953, #777 | **NEW** |
| pseudo-random | 偽隨機數 | 偽亂數 | 4 (1) | #785 | **NEW** |
| parameter | 參數 | 引數 | 3 (3) | #1095, #1048 | COVERED |
| compatible | 相容 | 兼容 | 3 (3) | #1147, #908 | COVERED |
| code | 程式碼 | 代碼 | 3 (3) | #1071, #983 | COVERED |
| obtain / get | 取得 / 抽取 | 獲取 | 3 (2) | #1190, #1066 | **NEW** |
| user | 使用者 | 用戶 | 3 (2) | #1074 | COVERED |
| setting / configure | 設定 / 配置 | 設置 / 呼叫 | 3 (2) | #1066, #1022 | COVERED |
| interface | 介面 | 接口 | 3 (1) | #1066 | **NEW** |
| hard disk | 磁碟 | 硬盤 | 3 (1) | #1066 | **NEW** |
| escape | 跳脫 | 轉換 / 轉義 | 3 (1) | #1097, #945 | COVERED |
| lookahead / lookbehind | 預查 / 回查 | 預看 | 3 (1) | #1175 | **NEW** |
| section (of a page) | 章節 / 段落 | 部分 | 3 (1) | #767, #983 | **NEW** |
| exit | 結束 | 退出 | 3 (1) | #767 | **NEW** |
| cache | 快取 | 緩存 | 3 (1) | #1092 | COVERED |
| pointer | 指標 | 指針 | 3 (1) | #1164 | COVERED |
| run | 執行 | 運行 / 跑 | notes | #767, #1128 | **NEW** |
| module | 模組 | 模塊 | 2 (2) | #1092, #1071 | COVERED |
| interpret | 直譯 | 解釋 | 2 (2) | #1115, #786 | COVERED |
| instance | 實例 | 實體 | 2 (2) | #1095 | COVERED |
| global | 全域 | 全局 | 2 (2) | #1092, #1027 | COVERED |
| expression | 運算式 | 表達式 | 2 (2) | #1164, #889 | COVERED |
| build | 建置 | 建構 / 構建 | 2 (2) | #1176, #1164 | **NEW** |
| base class | 基底類別 | 基礎類別 | 2 (2) | #1097, #817 | COVERED |
| response | 回應 | 響應 | 2 (2) | #1066, #820 | **NEW** |
| variable / optimize / program | 變數 / 最佳化 / 程式 | 變量 / 優化 / 程序 | 2 each | #1092, #979 | COVERED (程序 is **NEW**) |
| message | 訊息 | 信息 | 2 (1) | #1066, #824 | **NEW** (forbidden-terms maps 信息→資訊 only) |
| boolean | 布林 | 布爾 | 2 (1) | #1066 | COVERED |
| delegate | 委派 | 委託 | 2 (1) | #800 | **NEW** |
| audit event | 稽核事件 | 審計事件 | 2 (1) | #979 | **NEW** |
| entry | 條目 / 項目 (keep consistent) | mixed | 2 (1) + notes | #1074, #836 | **NEW** |
| constructor | 建構函式 | 建構器 | 2 (1) + note | #1066 | **NEW** |
| invoke | 叫用 | 調用 | 1 + notes | #1190, #1066 | COVERED |
| debug | 偵錯 | 除錯 / 調試 | 1 + notes | #1203, #1059 | COVERED (both allowed in skill; reviewers lean 偵錯) |
| signal | 訊號 | 信號 | 1 + note | #921, #860 | **NEW** |
| print | 列印 | 打印 | note | #860 | **CONFLICT**: forbidden-terms says 印出 |
| address | 位址 | 地址 | 1 | #1213 | **NEW** |
| port | 連接埠 | 端口 | 1 | #1066 | **NEW** |
| server | 伺服器 | 服務端 | 1 | #1066 | **NEW** |
| binary | 二進位 | 二進制 | 1 | #1205 | **NEW** |
| custom | 自訂 | 自定 / 自定義 | 1 + note | #1190, #945 | **NEW** |
| byte / character / macro / polymorphism | 位元組 / 字元 / 巨集 / 多型 | 字節 / 字符 / 宏 / 多態 | 1 each | #1076, #876, #1149, #1097 | COVERED (多型 is **NEW**) |
| generate | 產生 | 生成 | 1 + note | #785, #1213 | **NEW** |
| timestamp | 時間戳記 | 時間戳 | 1 + note | #1213 | **NEW** |
| introduce | 引進 / 採納 (not 引入, which is import) | 引入 | 1 + note | #1190 | COVERED |
| flag | 旗標 | 標誌 / 标识 | 2 (2) | #1076, #824 | COVERED |
| process | 行程 | 進程 / 程序 | 1 + notes | #1064, #828 | COVERED |
| package / class | 套件 / 類別 | 包 / 類 | notes | #1022, #876 | COVERED |
| keyword-only | 僅限關鍵字 | 關鍵字 / 只能用關鍵字 | 1 | #1128 | **NEW** |
| session | 工作階段 | 會話 | note | #1066 | **NEW** |
| stream | 串流 | 流 | note | #1029 | **NEW** |
| handler | 處理函式 | 處理器 | notes | #879, #853 | **NEW** |
| wrap | 包裝 | 封裝 (encapsulation) | 1 | #889 | **NEW** |
| context | 情境 | 內容 / 上下文 | notes | #770, #876 | COVERED |
| metadata | 詮釋資料 | 元數據 / 源資訊 | notes | #1190, #1164 | COVERED |
| concurrent | 並行 | 並發 | 1 | #1027 | **NEW** |
| network | 網路 | 網絡 | 1 | #777 | **NEW** |

The terms below are under active discussion; no fixed rendering is enforced yet. Annotate the original instead of forcing a term: token, pattern (模式/樣式), wildcard, frame, property (特性?), serialize, peer (對等/對等端點), cipher, partial function, debug (偵錯 vs 除錯), invoke.

---

## Already covered vs NEW — quick list

| # | Rule | Status |
|---|---|---|
| 1 | Natural phrasing: no English word order, too many 的 or needless 被; check meaning | NEW |
| 2 | Term list / zh_CN replacement (base set) | ALREADY-COVERED |
| 2a | Missing pairs: 傳回→回傳, 拋出→引發 / 設定例外, 通過→透過, 協議→協定, 命令行→命令列, 客戶端→用戶端, 檔案 (file) vs 文件 (document), 串列 vs 清單 rule, 訊息, 獲取→取得, 介面, 磁碟, 位址, 連接埠, 伺服器, 回應, 建置, 阻塞, 執行 (not 運行), 稽核, 委派, 產生 (not 生成), 時間戳記 | NEW |
| 2b | 打印 → 列印 (reviewer) vs 印出 (forbidden-terms.md) | CONFLICT, needs resolving |
| 3 | CJK–Latin space | ALREADY-COVERED |
| 3a | No space next to full-width punctuation (also around markup); no space after 。 or between CJK | PARTIAL / NEW |
| 4 | `\\ ` before roles adjacent to CJK | ALREADY-COVERED |
| 4a | Remove `\\ ` next to `，。、：；）「」`; prefer `\\ ` over `\\`; never a single `\`; spaces need no escape | NEW |
| 5 | Full-width punctuation, full-width parentheses for Chinese content, `： ::` | ALREADY-COVERED |
| 5a | `、` for enumerations; keep `...` as in the source; ASCII quotes for literal values | NEW |
| 6 | Preserve roles; translate display text `譯文 <target>` | ALREADY-COVERED |
| 6a | Re-add missing ``literal`` markup; balanced backticks | NEW |
| 7 | Consistent term within a page; search existing translations first | PARTIAL |
| 8 | Annotate the original at first occurrence only | ALREADY-COVERED |
| 9 | Leftover English is a defect; translate comments in code samples, not string literals | NEW |
| 10 | No omissions (qualifiers, parentheticals, second instances) | NEW |
| 11 | Keep English: runtime, pickle, yield, keywords, modules | ALREADY-COVERED |
| 11a | Keep English: socket, token, library names, words that are parameter names | NEW |
| 12 | No over-translation (超譯) | NEW |
| 13 | 你, never 您 | NEW |
| 14 | Don't touch msgid; powrap | ALREADY-COVERED |
| 14a | Don't just strip fuzzy; no trailing whitespace or stray `+`; no unrelated files; index entries as `English（譯文）`; delete commented-out obsolete entries | NEW |
| 15 | Code and formula copied verbatim; comments get full-width punctuation | PARTIAL |
