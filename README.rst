=======================================
Python 官方說明文件臺灣繁體中文翻譯計畫
=======================================

.. image:: https://badgen.net/badge/chat/on%20Discord/blue
   :target: https://discord.gg/44XheGXhWH
   :alt: Join Chat on Discord

這是 Python 3.11 官方說明文件的臺灣繁體中文（zh_TW）翻譯。

翻譯之前，請務必詳讀並同意\ `授權與 License`_。參與方式請參考\ `參與翻譯`_。

你可以在 https://python.github.io/python-docs-zh-tw/ 瀏覽目前翻譯的成果。

想問問題、認識翻譯同好，歡迎加入 Discord 頻道 `discord.gg/44XheGXhWH`_

.. _discord.gg/44XheGXhWH: https://discord.gg/44XheGXhWH

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
此專案在 Transifex、GitHub 以及其他公眾場合，以及邀請你參與，我們向你提出一個\
協議：你必須將你對於 Python 說明文件或是 Python 說明文件翻譯的貢獻以 CC0\
（請參考 https://creativecommons.org/publicdomain/zero/1.0/legalcode）的方式\
授權給 PSF 使用。你可以公開地聲明你所貢獻翻譯的部分，並且如果你的翻譯被 PSF
採用，你可以（但並不須要）送出一個修改，其包含在 Misc/ACKS 或是 TRANSLATORS
檔案裡增加合適的注釋。雖然這個說明文件貢獻協議並沒有說明 PSF 有義務納入你的\
文本貢獻，你在 Python 社群的參與是受歡迎且受感激的。

你在對 PSF 送出說明文件貢獻的同時，即表示同意上述的協議。


參與翻譯
========

關於 po (Portable Object) 檔
-----------------------------

此為所需翻譯的文字檔，副檔名為 ``.po``，不同語系就會有一個 po 檔。主要內容為翻譯的參考原始字串 (*msgid*)，\
及需要填入的翻譯字串 (*msgstr*)。有時你會看到 ``#, fuzzy`` 的註記，它代表此翻譯字串需要校閱。

翻譯流程
------------

**請注意**: 以下基於 ``make`` 的便捷指令僅能運作於 Unix 系統上（無法使用並不影響主要翻譯流程），\
其他作業系統的使用者在翻譯後可考慮改於 `GitHub Codespace <https://github.com/features/codespaces>`_ 上呼叫 ``make`` 指令。

事先需要有
~~~~~~~~~~

- 一個 `GitHub 帳號 <https://github.com/join>`_
- `安裝好 git <https://help.github.com/articles/set-up-git/>`_\ （Windows
  上請參考 https://gitforwindows.org/）
- 一個 ``.po`` 檔的編輯器。推薦使用 `Poedit <https://poedit.net>`_，若熟悉 po 檔用一般文字編輯器亦可。
- macOS 的使用者還需要先利用 `homebrew <https://brew.sh/index_zh-tw>`_ 安裝 gettext，屆時 Sphinx 會使用到。
.. code-block:: bash

  brew install gettext

  brew link gettext --force

在進行任何動作以前，你必須在 GitHub 上 fork 此專案（按下右上角的 ``Fork``
按鈕），這樣會把整個專案複製一份到你的 GitHub 帳號底下，你可以對這個 fork
進行修改。

第一次貢獻以前（還沒有 clone 過)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

請在 terminal 裡依照以下步驟：

.. code-block:: bash

  # 用 git clone 將你的 fork 下載到本機端
  git clone git@github.com:<你的 GitHub 帳號>/python-docs-zh-tw.git

  # 進入 clone 下來的資料夾裡：
  cd python-docs-zh-tw/

  # 將 python/python-docs-zh-tw 設為 upstream remote
  git remote add upstream https://github.com/python/python-docs-zh-tw.git

每一次翻譯時
~~~~~~~~~~~~

請遵照以下步驟（`GitHub Flow`_）：

.. _GitHub Flow: https://guides.github.com/introduction/flow/

首先，`新增一個 issue <https://github.com/python/python-docs-zh-tw/issues>`_\
，如：「翻譯 tutorial/introduction.po」，讓大家知道你正在翻譯這個檔案。可以使用 `make todo` 列出尚待翻譯的檔案。

接著在 terminal 裡按照以下步驟：

1. 基於最新版本的 ``upstream/3.11`` 開啟一個 branch，現在假設我們想要翻譯 Glossary \
   所以把這個 branch 叫做 ``glossary`` ::

    git fetch upstream
    git checkout -b glossary upstream/3.11

2. 接著就可以開始翻譯（翻譯時可參考 `翻譯守則`_），你可以手動開啟 Poedit 應用程式再選檔案或用以下指令請 Poedit 將檔案\
   打開，翻譯不同檔案時將 glossary 換成別的檔名） ::

    poedit glossary.po

