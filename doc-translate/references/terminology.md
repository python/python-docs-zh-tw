# 術語表摘錄

以下內容為術語表/翻譯對照摘錄，翻譯時請優先參考此處與 `glossary.po`。

互動式 shell 的預設 Python 提示字元。常見於能在直譯器中以互動方式被執行的程式碼範例。

可以表示：

在一個被縮排的程式碼區塊、在一對匹配的左右定界符（delimiter，例如括號、方括號、花括號或三引號）內部，或是在指定一個裝飾器 (decorator) 之後，要輸入程式碼時，互動式 shell 顯示的預設 Python 提示字元。

The three dots form of the Ellipsis object.

abstract base class（抽象基底類別）
抽象基底類別（又稱為 ABC）提供了一種定義介面的方法，作為 duck-typing（鴨子型別）的補充。其他類似的技術，像是 hasattr()，則顯得笨拙或是帶有細微的錯誤（例如使用魔術方法 (magic method)）。ABC 採用虛擬的 subclass（子類別），它們並不繼承自另一個 class（類別），但仍可被 isinstance() 及 issubclass() 辨識；請參閱 abc 模組的說明文件。Python 有許多內建的 ABC，用於資料結構（在 collections.abc 模組）、數字（在 numbers 模組）、串流（在 io 模組）及 import 尋檢器和載入器（在 importlib.abc 模組）。你可以使用 abc 模組建立自己的 ABC。

annotate function（註釋函式）
A function that can be called to retrieve the annotations of an object. This function is accessible as the __annotate__ attribute of functions, classes, and modules. Annotate functions are a subset of evaluate functions.

annotation（註釋）
一個與變數、class 屬性、函式的參數或回傳值相關聯的標籤。照慣例，它被用來作為 type hint（型別提示）。

在 runtime 的區域變數註釋無法被存取，但全域變數、類別屬性和函式的註釋，分別能夠以對模組、類別和函式呼叫 annotationlib.get_annotations() 來取得。

請參閱 variable annotation、function annotation、PEP 484、PEP 526 和 PEP 649，這些章節皆有此功能的說明。關於註釋的最佳實踐方法也請參閱 註釋 (annotation) 最佳實踐。

argument（引數）
呼叫函式時被傳遞給 function（或 method）的值。引數有兩種：

關鍵字引數 (keyword argument)：在函式呼叫中，以識別字（identifier，例如 name=）開頭的引數，或是以 ** 後面 dictionary（字典）內的值被傳遞的引數。例如，3 和 5 都是以下 complex() 呼叫中的關鍵字引數：

complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
位置引數 (positional argument)：不是關鍵字引數的引數。位置引數可在一個引數列表的起始處出現，和（或）作為 * 之後的 iterable（可疊代物件）中的元素被傳遞。例如，3 和 5 都是以下呼叫中的位置引數：

complex(3, 5)
complex(*(3, 5))
引數會被指定給函式主體中的附名區域變數。關於支配這個指定過程的規則，請參閱Calls章節。在語法上，任何運算式都可以被用來表示一個引數；其評估值會被指定給區域變數。

另請參閱術語表的 parameter（參數）條目、常見問題中的引數和參數之間的差異，以及 PEP 362。

asynchronous context manager（非同步情境管理器）
一個可以控制 async with 陳述式中所見環境的物件，而它是透過定義 __aenter__() 和 __aexit__() method（方法）來控制的。由 PEP 492 引入。

asynchronous generator（非同步產生器）
一個會回傳 asynchronous generator iterator（非同步產生器疊代器）的函式。它看起來像一個以 async def 定義的協程函式 (coroutine function)，但不同的是它包含了 yield 運算式，能生成一系列可用於 async for 迴圈的值。

這個術語通常用來表示一個非同步產生器函式，但在某些情境中，也可能是表示非同步產生器疊代器 (asynchronous generator iterator)。萬一想表達的意思不夠清楚，那就使用完整的術語，以避免歧義。

一個非同步產生器函式可能包含 await 運算式，以及 async for 和 async with 陳述式。

asynchronous generator iterator（非同步產生器疊代器）
一個由 asynchronous generator（非同步產生器）函式所建立的物件。

這是一個 asynchronous iterator（非同步疊代器），當它以 __anext__() method 被呼叫時，會回傳一個可等待物件 (awaitable object)，該物件將執行非同步產生器的函式主體，直到遇到下一個 yield 運算式。

每個 yield 會暫停處理程序，並記住執行狀態（包括區域變數及擱置中的 try 陳述式）。當非同步產生器疊代器以另一個被 __anext__() 回傳的可等待物件有效地回復時，它會從停止的地方繼續執行。請參閱 PEP 492 和 PEP 525。

asynchronous iterable（非同步可疊代物件）
一個物件，它可以在 async for 陳述式中被使用。必須從它的 __aiter__() method 回傳一個 asynchronous iterator（非同步疊代器）。由 PEP 492 引入。

asynchronous iterator（非同步疊代器）
一個實作 __aiter__() 和 __anext__() method 的物件。__anext__() 必須回傳一個 awaitable（可等待物件）。async for 會解析非同步疊代器的 __anext__() method 所回傳的可等待物件，直到它引發 StopAsyncIteration 例外。由 PEP 492 引入。

atomic operation
An operation that appears to execute as a single, indivisible step: no other thread can observe it half-done, and its effects become visible all at once. Python does not guarantee that high-level statements are atomic (for example, x += 1 performs multiple bytecode operations and is not atomic). Atomicity is only guaranteed where explicitly documented. See also race condition and data race.

attached thread state
A thread state that is active for the current OS thread.

When a thread state is attached, the OS thread has access to the full Python C API and can safely invoke the bytecode interpreter.

Unless a function explicitly notes otherwise, attempting to call the C API without an attached thread state will result in a fatal error or undefined behavior. A thread state can be attached and detached explicitly by the user through the C API, or implicitly by the runtime, including during blocking C calls and by the bytecode interpreter in between calls.

On most builds of Python, having an attached thread state implies that the caller holds the GIL for the current interpreter, so only one OS thread can have an attached thread state at a given moment. In free-threaded builds of Python, threads can concurrently hold an attached thread state, allowing for true parallelism of the bytecode interpreter.

attribute（屬性）
一個與某物件相關聯的值，該值大多能透過使用點分隔運算式 (dotted expression) 的名稱被參照。例如，如果物件 o 有一個屬性 a，則該屬性能以 o.a 被參照。

如果一個物件允許，給予該物件一個名稱不是由Names (identifiers and keywords)所定義之識別符 (identifier) 的屬性是有可能的，例如使用 setattr()。像這樣的屬性將無法使用點分隔運算式來存取，而是需要使用 getattr() 來取得它。

awaitable（可等待物件）
一個可以在 await 運算式中被使用的物件。它可以是一個 coroutine（協程），或是一個有 __await__() method 的物件。另請參閱 PEP 492。

BDFL
Benevolent Dictator For Life（終身仁慈獨裁者），又名 Guido van Rossum，Python 的創造者。

binary file（二進位檔案）
一個能夠讀取和寫入 bytes-like objects（類位元組串物件）的 file object（檔案物件）。二進位檔案的例子有：以二進位模式（'rb'、'wb' 或 'rb+'）開啟的檔案、sys.stdin.buffer、sys.stdout.buffer，以及 io.BytesIO 和 gzip.GzipFile 實例。

另請參閱 text file（文字檔案），它是一個能夠讀取和寫入 str 物件的檔案物件。

borrowed reference（借用參照）
在 Python 的 C API 中，借用參照是一個對物件的參照，其中使用該物件的程式碼並不擁有這個參照。如果該物件被銷毀，它會成為一個迷途指標 (dangling pointer)。例如，一次垃圾回收 (garbage collection) 可以移除對物件的最後一個 strong reference（強參照），而將該物件銷毀。

對 borrowed reference 呼叫 Py_INCREF() 以將它原地 (in-place) 轉換為 strong reference 是被建議的做法，除非該物件不能在最後一次使用借用參照之前被銷毀。Py_NewRef() 函式可用於建立一個新的 strong reference。

