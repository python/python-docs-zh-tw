=======================================
Python 官方說明文件臺灣繁體中文翻譯計畫
=======================================

.. image:: https://badgen.now.sh/badge/chat/on%20Telegram/blue
   :target: https://t.me/PyDocTW
   :alt: Join Chat on Telegram

本 GitHub repository 含有 Python 官方說明文件的 zh_TW 翻譯。實際的翻譯內容\
在這個 repository 裡以 Python 的穩定發行版本作為 branch 名稱，請參考 3.7 等
branch 以查看目前的翻譯內容。此 master branch 則為專案的貢獻說明。

您可以在 https://python-doc-tw.github.io/ 瀏覽目前翻譯的成果。目前以
Python 3.7 為翻譯的對象，**暫時不考慮 Python 2.7 的翻譯工作**。未來有新的
Python 發行版本時，也將會將翻譯滾動至新的版本。

想問問題、認識翻譯同好，歡迎加入 Telegram 聊天室 `t.me/PyDocTW`_

.. _t.me/PyDocTW: https://t.me/PyDocTW

.. contents:: **目錄 Table of Contents**

授權與 License
==============

以下為 Documentation Contribution Agreement，說明文件貢獻協議，請在貢獻以前\
務必詳讀以下內容。原文後附有中文翻譯，但譯文不保證完全正確，請以原文為準。

Documentation Contribution Agreement
------------------------------------