3. 存檔以後，執行以下列指令編譯輸出文件，以確保你的修改沒有 rST 的語法錯誤或警告 ::

    VERSION=3.11 make all

   如果你還沒有執行 `維護、預覽`_ 的 clone CPython 的動作，此指令會自動幫你 clone CPython，\
   並且會使用 Sphinx 幫你檢查 rST 語法錯誤，我們盡量保持沒有 warning \
   的狀態，因此如果有出現 warning 的話請修復它。另外也記得檢查是否符合\
   `翻譯守則`_

4. 輸出的文件會被放置在你的本地端 CPython clone（見 `維護、預覽`_ 段落的圖示）\
   底下的 ``Doc/build/html``，切換到該目錄再使用 ``python3 -m http.server`` \
   或類似的靜態網頁伺服器即可以預覽成果。你可以執行下列指令請瀏覽器打開編譯出來的文件\
   以確認整份文件的語意通暢（翻譯別的檔案時將 glossary 換成別的檔名） ::

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

這整個流程裡有幾件事情值得注意：

- 從 upstream（我們的主要 GitHub repo）做 fetch 的動作
- 對 origin（你的 fork）做 push
- 永遠不對 ``3.11`` branch 進行修改，請保持讓這個 branch 唯讀，可以避免\
  掉很多問題。

要翻譯哪些東西
--------------

主要是填入翻譯字串 (*msgstr*) 以及更新有標記為 ``#, fuzzy`` 的字串。

其中最簡單的貢獻方式就是更新 *fuzzy entries*，讓曾經翻譯的內容保持與最新版本的文件\
同步。請參考 `尋找有翻譯過但需校閱的 fuzzy entries`_ 段落。

此外，當前的目標為完成 **Tutorial** 的翻譯，因此在 ``tutorial/`` 底下的所有
po 檔皆為首要的翻譯對象。你也可以幫忙校對已經翻譯過的內容。


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
   ``dict``、``set``、``iterator``、``generator``、``iterable``、
   ``pickle``


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

為了讓翻譯保持統一，我們整理了一份 `術語列表 
<https://github.com/python/python-docs-zh-tw/wiki/%E8%A1%93%E8%AA%9E%E5%88%97%E8%A1%A8>`_ \
如果翻譯過程中你覺得需要術語列表有所缺漏，請至 `Discussion \
<https://github.com/python/python-docs-zh-tw/discussions>`_ 開啟新的討論補充術語。\
新增的術語，將會於每次 Sprint 中共同討論是否合併進術語列表。



問題回報與討論
==============

如果有需要共同討論的問題，請開設一個新的 Issue_。如果是翻譯上遇到困難需要\
幫助，則可以使用 Discord_。

.. _Issue: https://github.com/python/python-docs-zh-tw/issues
.. _Discord: https://discord.gg/44XheGXhWH

另外，此翻譯的 coordinator 為 `mattwang44 <https://github.com/mattwang44>`_ 和 \
`josix <https://github.com/josix>`_，你也可以分別透過以下 email 聯繫：\
``mattwang44 at gmail dot com``, ``josixwang at gmail dot com``。


額外翻譯資源
============

- Discord channel `discord.gg/44XheGXhWH`_
- `Doc-SIG mailing list <https://mail.python.org/mailman/listinfo/doc-sig>`_
- `PEP 545 <https://www.python.org/dev/peps/pep-0545/>`_
- `zh_CN Translation of the Python Documentation
  <https://github.com/python/python-docs-zh-cn>`_
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

與 CPython 同步最新的 pot 檔 (目前由 GitHub Actions 定時代為執行)
----------------------------------------------------------

pot 檔為翻譯的樣板檔案，它包含需要翻譯的原始字串 (*msgid*) 跟其對應的空白翻譯字串 (*msgstr*)，\
此步驟會參考最新的 CPython 中的 pot 檔來更新 po 檔。如果是之前在 po 檔中已填入過翻譯字串但參考的 \
pot 檔的 ``msgid`` 已有變動，則此指令會自動加上 ``#, fuzzy`` 的標記，代表內容有些許差異需要更新。

.. code-block:: bash

  $ make merge

尋找有翻譯過但需校閱的 fuzzy entries
---------------------------------

在 po 檔中，你會看到 ``#, fuzzy`` 的字樣，這就表示了接下來的字串是 fuzzy entry，需要更新翻譯。\
你可以自行用習慣的文字編輯器、Linux 指令搜尋有包含此字樣的檔案，但請記得 ``#, fuzzy`` 標記的翻譯字串\
有可能是尚未翻譯過的空白字串 (*msgstr*)。執行下列指令會列出有 *Fuzzy entries* 的檔案且會排除這個情形。

.. code-block:: bash

  $ make fuzzy

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