bytes-like object（類位元組串物件）
一個支援緩衝協定 (Buffer Protocol)且能夠匯出 C-contiguous 緩衝區的物件。這包括所有的 bytes、bytearray 和 array.array 物件，以及許多常見的 memoryview 物件。類位元組串物件可用於處理二進位資料的各種運算；這些運算包括壓縮、儲存至二進位檔案和透過 socket（插座）發送。

有些運算需要二進位資料是可變的。說明文件通常會將這些物件稱為「可讀寫的類位元組串物件」。可變緩衝區的物件包括 bytearray，以及 bytearray 的 memoryview。其他的運算需要讓二進位資料被儲存在不可變物件（「唯讀的類位元組串物件」）中；這些物件包括 bytes，以及 bytes 物件的 memoryview。

bytecode（位元組碼）
Python 的原始碼會被編譯成位元組碼，它是 Python 程式在 CPython 直譯器中的內部表示法。該位元組碼也會被暫存在 .pyc 檔案中，以便第二次執行同一個檔案時能夠更快速（可以不用從原始碼重新編譯為位元組碼）。這種「中間語言 (intermediate language)」據說是運行在一個 virtual machine（虛擬機器）上，該虛擬機器會執行與每個位元組碼對應的機器碼 (machine code)。要注意的是，位元組碼理論上是無法在不同的 Python 虛擬機器之間運作的，也不能在不同版本的 Python 之間保持穩定。

位元組碼的指令列表可以在 dis 模組的說明文件中找到。

callable（可呼叫物件）
一個 callable 是可以被呼叫的物件，呼叫時可能以下列形式帶有一組引數（請見 argument）：

callable(argument1, argument2, argumentN)
一個 function 與其延伸的 method 都是 callable。一個有實作 __call__() 方法的 class 之實例也是個 callable。

callback（回呼）
作為引數被傳遞的一個副程式 (subroutine) 函式，會在未來的某個時間點被執行。

class（類別）
一個用於建立使用者定義物件的模板。Class 的定義通常會包含 method 的定義，這些 method 可以在 class 的實例上進行操作。

class variable（類別變數）
一個在 class 中被定義，且應該只能在 class 層次（意即不是在 class 的實例中）被修改的變數。

closure variable（閉包變數）
從外部作用域中定義且從巢狀作用域參照的自由變數，不是於 runtime 從全域或內建命名空間解析。可以使用 nonlocal 關鍵字明確定義以允許寫入存取，或者如果僅需讀取變數則隱式定義即可。

例如在下面程式碼中的 inner 函式中，x 和 print 都是自由變數，但只有 x 是閉包變數：

def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    return inner
由於 codeobject.co_freevars 屬性（儘管名稱如此，但它僅包含閉包變數的名稱，而不是列出所有參照的自由變數），當預期含義是特指閉包變數時，有時候甚至也會使用更通用的自由變數一詞。

complex number（複數）
一個我們熟悉的實數系統的擴充，在此所有數字都會被表示為一個實部和一個虛部之和。虛數就是虛數單位（-1 的平方根）的實數倍，此單位通常在數學中被寫為 i，在工程學中被寫為 j。Python 內建了對複數的支援，它是用後者的記法來表示複數；虛部會帶著一個後綴的 j 被編寫，例如 3+1j。若要將 math 模組內的工具等效地用於複數，請使用 cmath 模組。複數的使用是一個相當進階的數學功能。如果你沒有察覺到對它們的需求，那麼幾乎能確定你可以安全地忽略它們。

concurrency（並行性）
The ability of a computer program to perform multiple tasks at the same time. Python provides libraries for writing programs that make use of different forms of concurrency. asyncio is a library for dealing with asynchronous tasks and coroutines. threading provides access to operating system threads and multiprocessing to operating system processes. Multi-core processors can execute threads and processes on different CPU cores at the same time (see parallelism).

concurrent modification
When multiple threads modify shared data at the same time. Concurrent modification without proper synchronization can cause race conditions, and might also trigger a data race, data corruption, or both.

context（情境）
This term has different meanings depending on where and how it is used. Some common meanings:

The temporary state or environment established by a context manager via a with statement.

The collection of key­value bindings associated with a particular contextvars.Context object and accessed via ContextVar objects. Also see context variable.

一個 contextvars.Context 物件。另請參閱 current context。

context management protocol（情境管理協定）
由 with 陳述式所呼叫的 __enter__() 和 __exit__() 方法。另請參閱 PEP 343。

context manager（情境管理器）
An object which implements the context management protocol and controls the environment seen in a with statement. See PEP 343.

context variable（情境變數）
A variable whose value depends on which context is the current context. Values are accessed via contextvars.ContextVar objects. Context variables are primarily used to isolate state between concurrent asynchronous tasks.

contiguous（連續的）
如果一個緩衝區是 C-contiguous 或是 Fortran contiguous，則它會確切地被視為是連續的。零維 (zero-dimensional) 的緩衝區都是 C 及 Fortran contiguous。在一維 (one-dimensional) 陣列中，各項目必須在記憶體中彼此相鄰地排列，而其索引順序是從零開始遞增。在多維的 (multidimensional) C-contiguous 陣列中，按記憶體位址的順序瀏覽各個項目時，最後一個索引的變化最快。然而，在 Fortran contiguous 陣列中，第一個索引的變化最快。

coroutine（協程）
協程是副程式 (subroutine) 的一種更為廣義的形式。副程式是在某個時間點被進入並在另一個時間點被退出。協程可以在許多不同的時間點被進入、退出和回復。它們能夠以 async def 陳述式被實作。另請參閱 PEP 492。

coroutine function（協程函式）
一個回傳 coroutine（協程）物件的函式。一個協程函式能以 async def 陳述式被定義，並可能會包含 await、async for 和 async with 關鍵字。這些關鍵字由 PEP 492 引入。

CPython
Python 程式語言的標準實作 (canonical implementation)，被發布在 python.org 上。「CPython」這個術語在必要時被使用，以區分此實作與其它語言的實作，例如 Jython 或 IronPython。

current context
The context (contextvars.Context object) that is currently used by ContextVar objects to access (get or set) the values of context variables. Each thread has its own current context. Frameworks for executing asynchronous tasks (see asyncio) associate each task with a context which becomes the current context whenever the task starts or resumes execution.

cyclic isolate
A subgroup of one or more objects that reference each other in a reference cycle, but are not referenced by objects outside the group. The goal of the cyclic garbage collector is to identify these groups and break the reference cycles so that the memory can be reclaimed.

data race
A situation where multiple threads access the same memory location concurrently, at least one of the accesses is a write, and the threads do not use any synchronization to control their access. Data races lead to non-deterministic behavior and can cause data corruption. Proper use of locks and other synchronization primitives prevents data races. Note that data races can only happen in native code, but that native code might be exposed in a Python API. See also race condition and thread-safe.

deadlock
A situation in which two or more tasks (threads, processes, or coroutines) wait indefinitely for each other to release resources or complete actions, preventing any from making progress. For example, if thread A holds lock 1 and waits for lock 2, while thread B holds lock 2 and waits for lock 1, both threads will wait indefinitely. In Python this often arises from acquiring multiple locks in conflicting orders or from circular join/await dependencies. Deadlocks can be avoided by always acquiring multiple locks in a consistent order. See also lock and reentrant.

decorator（裝飾器）
一個函式，它會回傳另一個函式，通常它會使用 @wrapper 語法，被應用為一種函式的變換 (function transformation)。裝飾器的常見範例是 classmethod() 和 staticmethod()。

裝飾器語法只是語法糖。以下兩個函式定義在語義上是等效的：

def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...
Class 也存在相同的概念，但在那裡比較不常用。關於裝飾器的更多內容，請參閱函式定義和 class 定義的說明文件。

descriptor（描述器）
任何定義了 __get__()、__set__() 或 __delete__() method 的物件。當一個 class 屬性是一個描述器時，它的特殊連結行為會在屬性查找時被觸發。通常，使用 a.b 來取得、設定或刪除某個屬性時，會在 a 的 class 字典中查找名稱為 b 的物件，但如果 b 是一個描述器，則相對應的描述器 method 會被呼叫。對描述器的理解是深入理解 Python 的關鍵，因為它們是許多功能的基礎，這些功能包括函式、method、屬性 (property)、class method、靜態 method，以及對 super class（父類別）的參照。