NOTE REGARDING THE LICENSE FOR TRANSLATIONS: Python's documentation is
maintained using a global network of volunteers. By posting this
project on Transifex, GitHub, and other public places, and inviting
you to participate, we are proposing an agreement that you will
provide your improvements to Python's documentation or the translation
of Python's documentation for the PSF's use under the CC0 license
(available at
https://creativecommons.org/publicdomain/zero/1.0/legalcode). In
return, you may publicly claim credit for the portion of the
translation you contributed and if your translation is accepted by the
PSF, you may (but are not required to) submit a patch including an
appropriate annotation in the Misc/ACKS or TRANSLATORS file. Although
nothing in this Documentation Contribution Agreement obligates the PSF
to incorporate your textual contribution, your participation in the
Python community is welcomed and appreciated.

You signify acceptance of this agreement by submitting your work to
the PSF for inclusion in the documentation.

中文翻譯
~~~~~~~~

請注意此予翻譯專案的授權：Python 的說明文件是以全球的志工社群來維護。透過張貼\
此專案在 Transifex、GitHub 以及其他公眾場合，以及邀請您參與，我們向您提出一個\
協議：您必須將您對於 Python 說明文件或是 Python 說明文件翻譯的貢獻以 CC0\
（請參考 https://creativecommons.org/publicdomain/zero/1.0/legalcode）的方式\
授權給 PSF 使用。您可以公開地聲明您所貢獻翻譯的部分，並且如果您的翻譯被 PSF
採用，您可以（但並不須要）送出一個修改，其包含在 Misc/ACKS 或是 TRANSLATORS
檔案裡增加合適的注釋。雖然這個說明文件貢獻協議並沒有說明 PSF 有義務納入您的\
文本貢獻，您在 Python 社群的參與是受歡迎且受感激的。

您在對 PSF 送出說明文件貢獻的同時，即表示同意上述的協議。


參加翻譯
========

如何參加翻譯
------------

實際的翻譯即為修改 po 檔，流程遵照標準的 `GitHub Flow
<https://guides.github.com/introduction/flow/>`_，並且在翻譯任何部份以前新增\
一個 issue 並且指定給自己，讓大家知道您正在翻譯該部分。詳細的步驟如下：

- `新增一個 issue <https://github.com/python/python-docs-zh-tw/issues>`_ 並
  assign 給自己，如：「翻譯 tutorial/introduction.po」
- 在 GitHub 上 fork 此專案
- 將您的 fork clone 一份到本機端
- 新增一個 branch，所有新的變更將在這個 branch 上完成
- 修改 po 檔的內容（參考下面的段落）
- commit 您所修改的內容並且 push 到 GitHub
- 對本專案發出 *Pull Request*

編輯 po 檔的方式主要可以分為兩種，以 Transifex 作為工具或是使用其他翻譯工具：

1. 使用 Transifex 作為翻譯工具（不建議）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

您可以註冊 Transifex 帳號並申請加入官方的 `Transifex 專案
<https://www.transifex.com/python-doc/python-newest>`_，並且在上面\
編輯您所要翻譯的頁面，並且在您本機上透過 command line 從此專案的 clone 的\
根目錄位置執行以下指令：

.. code-block:: bash

  $ ./txpull <po 檔的路徑>

此指令會需要 PyPI 上的 ``transifex-client`` 和 ``poindent``，|gettext|_、
``tac`` 等指令。這個小工具可以幫您把您在 Transifex 上針對特定檔案的翻譯 pull
下來，並且修正換行格式的錯誤。您在使用 txpull 以後就可以 commit 以及 push 了。

.. |gettext| replace:: ``gettext``
.. _gettext: https://www.gnu.org/software/gettext/

2. 使用其他翻譯工具（建議）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

您可以使用以下工具在本機端翻譯 po 檔內容：

- 推薦：`poedit <https://www.poedit.net/>`_
- gted
- gtranslator
- lokalize
- betterpoeditor
- 適當模式底下的 vim 或 emacs
- Vé on Android
- 可能還有更多其他的

編輯完檔案以後，請執行以下指令以確保檔案的換行格式一致（需要安裝
|poindent|_ ：``pip install poindent``）：

.. |poindent| replace:: ``poindent``
.. _poindent: https://pypi.org/project/poindent/

.. code-block:: bash

  $ poindent <po 檔的路徑>

執行完 ``poindent`` 以後即可 commit、push 等。


要翻譯哪些東西
--------------

最簡單的貢獻方式就是更新 *fuzzy entries*，讓翻譯的內容保持與最新版本的文件\
同步。請參考 `尋找 fuzzy entries`_ 段落。

此外，當前的目標為完成 **Tutorial** 的翻譯，因此在 ``tutorial/`` 底下的所有
po 檔皆為首要的翻譯對象。您也可以幫忙校對已經翻譯過的內容。


翻譯守則
========

#. 譯文應兼顧前後文大意。

#. 中文句使用全形標點符號；英文句維持半形的標點符號。

   例如：「」（）、，。

   例如：Python is supported by Python Software Foundation (PSF).

#. 中英文交雜時要插入空白；符號英文間不用。

   例如：使用 CPU 運算、使用「CPU」運算

#. 專有名詞應該參考 `術語表 Glossary`_ 裡翻譯方式。

#. 專有名詞可以選擇不翻譯。

   例如：CPU、Unicode

#. 在翻譯名稱不常用或不確定的情形，宜用括號註解或直接保留原文。單頁只要首次\
   出現有註解即可。

   例如：正規表示式 (regular expression)

   例如：Network News Transfer Protocol、Portable Network Graphics
   （可攜式網路圖形）

#. 務必保留 reStructuredText 格式（如：超連結名稱）

#. po 檔單行不應超過 79 字元寬度（可以使用 |poindent|_ 來確保格式）

#. 高頻詞保留原文。因為翻譯後不一定能較好理解市面上 Python 的文章。 這些高頻詞\
   在 Glossary 中的譯文仍保持原文，並加註市面上的翻譯。

   例如：``int``、``float``、``str``、``bytes``、``list``、``tuple``、
   ``dict``、``set``、``iterator``、``generator``、``iterable``


括號的使用
----------

如果括號中的文字包含中文，使用全形括號；如果括號中只有英文，使用半形括號並\
比照英文的形式加入前後文的空白。

例如：

- list（串列）是 Python 中很常見的資料型別。
- 在本情況使用 ``zip(*[iter(x)]*n)`` 是很常見的情況（Python 慣例）。
- 在超文件標示語言 (HTML) 中應注意跳脫符號。

rST 語法注意事項
----------------

- ``:xxx:`...``` 即為 rST 的語法，應該在譯文中保留。
- rST 諸多語法需要保留前後的空白。在中文裡，該空白可以用 :literal:`\\\  \ `
  來取代，製造一個沒有寬度的分隔符號。

  例如：

  .. code-block:: rst

    For more information, please see :ref:`detail-instruction`.

  翻譯為

  .. code-block:: rst

    更多資訊請參考\ :ref:`detail-instruction`\ 。

- 超連結語法該要在譯文中保留原字串。

  例如：

  .. code-block:: rst

    `Documentation bugs`_ on the Python issue tracker

  應更改為

  .. code-block:: rst

    Python issue tracker 上\ `文件相關的錯誤 <Documentation bugs_>`_

  才能正確顯示為「Python issue tracker 上\ `文件相關的錯誤 <#>`_」，連結與\
  前文才不會有多餘的空白。

- 舉例中有程式碼時，前一段經常為 ``::`` 結尾，此記號\ `具有特殊意義
  <http://www.sphinx-doc.org/en/stable/rest.html#source-code>`_，除了該段落\
  結尾為冒號外，也代表下段縮排為程式碼。翻譯時應改為全型冒號，並\ **增加以**
  ``::`` **開頭的新段落**。

  例如：

  .. code-block:: rst

    Here is a code example::

      import sys
      print(sys.version)

  程式碼並不會出現在 po 檔之中，故在 po 檔中會顯示為

  .. code-block:: rst

    Here is a code example::

  此時翻譯應為：

  .. code-block:: rst

    以下是個程式範例：

    ::

  注意\ **額外的空行是必須的**。


術語表 Glossary
===============

為了讓翻譯保持統一，我們在這邊整理了一個術語列表，如果您有不同意的地方，歡迎\
打開一個 issue 或是 pull request 一起討論。

===================== =====================
原文                  翻譯
===================== =====================
argument              引數
attribute             屬性
boolean               boolean（布林）
class                 class（類別）
condition             條件
contributor           貢獻者
deprecated            已棄用
dictionary            dictionary（字典）
element               元素
exception             例外
expression            運算式
float                 float（浮點數）
function              函式
import                import（不翻譯）
index                 索引
instance              實例
int                   int（整數）
interpreter           直譯器
iterate               疊代
list                  list（串列）
loop                  迴圈
method                method（方法）
module                module（模組）
object                物件
operand               運算元
operator              運算子
parameter             參數
prompt                提示字元
return                回傳
set                   set（集合）
statement             陳述式
type                  型別
===================== =====================


問題回報與討論
==============

如果有需要共同討論的問題，請開設一個新的 Issue_。如果是翻譯上遇到困難需要\
幫助，則可以使用 Telegram_。

.. _Issue: https://github.com/python-doc-tw/python-docs-zh-tw/issues
.. _Telegram: https://t.me/PyDocT

另外，此翻譯的 coordinator 為 `adrianliaw <https://github.com/adrianliaw>`_，\
您也可以透過此 email 聯繫：``adrianliaw2000 at gmail dot com``。


額外翻譯資源
============

- Telegram group `t.me/PyDocTW`_
- `Doc-SIG mailing list <https://mail.python.org/mailman/listinfo/doc-sig>`_
- `PEP 545 <https://www.python.org/dev/peps/pep-0545/>`_


維護、預覽
==========

以下的指令皆預設在本機端 ``python-docs-zh-tw`` clone 的根目錄執行，同時預設\
在同一個目錄底下有一個 CPython clone，如下：

::

  ~/
  ├── python-docs-zh-tw/
  └── cpython/

若要在本機端 clone 一個 CPython，可以使用以下指令：

.. code-block:: bash

  $ git clone --depth 1 --no-single-branch https://github.com/python/cpython.git

這樣可以避免下載完整的 commit 歷史（對輸出文件沒什麼幫助），但仍然能把所有的
branch clone 下來。

與 CPython 同步最新的 pot 檔
----------------------------

.. code-block:: bash

  $ make merge

尋找 fuzzy entries
------------------

*Fuzzy entries* 係指更新 po 檔的原始字串（*msgid*）以後，大部分內容相同但有\
些許差異的字串，即表示該字串的翻譯需要更新。在 po 檔中，您會看到 ``#, fuzzy``
的字樣，這就表示了接下來的字串是 fuzzy entry，需要更新翻譯。

.. code-block:: bash

  $ make fuzzy

本地端編譯輸出文件
------------------

輸出的文件會被放置在您的本地端 CPython clone（見 `維護、預覽`_ 段落的圖示）\
底下的 ``Doc/build/html``，切換到該目錄再使用 ``python3 -m http.server``
或類似的靜態網頁伺服器即可以預覽成果。編譯程序則使用：

.. code-block:: bash

  $ make


Project History
===============

This translation project was created by Liang-Bo Wang in late-2015, the
translations were hosted on https://docs.python.org.tw/3, and the project
includes daily auto-build sever, documentation website enhancement for
translations and project management on the `python-doc-tw
<https://github.com/python-doc-tw>`_ GitHub organisation. The translations
were done on Transifex, with `our own translation team and project
<https://www.transifex.com/python-tw-doc>`_. People who've contributed
on this Transifex project are listed in `TRANSLATORS`_

.. _TRANSLATORS: TRANSLATORS

In mid-2018, thanks to `PEP 545 <https://www.python.org/dev/peps/pep-0545/>`_
and the Doc-SIG community, this project has migrated to Python's Github
organisation and will become the official Taiwanese Mandarin translation of the
documentation.


Acknowledgement
===============

This translation project is highly influenced by python-doc-ja_ and
python-doc-fr_'s translation architecture and workflow (i.e. a shameless
copy). We truly appreciate their contributions.

.. _python-doc-ja: https://github.com/python-doc-ja/python-doc-ja
.. _python-doc-fr: https://github.com/python/python-docs-fr
