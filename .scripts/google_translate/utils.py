MAPPING_ZH_TW_COMMON_TRANSLATION_ERROR = {
    '創建': '建立',  # create
    '代碼': '程式碼',  # code
    '信息': '資訊',  # information
    '模塊': '模組',  # module
    '標誌': '旗標',  # flag
    '異常': '例外',  # exception
    '解釋器': '直譯器',  # interpreter
    '頭文件': '標頭檔',  # header
    '對象': '物件',  # objetc
    '支持': '支援',  # support
    '默認': '預設',  # default
    '兼容': '相容',  # compatible
    '字符串': '字串',  # string
    '宏': '巨集',  # macro
    '描述符': '描述器',  # descriptor
    '字節': '位元組',  # bytes
    '緩存': '快取',  # cache
    '調用': '呼叫',  # call
    '哈希': '雜湊',  # hash
    '類型': '型別',  # type
    '子類': '子類別',  # subclass
    '實現': '實作',  # implement
    '數據': '資料',  # data
    '返回': '回傳',  # return
    '指針': '指標',  # pointer
    '字段': '欄位',  # field
    '擴展': '擴充',  # extension
    '遞歸': '遞迴',  # recursive
    '用戶': '使用者',  # user
    '算法': '演算法',  # algorithm
    '優化': '最佳化',  # optimize
    '字符': '字元',  # character
    '設置': '設定',  # setting/configure
    '線程': '執行緒',  # thread
    '進程': '行程',  # process
    '迭代': '疊代',  # iterate
    '內存': '記憶體',  # memory
    '打印': '印出',  # print
    '異步': '非同步',  # async
    '調試': '除錯',  # debug
    '堆棧': '堆疊',  # stack
    '回調': '回呼',  # callback
    '公共': '公開',  # public
    '函數': '函式',  # function
    '變量': '變數',  # variable
    '常量': '常數',  # constant
    '添加': '新增',  # add
    '基類': '基底類別',  # base class
}


def refine_translations(s: str) -> str:
    for original, target in MAPPING_ZH_TW_COMMON_TRANSLATION_ERROR.items():
        s = s.replace(original, target)
    return s