關於描述器 method 的更多資訊，請參閱實作描述器或描述器使用指南。

dictionary（字典）
一個關聯陣列 (associative array)，其中任意的鍵會被對映到值。鍵可以是任何帶有 __hash__() 和 __eq__() method 的物件。在 Perl 中被稱為雜湊 (hash)。

dictionary comprehension（字典綜合運算）
一種緊密的方法，用來處理一個可疊代物件中的全部或部分元素，並將處理結果以一個字典回傳。results = {n: n ** 2 for n in range(10)} 會產生一個字典，它包含了鍵 n 對映到值 n ** 2。請參閱Displays for lists, sets and dictionaries。

dictionary view（字典檢視）
從 dict.keys()、dict.values() 及 dict.items() 回傳的物件被稱為字典檢視。它們提供了字典中項目的動態檢視，這表示當字典有變動時，該檢視會反映這些變動。若要強制將字典檢視轉為完整的 list（串列），須使用 list(dictview)。請參閱字典視圖物件。

docstring（說明字串）
一個在 class、函式或模組中，作為第一個運算式出現的字串文本。雖然它在套件執行時會被忽略，但它會被編譯器辨識，並被放入所屬 class、函式或模組的 __doc__ 屬性中。由於說明字串可以透過內省 (introspection) 來瀏覽，因此它是物件的說明文件存放的標準位置。

duck-typing（鴨子型別）
一種程式設計風格，它不是藉由檢查一個物件的型別來確定它是否具有正確的介面；取而代之的是，method 或屬性會單純地被呼叫或使用。（「如果它看起來像一隻鴨子而且叫起來像一隻鴨子，那麼它一定是一隻鴨子。」）因為強調介面而非特定型別，精心設計的程式碼能讓多形替代 (polymorphic substitution) 來增進它的靈活性。鴨子型別要避免使用 type() 或 isinstance() 進行測試。（但是請注意，鴨子型別可以用抽象基底類別 (abstract base class) 來補充。）然而，它通常會採用 hasattr() 測試，或是 EAFP 程式設計風格。

dunder（雙底線）
一個非正式的縮寫，代表「雙底線 (double underscore)」，當談論到特殊方法時使用。例如，__init__ 通常被叫做 "dunder init"。

EAFP
Easier to ask for forgiveness than permission.（請求寬恕比請求許可更容易。）這種常見的 Python 編碼風格會先假設有效的鍵或屬性的存在，並在該假設被推翻時再捕獲例外。這種乾淨且快速的風格，其特色是存在許多的 try 和 except 陳述式。該技術與許多其他語言（例如 C）常見的 LBYL 風格形成了對比。

evaluate function（求值函式）
A function that can be called to evaluate a lazily evaluated attribute of an object, such as the value of type aliases created with the type statement.

expression（運算式）
一段可以被評估並求值的語法。換句話說，一個運算式就是文字、名稱、屬性存取、運算子或函式呼叫等運算式元件的累積，而這些元件都能回傳一個值。與許多其他語言不同的是，並非所有的 Python 語言構造都是運算式。另外有一些 statement（陳述式）不能被用作運算式，例如 while。賦值 (assignment) 也是陳述式，而不是運算式。

extension module（擴充模組）
一個以 C 或 C++ 編寫的模組，它使用 Python 的 C API 來與核心及使用者程式碼進行互動。

f-string（f 字串）
f-strings（f 字串）
以 f 或 F 為前綴的字串文本通常被稱為「f 字串」，它是格式化的字串文本的縮寫。另請參閱 PEP 498。

file object（檔案物件）
一個讓使用者透過檔案導向 (file-oriented) API（如 read() 或 write() 等 method）來操作底層資源的物件。根據檔案物件被建立的方式，它能夠協調對真實磁碟檔案或是其他類型的儲存器或通訊裝置（例如標準輸入／輸出、記憶體內緩衝區、socket（插座）、管線 (pipe) 等）的存取。檔案物件也被稱為類檔案物件 (file-like object) 或串流 (stream)。

實際上，有三種檔案物件：原始的二進位檔案、緩衝的二進位檔案和文字檔案。它們的介面在 io 模組中被定義。建立檔案物件的標準方法是使用 open() 函式。

file-like object（類檔案物件）
file object（檔案物件）的同義字。

filesystem encoding and error handler（檔案系統編碼和錯誤處理函式）
Python 所使用的一種編碼和錯誤處理函式，用來解碼來自作業系統的位元組，以及將 Unicode 編碼到作業系統。

檔案系統編碼必須保證能成功解碼所有小於 128 的位元組。如果檔案系統編碼無法提供此保證，則 API 函式會引發 UnicodeError。

sys.getfilesystemencoding() 和 sys.getfilesystemencodeerrors() 函式可用於取得檔案系統編碼和錯誤處理函式。

filesystem encoding and error handler（檔案系統編碼和錯誤處理函式）會在 Python 啟動時由 PyConfig_Read() 函式來配置：請參閱 filesystem_encoding，以及 PyConfig 的成員 filesystem_errors。

另請參閱 locale encoding（區域編碼）。

finder（尋檢器）
一個物件，它會嘗試為正在被 import 的模組尋找 loader（載入器）。

有兩種類型的尋檢器：元路徑尋檢器 (meta path finder) 會使用 sys.meta_path，而路徑項目尋檢器 (path entry finder) 會使用 sys.path_hooks。

請參閱 尋檢器 (Finder) 與載入器 (Loader) 和 importlib 以了解更多細節。

floor division（向下取整除法）
向下無條件捨去到最接近整數的數學除法。向下取整除法的運算子是 //。例如，運算式 11 // 4 的計算結果為 2，與 float（浮點數）真除法所回傳的 2.75 不同。請注意，(-11) // 4 的結果是 -3，因為是 -2.75 被向下無條件捨去。請參閱 PEP 238。

free threading（自由執行緒）
為一種執行緒模型，多個執行緒可以在同一直譯器中同時運行 Python 位元組碼。這與全域直譯器鎖形成對比，後者一次只允許一個執行緒執行 Python 位元組碼。請參閱 PEP 703。

free variable（自由變數）
Formally, as defined in the language execution model, a free variable is any variable used in a namespace which is not a local variable in that namespace. See closure variable for an example. Pragmatically, due to the name of the codeobject.co_freevars attribute, the term is also sometimes used as a synonym for closure variable.

function（函式）
一連串的陳述式，它能夠向呼叫者回傳一些值。它也可以被傳遞零個或多個引數，這些引數可被使用於函式本體的執行。另請參閱 parameter（參數）、method（方法），以及函式定義章節。

function annotation（函式註釋）
函式參數或回傳值的一個 annotation（註釋）。

函式註釋通常被使用於型別提示：例如，這個函式預期會得到兩個 int 引數，並會有一個 int 回傳值：

def sum_two_numbers(a: int, b: int) -> int:
   return a + b
函式註釋的語法在函式定義章節有詳細解釋。

請參閱 variable annotation 和 PEP 484，皆有此功能的描述。關於註釋的最佳實踐方法，另請參閱 註釋 (annotation) 最佳實踐。

__future__
future 陳述式：from __future__ import <feature>，會指示編譯器使用那些在 Python 未來的發布版本中將成為標準的語法或語義，來編譯目前的模組。而 __future__ 模組則記錄了 feature（功能）可能的值。透過 import 此模組並對其變數求值，你可以看見一個新的功能是何時首次被新增到此語言中，以及它何時將會（或已經）成為預設的功能：

import __future__
__future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
garbage collection（垃圾回收）
當記憶體不再被使用時，將其釋放的過程。Python 執行垃圾回收，是透過參照計數 (reference counting)，以及一個能夠檢測和中斷參照循環 (reference cycle) 的循環垃圾回收器 (cyclic garbage collector) 來完成。垃圾回收器可以使用 gc 模組對其進行控制。

