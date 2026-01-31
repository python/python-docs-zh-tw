---
name: terminology-check
description: Check and enforce terminology consistency based on project glossary. Identifies zh_CN variants and suggests zh_TW corrections.
metadata:
  short-description: Terminology consistency checker
---

# terminology-check

## Scope
- Check terminology against project glossary
- Identify zh_CN to zh_TW conversion needs
- Track term usage consistency across files
- Suggest standardized translations

## Terminology Sources

### Primary: glossary.po
Official Python glossary translations at project root.

### Secondary: terminology.md
Quick reference at `doc-translate/references/terminology.md`.

### Tertiary: Built-in Mapping
Common zh_CN to zh_TW corrections (from `.scripts/google_translate/utils.py`).

## Forbidden Terms (zh_CN -> zh_TW)

These Simplified Chinese terms MUST be converted:

| Forbidden | Required | English |
|-----------|----------|---------|
| 創建 | 建立 | create |
| 代碼 | 程式碼 | code |
| 信息 | 資訊 | information |
| 模塊 | 模組 | module |
| 標誌 | 旗標 | flag |
| 異常 | 例外 | exception |
| 解釋器 | 直譯器 | interpreter |
| 頭文件 | 標頭檔 | header |
| 對象 | 物件 | object |
| 支持 | 支援 | support |
| 默認 | 預設 | default |
| 兼容 | 相容 | compatible |
| 字符串 | 字串 | string |
| 宏 | 巨集 | macro |
| 描述符 | 描述器 | descriptor |
| 字節 | 位元組 | bytes |
| 緩存 | 快取 | cache |
| 調用 | 呼叫 | call |
| 哈希 | 雜湊 | hash |
| 類型 | 型別 | type |
| 子類 | 子類別 | subclass |
| 實現 | 實作 | implement |
| 數據 | 資料 | data |
| 返回 | 回傳 | return |
| 指針 | 指標 | pointer |
| 字段 | 欄位 | field |
| 擴展 | 擴充 | extension |
| 遞歸 | 遞迴 | recursive |
| 用戶 | 使用者 | user |
| 算法 | 演算法 | algorithm |
| 優化 | 最佳化 | optimize |
| 字符 | 字元 | character |
| 設置 | 設定 | setting |
| 線程 | 執行緒 | thread |
| 進程 | 行程 | process |
| 迭代 | 疊代 | iterate |
| 內存 | 記憶體 | memory |
| 打印 | 印出 | print |
| 異步 | 非同步 | async |
| 調試 | 除錯 | debug |
| 堆棧 | 堆疊 | stack |
| 回調 | 回呼 | callback |
| 公共 | 公開 | public |
| 函數 | 函式 | function |
| 變量 | 變數 | variable |
| 常量 | 常數 | constant |
| 添加 | 新增 | add |
| 轉義 | 跳脫 | escape |
| 基類 | 基底類別 | base class |

## High-Frequency Terms (Keep in English)

These terms should NOT be translated, even if glossary has translations:

```
int, float, str, bytes, bool
list, tuple, dict, set
iterator, generator, iterable
pickle, module, method
True, False, None
```

## Standard Translations

Core Python terms with required zh_TW translations:

| English | Traditional Chinese |
|---------|---------------------|
| abstract base class | 抽象基底類別 |
| annotation | 註釋 |
| argument | 引數 |
| attribute | 屬性 |
| callable | 可呼叫物件 |
| class | 類別 |
| closure | 閉包 |
| context manager | 情境管理器 |
| coroutine | 協程 |
| decorator | 裝飾器 |
| descriptor | 描述器 |
| dictionary | 字典 |
| docstring | 說明字串 |
| exception | 例外 |
| expression | 運算式 |
| function | 函式 |
| generator | 產生器 |
| global | 全域 |
| immutable | 不可變物件 |
| import | 引入 |
| instance | 實例 |
| interpreter | 直譯器 |
| iterable | 可疊代物件 |
| iterator | 疊代器 |
| keyword argument | 關鍵字引數 |
| list comprehension | 串列綜合運算 |
| local | 區域 |
| method | 方法 |
| module | 模組 |
| mutable | 可變物件 |
| namespace | 命名空間 |
| object | 物件 |
| package | 套件 |
| parameter | 參數 |
| positional argument | 位置引數 |
| sequence | 序列 |
| slice | 切片 |
| statement | 陳述式 |
| type | 型別 |
| variable | 變數 |

## Check Process

1. **Extract terms** - Parse msgstr for Chinese phrases and English words
2. **Check forbidden** - Flag any zh_CN variants from the forbidden list
3. **Check consistency** - Compare with other translations of same term
4. **Check glossary** - Verify against official glossary.po
5. **Report issues** - List violations with suggestions

## Output Format

```
=== Terminology Report: library/functions.po ===

FORBIDDEN TERMS (must fix):
  Line 42: "函數" -> "函式" (function)
  Line 78: "返回" -> "回傳" (return)
  Line 156: "對象" -> "物件" (object)

INCONSISTENT TERMS (review):
  "iterator" translated as:
    - "疊代器" (45 occurrences) <- standard
    - "迭代器" (3 occurrences) <- zh_CN variant

Total: 3 forbidden, 1 inconsistent
```

## Related Skills
- `doc-translate` - General translation rules
- `validate-translation` - Comprehensive validation
