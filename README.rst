=======================================
Python 官方說明文件臺灣繁體中文翻譯計畫
=======================================

.. image:: https://badgen.now.sh/badge/chat/on%20Telegram/blue
   :target: https://t.me/PyDocTW
   :alt: Join Chat on Telegram

這是 Python 3.7 官方說明文件的臺灣繁體中文（zh_TW）翻譯。

翻譯之前，請務必詳讀並同意\ `授權與 License`_。參與方式請參考\ `參加翻譯`_。

您可以在 https://python-doc-tw.github.io/ 瀏覽目前翻譯的成果。

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

**事先需要有：**

- 一個 `GitHub 帳號 <https://github.com/join>`_
- `安裝好 git <https://help.github.com/articles/set-up-git/>`_\ （Windows
  上請參考 https://gitforwindows.org/）
- 一個 ``.po`` 檔的編輯器，如果還沒有的話請使用 `poedit <https://poedit.net>`_

在進行任何動作以前，你必須在 GitHub 上 fork 此專案（按下右上角的 ``Fork``
按鈕），這樣會把整個專案複製一份到你的 GitHub 帳號底下，你可以對這個 fork
進行修改。

在\ **第一次貢獻以前**\ （還沒有 clone 過），請在 terminal 裡依照以下步驟：

.. code-block:: bash

  # 用 git clone 將你的 fork 下載到本機端
  git clone git@github.com:<你的 GitHub 帳號>/python-docs-zh-tw.git

  # 進入 clone 下來的資料夾裡：
  cd python-docs-zh-tw/

  # 將 python/python-docs-zh-tw 設為 upstream remote
  git remote add upstream https://github.com/python/python-docs-zh-tw.git

在\ **每一次翻譯時**\ 請遵照以下步驟（`GitHub Flow`_）：

.. _GitHub Flow: https://guides.github.com/introduction/flow/

首先，`新增一個 issue <https://github.com/python/python-docs-zh-tw/issues>`_\
，如：「翻譯 tutorial/introduction.po」，讓大家知道您正在翻譯這個檔案。

接著在 terminal 裡按照以下步驟：

1. 基於最新版本的 ``upstream/3.7`` 開啟一個 branch，現在假設我們想要翻譯 Glossary
   所以把這個 branch 叫做 ``glossary`` ::

    git fetch upstream
    git checkout -b glossary upstream/3.7

2. 接著就可以開始翻譯，你可以使用 Poedit 應用程式將檔案打開，或是用以下指令\
   （翻譯不同檔案時將 glossary 換成別的檔名） ::

    poedit glossary.po

3. 存檔以後，可以輸出文件以確保你的修改沒有 rST 的語法錯誤或警告 ::

    make

   這個過程中 Sphinx 會幫你檢查 rST 語法錯誤，我們盡量保持沒有 warning
   的狀態，因此如果有出現 warning 的話請修復它。另外也記得檢查是否符合\
   `翻譯守則`_

4. 在瀏覽器中打開編譯出來的文件以確認整份文件的語意通暢\
   （翻譯別的檔案時將 glossary 換成別的檔名） ::

    open ../cpython/Doc/build/html/glossary.html

5. 檢查完畢後，即可以將你的翻譯 commit 起來，請使用明確的 commit message ::

    git add glossary.po
    git commit -m "Working on glossary."

6. 將你的修改 push 到你的 GitHub clone 上。為了簡單，我們可以用 ``origin HEAD``
   來告訴 git 我們將修改 push 到 origin，branch 則和本機端的 branch 名稱一樣 ::

    git push origin HEAD

7. 這時候你就可以打開一個 pull request 了，請打開
   https://github.com/python/python-docs-zh-tw，你會看到一個「Compare & Pull
   Request」按鈕，按下它就可以對此專案發送一個 pull request。

8. 如果有人在 GitHub 上 review 了你的 pull request，並且你想要修改你的內容，\
   那麼（如果你切換到了別的 branch 上）你要先切換回到你的 branch 上 ::

    git checkout glossary

   接著修改你要修正的問題，並再次 commit、push ::

    git add glossary.po
    git commit -m "glossary: small fixes"
    git push origin HEAD


要翻譯哪些東西
--------------

最簡單的貢獻方式就是更新 *fuzzy entries*，讓翻譯的內容保持與最新版本的文件\
同步。請參考 `尋找 fuzzy entries`_ 段落。

此外，當前的目標為完成 **Tutorial** 的翻譯，因此在 ``tutorial/`` 底下的所有
po 檔皆為首要的翻譯對象。您也可以幫忙校對已經翻譯過的內容。


翻譯守則
========

#. 譯文應兼顧前後文大意，在翻譯一份文件前請務必熟讀該文件的原文。

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

#. po 檔單行不應超過 79 字元寬度（Poedit 會處理，但也可以使用 `poindent
   <https://pypi.org/project/poindent/>`_ 來確保格式）

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
- `zh_CN Translation of the Python Documentation
  <https://zhsj.github.io/python-docs-zh-cn/>`_
- `Cambridge Dictionary <https://dictionary.cambridge.org/>`_


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