generator（產生器）
一個會回傳 generator iterator（產生器疊代器）的函式。它看起來像一個正常的函式，但不同的是它包含了 yield 運算式，能產生一系列的值，這些值可用於 for 迴圈，或是以 next() 函式，每次檢索其中的一個值。

這個術語通常用來表示一個產生器函式，但在某些情境中，也可能是表示產生器疊代器。萬一想表達的意思不夠清楚，那就使用完整的術語，以避免歧義。

generator iterator（產生器疊代器）
一個由 generator（產生器）函式所建立的物件。

每個 yield 會暫停處理程序，並記住執行狀態（包括區域變數及擱置中的 try 陳述式）。當產生器疊代器回復時，它會從停止的地方繼續執行（與那些每次呼叫時都要重新開始的函式有所不同）。

generator expression（產生器運算式）
一個會回傳疊代器的運算式。它看起來像一個正常的運算式，後面接著一個 for 子句，該子句定義了迴圈變數、範圍以及一個選擇性的 if 子句。該組合運算式會為外層函式產生多個值：

sum(i*i for i in range(10))         # 平方之和 0, 1, 4, ... 81
285
generic function（泛型函式）
一個由多個函式組成的函式，該函式會對不同的型別實作相同的運算。呼叫期間應該使用哪種實作，是由調度演算法 (dispatch algorithm) 來決定。

另請參閱 single dispatch（單一調度）術語表條目、functools.singledispatch() 裝飾器和 PEP 443。

generic type（泛型型別）
一個能夠被參數化 (parameterized) 的 type（型別）；通常是一個 容器型別，像是 list 和 dict。它被用於型別提示和註釋。

詳情請參閱泛型別名型別、PEP 483、PEP 484、PEP 585 和 typing 模組。

GIL
請參閱 global interpreter lock（全域直譯器鎖）。

global interpreter lock（全域直譯器鎖）
CPython 直譯器所使用的機制，用以確保每次都只有一個執行緒能執行 Python 的 bytecode（位元組碼）。透過使物件模型（包括關鍵的內建型別，如 dict）自動地避免並行存取 (concurrent access) 的危險，此機制可以簡化 CPython 的實作。鎖定整個直譯器，會使直譯器更容易成為多執行緒 (multi-threaded)，但代價是會犧牲掉多處理器的機器能夠提供的一大部分平行性 (parallelism)。

然而，有些擴充模組，無論是標準的或是第三方的，它們被設計成在執行壓縮或雜湊等計算密集 (computationally intensive) 的任務時，可以解除 GIL。另外，在執行 I/O 時，GIL 總是會被解除。

從 Python 3.13 開始可以使用 --disable-gil 建置設定來停用 GIL。使用此選項建立 Python 後，必須使用 -X gil=0 來執行程式碼，或者設定 PYTHON_GIL=0 環境變數後再執行程式碼。此功能可以提高多執行緒應用程式的效能，並使多核心 CPU 的高效使用變得更加容易。有關更多詳細資訊，請參閱 PEP 703。

In prior versions of Python's C API, a function might declare that it requires the GIL to be held in order to use it. This refers to having an attached thread state.

global state
Data that is accessible throughout a program, such as module-level variables, class variables, or C static variables in extension modules. In multi-threaded programs, global state shared between threads typically requires synchronization to avoid race conditions and data races.

hash-based pyc（雜湊架構的 pyc）
一個位元組碼 (bytecode) 暫存檔，它使用雜湊值而不是對應原始檔案的最後修改時間，來確定其有效性。請參閱Cached bytecode invalidation。

hashable（可雜湊的）
如果一個物件有一個雜湊值，該值在其生命週期中永不改變（它需要一個 __hash__() method），且可與其他物件互相比較（它需要一個 __eq__() method），那麼它就是一個可雜湊物件。比較結果為相等的多個可雜湊物件，它們必須擁有相同的雜湊值。

可雜湊性 (hashability) 使一個物件可用作 dictionary（字典）的鍵和 set（集合）的成員，因為這些資料結構都在其內部使用了雜湊值。

大多數的 Python 不可變內建物件都是可雜湊的；可變的容器（例如 list 或 dictionary）並不是；而不可變的容器（例如 tuple（元組）和 frozenset），只有當它們的元素是可雜湊的，它們本身才是可雜湊的。若物件是使用者自定 class 的實例，則這些物件會被預設為可雜湊的。它們在互相比較時都是不相等的（除非它們與自己比較），而它們的雜湊值則是衍生自它們的 id()。

IDLE
Python 的 Integrated Development and Learning Environment（整合開發與學習環境）。IDLE --- Python 編輯器與 shell 是一個基本的編輯器和直譯器環境，它和 Python 的標準發行版本一起被提供。

immortal（不滅）
不滅物件 (Immortal objects) 是 PEP 683 引入的 CPython 實作細節。

如果一個物件是不滅的，它的參照計數永遠不會被修改，因此在直譯器運行時它永遠不會被釋放。例如，True 和 None 在 CPython 中是不滅的。

Immortal objects can be identified via sys._is_immortal(), or via PyUnstable_IsImmortal() in the C API.

immutable（不可變物件）
一個具有固定值的物件。不可變物件包括數字、字串和 tuple（元組）。這類物件是不能被改變的。如果必須儲存一個不同的值，則需要建立一個新的物件。它們在需要恆定雜湊值的地方扮演重要的角色，例如 dictionary 中的一個鍵。不可變物件本質上是執行緒安全的，因為它們的狀態在建立後無法被修改，從而消除了對不當同步的並行修改的疑慮。

import path（引入路徑）
一個位置（或路徑項目）的列表，而那些位置就是在 import 模組時，會被 path based finder（基於路徑的尋檢器）搜尋模組的位置。在 import 期間，此位置列表通常是來自 sys.path，但對於子套件 (subpackage) 而言，它也可能是來自父套件的 __path__ 屬性。

importing（引入）
一個過程。一個模組中的 Python 程式碼可以透過此過程，被另一個模組中的 Python 程式碼使用。

importer（引入器）
一個能夠尋找及載入模組的物件；它既是 finder（尋檢器）也是 loader（載入器）物件。

interactive（互動的）
Python 有一個互動式直譯器，這表示你可以在直譯器的提示字元輸入陳述式和運算式，立即執行它們並且看到它們的結果。只要啟動 python，不需要任何引數（可能藉由從你的電腦的主選單選擇它）。這是測試新想法或檢查模組和包的非常強大的方法（請記住help(x)）。更多互動式模式相關資訊請見 互動模式。

interpreted（直譯的）
Python 是一種直譯語言，而不是編譯語言，不過這個區分可能有些模糊，因為有位元組碼 (bytecode) 編譯器的存在。這表示原始檔案可以直接被運行，而不需明確地建立另一個執行檔，然後再執行它。直譯語言通常比編譯語言有更短的開發／除錯週期，不過它們的程式通常也運行得較慢。另請參閱 interactive（互動的）。

interpreter shutdown（直譯器關閉）
當 Python 直譯器被要求關閉時，它會進入一個特殊階段，在此它逐漸釋放所有被配置的資源，例如模組和各種關鍵內部結構。它也會多次呼叫垃圾回收器 (garbage collector)。這能夠觸發使用者自定的解構函式 (destructor) 或弱引用的回呼 (weakref callback)，並執行其中的程式碼。在關閉階段被執行的程式碼會遇到各種例外，因為它所依賴的資源可能不再有作用了（常見的例子是函式庫模組或是警告機制）。

直譯器關閉的主要原因，是 __main__ 模組或正被運行的腳本已經執行完成。

iterable（可疊代物件）
一種能夠一次回傳一個其中成員的物件。可疊代物件的例子包括所有的序列型別（像是 list、str 和 tuple）和某些非序列型別，像是 dict、檔案物件，以及你所定義的任何 class 物件，只要那些 class 有實作 sequence（序列）語意的 __iter__() 或是 __getitem__() method，該物件就是可疊代物件。

可疊代物件可用於 for 迴圈和許多其他需要一個序列的地方 (zip()、map()...)。當一個可疊代物件作為引數被傳遞給內建函式 iter() 時，它會為該物件回傳一個疊代器。此疊代器適用於針對一組值進行一遍 (one pass) 運算。使用疊代器時，通常不一定要呼叫 iter() 或自行處理疊代器物件。for 陳述式會自動地為你處理這些事，它會建立一個暫時性的未命名變數，用於在迴圈期間保有該疊代器。另請參閱 iterator（疊代器）、sequence（序列）和 generator（產生器）。

iterator（疊代器）
一個表示資料流的物件。重複地呼叫疊代器的 __next__() method（或是將它傳遞給內建函式 next()）會依序回傳資料流中的各項目。當不再有資料時，則會引發 StopIteration 例外。此時，該疊代器物件已被用盡，而任何對其 __next__() method 的進一步呼叫，都只會再次引發 StopIteration。疊代器必須有一個 __iter__() method，它會回傳疊代器物件本身，所以每個疊代器也都是可疊代物件，且可以用於大多數適用其他可疊代物件的場合。一個明顯的例外，是嘗試多遍疊代 (multiple iteration passes) 的程式碼。一個容器物件（像是 list）在每次你將它傳遞給 iter() 函式或在 for 迴圈中使用它時，都會產生一個全新的疊代器。使用疊代器嘗試此事（多遍疊代）時，只會回傳在前一遍疊代中被用過的、同一個已被用盡的疊代器物件，使其看起來就像一個空的容器。

在疊代器型別文中可以找到更多資訊。

CPython 並不是始終如一地都會檢查「疊代器有定義 __iter__()」這個規定。另請注意，free-threading（自由執行緒） CPython 不保證疊代器操作的執行緒安全 行為。

key function（鍵函式）
鍵函式或理序函式 (collation function) 是一個可呼叫 (callable) 函式，它會回傳一個用於排序 (sorting) 或定序 (ordering) 的值。例如，locale.strxfrm() 被用來產生一個了解區域特定排序慣例的排序鍵。

Python 中的許多工具，都接受以鍵函式來控制元素被定序或分組的方式。它們包括 min()、max()、sorted()、list.sort()、heapq.merge()、heapq.nsmallest()、heapq.nlargest() 和 itertools.groupby()。

有幾種方法可以建立一個鍵函式。例如，str.casefold() method 可以作為不分大小寫排序的鍵函式。或者，一個鍵函式也可以從 lambda 運算式被建造，例如 lambda r: (r[0], r[2])。另外，operator.attrgetter()、operator.itemgetter() 和 operator.methodcaller() 為三個鍵函式的建構函式 (constructor)。關於如何建立和使用鍵函式的範例，請參閱如何排序。

keyword argument（關鍵字引數）
請參閱 argument（引數）。

lambda
由單一 expression（運算式）所組成的一個匿名行內函式 (inline function)，於該函式被呼叫時求值。建立 lambda 函式的語法是 lambda [parameters]: expression

LBYL
Look before you leap.（三思而後行。）這種編碼風格會在進行呼叫或查找之前，明確地測試先決條件。這種風格與 EAFP 方式形成對比，且它的特色是會有許多 if 陳述式的存在。

在一個多執行緒環境中，LBYL 方式有在「三思」和「後行」之間引入競爭條件 的風險。例如以下程式碼 if key in mapping: return mapping[key]，如果另一個執行緒在測試之後但在查找之前，從 mapping 中移除了 key，則該程式碼就會失效。這個問題可以用鎖或使用 EAFP 編碼方式來解決。另請參閱執行緒安全。

lexical analyzer（詞法分析器）
tokenizer 的正式名稱；請參閱 token。

list（串列）
一個 Python 內建的 sequence （序列）。儘管它的名字是 list，它其實更類似其他語言中的一個陣列 (array) 而較不像一個鏈結串列 (linked list)，因為存取元素的時間複雜度是 O(1)。

list comprehension（串列綜合運算）
一種用來處理一個序列中的全部或部分元素，並將處理結果以一個 list 回傳的簡要方法。result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0] 會產生一個字串 list，其中包含 0 到 255 範圍內，所有偶數的十六進位數 (0x..)。if 子句是選擇性的。如果省略它，則 range(256) 中的所有元素都會被處理。

lock（鎖）
A synchronization primitive that allows only one thread at a time to access a shared resource. A thread must acquire a lock before accessing the protected resource and release it afterward. If a thread attempts to acquire a lock that is already held by another thread, it will block until the lock becomes available. Python's threading module provides Lock (a basic lock) and RLock (a reentrant lock). Locks are used to prevent race conditions and ensure thread-safe access to shared data. Alternative design patterns to locks exist such as queues, producer/consumer patterns, and thread-local state. These primitives help prevent race conditions and coordinate thread execution. See also deadlock, and reentrant.

loader（載入器）
一個能夠載入模組的物件。它必須定義 exec_module() 和 create_module() 方法以實作 Loader 介面。載入器通常是被 finder（尋檢器）回傳。更多細節請參閱：

尋檢器 (Finder) 與載入器 (Loader)

importlib.abc.Loader

PEP 302

locale encoding（區域編碼）
在 Unix 上，它是 LC_CTYPE 區域設定的編碼。它可以用 locale.setlocale(locale.LC_CTYPE, new_locale) 來設定。

在 Windows 上，它是 ANSI 碼頁（code page，例如 "cp1252"）。

在 Android 和 VxWorks 上，Python 使用 "utf-8" 作為區域編碼。

locale.getencoding() 可以用來取得區域編碼。

也請參考 filesystem encoding and error handler。

magic method（魔術方法）
special method（特殊方法）的一個非正式同義詞。

mapping（對映）
一個容器物件，它支援任意鍵的查找，且能實作 abstract base classes（抽象基底類別）中，collections.abc.Mapping 或 collections.abc.MutableMapping 所指定的 method。範例包括 dict、collections.defaultdict、collections.OrderedDict 和 collections.Counter。

meta path finder（元路徑尋檢器）
一種經由搜尋 sys.meta_path 而回傳的 finder（尋檢器）。元路徑尋檢器與路徑項目尋檢器 (path entry finder) 相關但是不同。

關於元路徑尋檢器實作的 method，請參閱 importlib.abc.MetaPathFinder。

metaclass（元類別）
一種 class 的 class。Class 定義過程會建立一個 class 名稱、一個 class dictionary（字典），以及一個 base class（基底類別）的列表。Metaclass 負責接受這三個引數，並建立該 class。大多數的物件導向程式語言會提供一個預設的實作。Python 的特別之處在於它能夠建立自訂的 metaclass。大部分的使用者從未需要此工具，但是當需要時，metaclass 可以提供強大且優雅的解決方案。它們已被用於記錄屬性存取、增加執行緒安全性、追蹤物件建立、實作單例模式 (singleton)，以及許多其他的任務。

更多資訊可以在Metaclasses章節中找到。

method（方法）
一個在 class 本體內被定義的函式。如果 method 作為其 class 實例的一個屬性被呼叫，則它將會得到該實例物件成為它的第一個 argument（引數）（此引數通常被稱為 self）。請參閱 function（函式）和 nested scope（巢狀作用域）。

method resolution order（方法解析順序）
方法解析順序是在查找某個成員的過程中，base class（基底類別）被搜尋的順序。關於 Python 自 2.3 版直譯器所使用的演算法細節，請參閱 Python 2.3 方法解析順序。

module（模組）
一個擔任 Python 程式碼的組織單位 (organizational unit) 的物件。模組有一個命名空間，它包含任意的 Python 物件。模組是藉由 importing 的過程，被載入至 Python。

另請參閱 package（套件）。

module spec（模組規格）
一個命名空間，它包含用於載入模組的 import 相關資訊。它是 importlib.machinery.ModuleSpec 的一個實例。

另請參閱 模組規格。

MRO
請參閱 method resolution order（方法解析順序）。

mutable（可變物件）
An object with state that is allowed to change during the course of the program. In multi-threaded programs, mutable objects that are shared between threads require careful synchronization to avoid race conditions. See also immutable, thread-safe, and concurrent modification.

named tuple（附名元組）
術語「named tuple（附名元組）」是指從 tuple 繼承的任何型別或 class，且它的可索引 (indexable) 元素也可以用附名屬性來存取。這些型別或 class 也可以具有其他的特性。

有些內建型別是 named tuple，包括由 time.localtime() 和 os.stat() 回傳的值。另一個例子是 sys.float_info：

sys.float_info[1]                   # 以索引存取
1024
sys.float_info.max_exp              # 以欄位名稱存取
1024
isinstance(sys.float_info, tuple)   # 屬於 tuple 型別
True
有些 named tuple 是內建型別（如上例）。或者，一個 named tuple 也可以從一個正規的 class 定義來建立，只要該 class 是繼承自 tuple，且定義了附名欄位 (named field) 即可。這類的 class 可以手工編寫、可以繼承自 typing.NamedTuple 來建立，也可以使用工廠函式 (factory function) collections.namedtuple() 來建立。後者技術也增加了一些額外的 method，這些 method 可能是在手寫或內建的 named tuple 中，無法找到的。

namespace（命名空間）
變數被儲存的地方。命名空間是以 dictionary（字典）被實作。有區域的、全域的及內建的命名空間，而在物件中（在 method 中）也有巢狀的命名空間。命名空間藉由防止命名衝突，來支援模組化。例如，函式 builtins.open 和 os.open() 是透過它們的命名空間來區分彼此。命名空間也藉由明確地區分是哪個模組在實作一個函式，來增進可讀性及可維護性。例如，寫出 random.seed() 或 itertools.islice() 明確地表示，這些函式分別是由 random 和 itertools 模組在實作。

namespace package（命名空間套件）
一個 package（套件），它只能作為子套件 (subpackage) 的一個容器。命名空間套件可能沒有實體的表示法，而且具體來說它們不像是一個 regular package（正規套件），因為它們並沒有 __init__.py 這個檔案。

命名空間套件允許數個可獨立安裝的套件擁有一個共同的父套件。除此之外，建議使用 regular package。

更多資訊，請參閱 PEP 420 和 命名空間套件。

另請參閱 module（模組）。

native code
Code that is compiled to machine instructions and runs directly on the processor, as opposed to code that is interpreted or runs in a virtual machine. In the context of Python, native code typically refers to C, C++, Rust or Fortran code in extension modules that can be called from Python. See also extension module.

nested scope（巢狀作用域）
能夠參照外層定義 (enclosing definition) 中的變數的能力。舉例來說，一個函式如果是在另一個函式中被定義，則它便能夠參照外層函式中的變數。請注意，在預設情況下，巢狀作用域僅適用於參照，而無法用於賦值。區域變數能在最內層作用域中讀取及寫入。同樣地，全域變數是在全域命名空間中讀取及寫入。nonlocal 容許對外層作用域進行寫入。

new-style class（新式類別）
一個舊名，它是指現在所有的 class 物件所使用的 class 風格。在早期的 Python 版本中，只有新式 class 才能使用 Python 較新的、多樣的功能，像是 __slots__、描述器 (descriptor)、屬性 (property)、__getattribute__()、class method（類別方法）和 static method（靜態方法）。

non-deterministic
Behavior where the outcome of a program can vary between executions with the same inputs. In multi-threaded programs, non-deterministic behavior often results from race conditions where the relative timing or interleaving of threads affects the result. Proper synchronization using locks and other synchronization primitives helps ensure deterministic behavior.

object（物件）
具有狀態（屬性或值）及被定義的行為（method）的任何資料。它也是任何 new-style class（新式類別）的最終 base class（基底類別）。

optimized scope（最佳化作用域）
A scope where target local variable names are reliably known to the compiler when the code is compiled, allowing optimization of read and write access to these names. The local namespaces for functions, generators, coroutines, comprehensions, and generator expressions are optimized in this fashion. Note: most interpreter optimizations are applied to all scopes, only those relying on a known set of local and nonlocal variable names are restricted to optimized scopes.

optional module（可選模組）
An extension module that is part of the standard library, but may be absent in some builds of CPython, usually due to missing third-party libraries or because the module is not available for a given platform.

See 可選模組的需求 for a list of optional modules that require third-party libraries.

package（套件）
一個 Python 的 module（模組），它可以包含子模組 (submodule) 或是遞迴的子套件 (subpackage)。技術上而言，套件就是具有 __path__ 屬性的一個 Python 模組。

另請參閱 regular package（正規套件）和 namespace package（命名空間套件）。

parallelism
Executing multiple operations at the same time (e.g. on multiple CPU cores). In Python builds with the global interpreter lock (GIL), only one thread runs Python bytecode at a time, so taking advantage of multiple CPU cores typically involves multiple processes (e.g. multiprocessing) or native extensions that release the GIL. In free-threaded Python, multiple Python threads can run Python code simultaneously on different cores.

parameter（參數）
在 function（函式）或 method 定義中的一個命名實體 (named entity)，它指明該函式能夠接受的一個 argument（引數），或在某些情況下指示多個引數。共有有五種不同的參數類型：

positional-or-keyword（位置或關鍵字）：指明一個可以按照位置或是作為關鍵字引數被傳遞的引數。這是參數的預設類型，例如以下的 foo 和 bar：

def func(foo, bar=None): ...
positional-only（僅限位置）：指明一個只能按照位置被提供的引數。在函式定義的參數列表中包含一個 / 字元，就可以在該字元前面定義僅限位置參數，例如以下的 posonly1 和 posonly2：

def func(posonly1, posonly2, /, positional_or_keyword): ...
keyword-only（僅限關鍵字）：指明一個只能以關鍵字被提供的引數。在函式定義的參數列表中，包含一個任意數量位置參數 (var-positional parameter) 或是單純的 * 字元，就可以在其後方定義僅限關鍵字參數，例如以下的 kw_only1 和 kw_only2：

def func(arg, *, kw_only1, kw_only2): ...
var-positional（任意數量位置）：指明一串能以任意序列被提供的位置引數（在已被其他參數接受的任何位置引數之外）。這類參數是透過在其參數名稱字首加上 * 來定義的，例如以下的 args：

def func(*args, **kwargs): ...
var-keyword（任意數量關鍵字）：指明可被提供的任意數量關鍵字引數（在已被其他參數接受的任何關鍵字引數之外）。這類參數是透過在其參數名稱字首加上 ** 來定義的，例如上面範例中的 kwargs。

參數可以指明引數是選擇性的或必需的，也可以為一些選擇性的引數指定預設值。

另請參閱術語表的 argument（引數）條目、常見問題中的引數和參數之間的差異、inspect.Parameter class、函式定義章節，以及 PEP 362。

path entry（路徑項目）
在 import path（引入路徑）中的一個位置，而 path based finder （基於路徑的尋檢器）會參考該位置來尋找要 import 的模組。

path entry finder（路徑項目尋檢器）
被 sys.path_hooks 中的一個可呼叫物件 (callable)（意即一個 path entry hook）所回傳的一種 finder，它知道如何以一個 path entry定位模組。

關於路徑項目尋檢器實作的 method，請參閱 importlib.abc.PathEntryFinder。

path entry hook（路徑項目鉤）
在 sys.path_hooks 列表中的一個可呼叫物件 (callable)，若它知道如何在一個特定的 path entry 中尋找模組，則會回傳一個 path entry finder（路徑項目尋檢器）。

path based finder（基於路徑的尋檢器）
預設的元路徑尋檢器 (meta path finder) 之一，它會在一個 import path 中搜尋模組。

path-like object（類路徑物件）
一個表示檔案系統路徑的物件。類路徑物件可以是一個表示路徑的 str 或 bytes 物件，或是一個實作 os.PathLike 協定的物件。透過呼叫 os.fspath() 函式，一個支援 os.PathLike 協定的物件可以被轉換為 str 或 bytes 檔案系統路徑；而 os.fsdecode() 及 os.fsencode() 則分別可用於確保 str 及 bytes 的結果。由 PEP 519 引入。

PEP
Python Enhancement Proposal（Python 增強提案）。PEP 是一份設計說明文件，它能為 Python 社群提供資訊，或是描述 Python 的一個新功能或該功能的程序和環境。PEP 應該要提供簡潔的技術規範以及被提案功能的運作原理。

PEP 的存在目的，是要成為重大新功能的提案、社群中關於某個問題的意見收集，以及已納入 Python 的設計決策的記錄，這些過程的主要機制。PEP 的作者要負責在社群內建立共識並記錄反對意見。

請參閱 PEP 1。

portion（部分）
在單一目錄中的一組檔案（也可能儲存在一個 zip 檔中），這些檔案能對一個命名空間套件 (namespace package) 有所貢獻，如同 PEP 420 中的定義。

positional argument（位置引數）
請參閱 argument（引數）。

provisional API（暫行 API）
暫行 API 是指，從標準函式庫的向後相容性 (backwards compatibility) 保證中，故意被排除的 API。雖然此類介面，只要它們被標示為暫行的，理論上並不會有重大的變更，但如果核心開發人員認為有必要，也可能會出現向後不相容的變更（甚至包括移除該介面）。這種變更並不會無端地產生——只有 API 被納入之前未察覺的嚴重基本缺陷被揭露時，它們才會發生。

即使對於暫行 API，向後不相容的變更也會被視為「最後的解決方案」——對於任何被發現的問題，仍然會盡可能找出一個向後相容的解決方案。

這個過程使得標準函式庫能隨著時間不斷進化，而避免耗費過長的時間去鎖定有問題的設計錯誤。請參閱 PEP 411 了解更多細節。

provisional package（暫行套件）
請參閱 provisional API（暫行 API）。

Python 3000
Python 3.x 系列版本的暱稱（很久以前創造的，當時第 3 版的發布是在遙遠的未來。）也可以縮寫為「Py3k」。

Pythonic（Python 風格的）
一個想法或一段程式碼，它應用了 Python 語言最常見的慣用語，而不是使用其他語言常見的概念來實作程式碼。例如，Python 中常見的一種習慣用法，是使用一個 for 陳述式，對一個可疊代物件的所有元素進行迴圈。許多其他語言並沒有這種類型的架構，所以不熟悉 Python 的人有時會使用一個數值計數器來代替：

for i in range(len(food)):
    print(food[i])
相較之下，以下方法更簡潔、更具有 Python 風格：

for piece in food:
    print(piece)
qualified name（限定名稱）
一個「點分隔名稱」，它顯示從一個模組的全域作用域到該模組中定義的 class、函式或 method 的「路徑」，如 PEP 3155 中的定義。對於頂層的函式和 class 而言，限定名稱與其物件名稱相同：

class C:
    class D:
        def meth(self):
            pass

C.__qualname__
'C'
C.D.__qualname__
'C.D'
C.D.meth.__qualname__
'C.D.meth'
當用於引用模組時，完全限定名稱 (fully qualified name) 是表示該模組的完整點分隔路徑，包括任何的父套件，例如 email.mime.text：

import email.mime.text
email.mime.text.__name__
'email.mime.text'
race condition
A condition of a program where the its behavior depends on the relative timing or ordering of events, particularly in multi-threaded programs. Race conditions can lead to non-deterministic behavior and bugs that are difficult to reproduce. A data race is a specific type of race condition involving unsynchronized access to shared memory. The LBYL coding style is particularly susceptible to race conditions in multi-threaded code. Using locks and other synchronization primitives helps prevent race conditions.

reference count（參照計數）
對於一個物件的參照次數。當一個物件的參照計數下降到零時，它會被解除配置 (deallocated)。有些物件是「不滅的 (immortal)」並擁有不會被改變的參照計數，也因此永遠不會被解除配置。參照計數通常在 Python 程式碼中看不到，但它卻是 CPython 實作的一個關鍵元素。程式設計師可以呼叫 getrefcount() 函式來回傳一個特定物件的參照計數。

在 CPython 中，參照計數不被視為穩定或明確定義的值；對物件的參照數量，以及該數量如何受到 Python 程式碼的影響，在不同版本之間可能會有所不同。

regular package（正規套件）
一個傳統的 package（套件），例如一個包含 __init__.py 檔案的目錄。

另請參閱 namespace package（命名空間套件）。

reentrant
A property of a function or lock that allows it to be called or acquired multiple times by the same thread without causing errors or a deadlock.

For functions, reentrancy means the function can be safely called again before a previous invocation has completed, which is important when functions may be called recursively or from signal handlers. Thread-unsafe functions may be non-deterministic if they're called reentrantly in a multithreaded program.

For locks, Python's threading.RLock (reentrant lock) is reentrant, meaning a thread that already holds the lock can acquire it again without blocking. In contrast, threading.Lock is not reentrant - attempting to acquire it twice from the same thread will cause a deadlock.

另請參閱 lock 和 deadlock。

REPL
「read-eval-print 迴圈 (read–eval–print loop)」的縮寫，是互動式直譯器 shell 的另一個名稱。

__slots__
在 class 內部的一個宣告，它藉由預先宣告實例屬性的空間，以及消除實例 dictionary（字典），來節省記憶體。雖然該技術很普遍，但它有點難以正確地使用，最好保留給那種在一個記憶體關鍵 (memory-critical) 的應用程式中存在大量實例的罕見情況。

sequence（序列）
一個 iterable（可疊代物件），它透過 __getitem__() special method（特殊方法），使用整數索引來支援高效率的元素存取，並定義了一個 __len__() method 來回傳該序列的長度。一些內建序列型別包括 list、str、tuple 和 bytes。請注意，雖然 dict 也支援 __getitem__() 和 __len__()，但它被視為對映 (mapping) 而不是序列，因為其查找方式是使用任意的 hashable 鍵，而不是整數。

抽象基底類別 (abstract base class) collections.abc.Sequence 定義了一個更加豐富的介面，並不僅止於 __getitem__() 和 __len__()，還增加了 count()、index()、__contains__() 和 __reversed__()。實作此擴充介面的型別，可以使用 register() 被明確地註冊。更多關於序列方法的文件，請見常見序列操作。

set comprehension（集合綜合運算）
一種緊密的方法，用來處理一個可疊代物件中的全部或部分元素，並將處理結果以一個 set 回傳。results = {c for c in 'abracadabra' if c not in 'abc'} 會產生一個字串 set：{'r', 'd'}。請參閱Displays for lists, sets and dictionaries。

single dispatch（單一調度）
generic function（泛型函式）調度的一種形式，在此，實作的選擇是基於單一引數的型別。

slice（切片）
一個物件，它通常包含一段 sequence（序列）的某一部分。建立一段切片的方法是使用下標符號 (subscript notation) []，若要給出多個數字，則在數字之間使用冒號，例如 variable_name[1:3:5]。在括號（下標）符號的內部，會使用 slice 物件。

soft deprecated（軟性棄用）
被軟性棄用的 API 代表不應再用於新程式碼中，但在現有程式碼中繼續使用它仍會是安全的。API 仍會以文件記錄並會被測試，但不會被繼續改進。

與正常棄用不同，軟性棄用沒有刪除 API 的規劃，也不會發出警告。

請參閱 PEP 387：軟性棄用。

special method（特殊方法）
一種會被 Python 自動呼叫的 method，用於對某種型別執行某種運算，例如加法。這種 method 的名稱會在開頭和結尾有兩個下底線。Special method 在Special method names中有詳細說明。

標準函式庫
包含套件、模組和擴充模組的集合，它們是作為官方 Python 直譯器套件的一部分來發行。該集合的成員可能會因平台、可用的系統函式庫或其他條件而有所不同。相關文件可以在 Python 標準函式庫 (Standard Library) 中找到。

請參閱 sys.stdlib_module_names 以取得所有可能的標準函式庫模組名稱的列表。

statement（陳述式）
陳述式是一個套組（suite，一個程式碼「區塊」）中的一部分。陳述式可以是一個 expression（運算式），或是含有關鍵字（例如 if、while 或 for）的多種結構之一。

static type checker（靜態型別檢查器）
會讀取 Python 程式碼並分析的外部工具，能夠找出錯誤，像是使用了不正確的型別。另請參閱型別提示 (type hints) 以及 typing 模組。

stdlib（標準函式庫）
standard library 的縮寫。

strong reference（強參照）
在 Python 的 C API 中，強參照是對物件的參照，該物件為持有該參照的程式碼所擁有。建立參照時透過呼叫 Py_INCREF() 來獲得強參照、刪除參照時透過 Py_DECREF() 釋放強參照。

Py_NewRef() 函式可用於建立一個對物件的強參照。通常，在退出強參照的作用域之前，必須在該強參照上呼叫 Py_DECREF() 函式，以避免洩漏一個參照。

另請參閱 borrowed reference（借用參照）。

synchronization primitive
A basic building block for coordinating (synchronizing) the execution of multiple threads to ensure thread-safe access to shared resources. Python's threading module provides several synchronization primitives including Lock, RLock, Semaphore, Condition, Event, and Barrier. Additionally, the queue module provides multi-producer, multi-consumer queues that are especially useful in multithreaded programs. These primitives help prevent race conditions and coordinate thread execution. See also lock.

t-string（t 字串）
t-strings（t 字串）
以 t 或 T 為前綴的字串文本通常被稱為「t 字串」，它是模板化的字串文本的縮寫。

text encoding（文字編碼）
Python 中的字串是一個 Unicode 編碼位置 (code point) 的序列（範圍在 U+0000 -- U+10FFFF 之間）。若要儲存或傳送一個字串，它必須被序列化為一個位元組序列。

將一個字串序列化為位元組序列，稱為「編碼」，而從位元組序列重新建立該字串則稱為「解碼 (decoding)」。

有多種不同的文字序列化編解碼器 (codecs)，它們被統稱為「文字編碼」。

text file（文字檔案）
一個能夠讀取和寫入 str 物件的一個 file object（檔案物件）。通常，文字檔案實際上是存取位元組導向的資料流 (byte-oriented datastream) 並會自動處理 text encoding（文字編碼）。文字檔案的例子有：以文字模式（'r' 或 'w'）開啟的檔案、sys.stdin、sys.stdout 以及 io.StringIO 的實例。

另請參閱 binary file（二進位檔案），它是一個能夠讀取和寫入類位元組串物件 (bytes-like object) 的檔案物件。

thread state
The information used by the CPython runtime to run in an OS thread. For example, this includes the current exception, if any, and the state of the bytecode interpreter.

Each thread state is bound to a single OS thread, but threads may have many thread states available. At most, one of them may be attached at once.

An attached thread state is required to call most of Python's C API, unless a function explicitly documents otherwise. The bytecode interpreter only runs under an attached thread state.

Each thread state belongs to a single interpreter, but each interpreter may have many thread states, including multiple for the same OS thread. Thread states from multiple interpreters may be bound to the same thread, but only one can be attached in that thread at any given moment.

See Thread State and the Global Interpreter Lock for more information.

thread-safe
A module, function, or class that behaves correctly when used by multiple threads concurrently. Thread-safe code uses appropriate synchronization primitives like locks to protect shared mutable state, or is designed to avoid shared mutable state entirely. In the free-threaded build, built-in types like dict, list, and set use internal locking to make many operations thread-safe, although thread safety is not necessarily guaranteed. Code that is not thread-safe may experience race conditions and data races when used in multi-threaded programs.

token
原始碼的小單位，由 詞法分析器 （也稱為 tokenizer）產生。名稱、數字、字串、運算子、換行符號等都以 token 表示。

tokenize 模組公開了 Python 的詞法分析器。token 模組包含各種 token 類型的資訊。

triple-quoted string（三引號內字串）
由三個雙引號 (") 或單引號 (') 的作為邊界的一個字串。雖然它們並沒有提供異於單引號字串的任何額外功能，但基於許多原因，它們仍是很有用的。它們讓你可以在字串中包含未跳脫 (unescaped) 的單引號和雙引號，而且它們不需使用連續字元 (continuation character) 就可以跨越多行，這使得它們在編寫說明字串時特別有用。

type（型別）
一個 Python 物件的型別決定了它是什麼類型的物件；每個物件都有一個型別。一個物件的型別可以用它的 __class__ 屬性來存取，或以 type(obj) 來檢索。

type alias（型別別名）
一個型別的同義詞，透過將型別指定給一個識別符 (identifier) 來建立。

型別別名對於簡化型別提示 (type hint) 很有用。例如：

def remove_gray_shades(
        colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass
可以寫成這樣，更具有可讀性：

Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass
請參閱 typing 和 PEP 484，有此功能的描述。

type hint（型別提示）
一種 annotation（註釋），它指定一個變數、一個 class 屬性或一個函式的參數或回傳值的預期型別。

型別提示是選擇性的，而不是被 Python 強制的，但它們對靜態型別檢查器 (static type checkers)很有用，並能協助 IDE 完成程式碼的補全 (completion) 和重構 (refactoring)。

全域變數、class 屬性和函式（不含區域變數）的型別提示，都可以使用 typing.get_type_hints() 來存取。

請參閱 typing 和 PEP 484，有此功能的描述。

universal newlines（通用換行字元）
一種解譯文字流 (text stream) 的方式，會將以下所有的情況識別為一行的結束：Unix 行尾慣例 '\n'、Windows 慣例 '\r\n' 和舊的 Macintosh 慣例 '\r'。請參閱 PEP 278 和 PEP 3116，以及用於 bytes.splitlines() 的附加用途。

variable annotation（變數註釋）
一個變數或 class 屬性的 annotation（註釋）。

註釋變數或 class 屬性時，賦值是選擇性的：

class C:
    field: 'annotation'
變數註釋通常用於型別提示 (type hint)：例如，這個變數預期會取得 int（整數）值：

count: int = 0
變數註釋的語法在註釋賦值陳述式章節有詳細的解釋。

請參閱 function annotation（函式註釋）、PEP 484 和 PEP 526，皆有此功能的描述。關於註釋的最佳實踐方法，另請參閱 註釋 (annotation) 最佳實踐。

virtual environment（虛擬環境）
一個協作隔離 (cooperatively isolated) 的執行環境，能讓 Python 的使用者和應用程式得以安裝和升級 Python 發佈套件，而不會對同一個系統上運行的其他 Python 應用程式的行為產生干擾。

另請參閱 venv。

virtual machine（虛擬機器）
一部完全由軟體所定義的電腦 (computer)。Python 的虛擬機器會執行由 bytecode（位元組碼）編譯器所發出的位元組碼。

walrus operator（海象運算子）
A light-hearted way to refer to the assignment expression operator := because it looks a bit like a walrus if you turn your head.

Zen of Python（Python 之禪）
Python 設計原則與哲學的列表，其內容有助於理解和使用此語言。此列表可以透過在互動式提式字元後輸入「import this」來找到它。

原文	翻譯	說明
access	存取（勿用「訪問」）
approximate	近似
argument	引數
attribute	屬性
boolean	boolean、布林
call	呼叫（invoke 可譯為「叫用」、「呼叫」）
callback	回呼
child	子代、下代
cipher	密碼
circular reference	循環參照
class	類別
condition	條件
contributor	貢獻者
coroutine	協程
current	目前（勿用「當前」）
deprecated	已棄用
dictionary	dictionary、字典
document	文件（勿用「文檔」）
element	元素
evaluate	給值 / 計算
exception	例外
expression	運算式（但 regular expression 翻成「正規表示式」）
finalizing / finalize	最終化
flag	旗標
float	float、浮點數
function	函式
global	全域
helper	幫助函式、輔助函式
identity	識別性
import	import（不翻譯）、引入
index	索引
instance	實例
int	int、整數
introduce	引進
interpreter	直譯器
invoke	叫用（勿譯為「調用」）
iterate	疊代
iteration	疊代
level	階 / 層級 / 層
library	函式庫
list	list、串列
local	區域
loop	迴圈
method	method、方法
metadata	詮釋資料
mock	mock
module	module、模組
object	物件
operand	運算元
operator	運算子
parameter	參數
parent	父- / 上代
parse	剖析
parser	剖析器
patch	patch
policy	政策 / 原則
prompt	提示字元
regular expression	正規表示式
return	回傳
resolve	解析
runtime	runtime（不翻譯）
set	set、集合
signature	簽名
spec	規格
specification	規格
statement	陳述式
type	型別
visit	瀏覽
