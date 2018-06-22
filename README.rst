=======================================
Python 官方說明文件臺灣繁體中文翻譯計畫
=======================================

本 GitHub repository 含有 Python 官方說明文件的 zh_TW 翻譯。實際的翻譯內容\
在這個 repository 裡以 Python 的穩定發行版本作為 branch 名稱，請參考 3.6 等
branch 以查看目前的翻譯內容。此 master branch 則為專案的貢獻說明。

您可以在 https://python-doc-tw.github.io/ 瀏覽目前翻譯的成果。目前以
Python 3.6 為翻譯的對象，**暫時不考慮 Python 2.7 的翻譯工作**。未來有新的
Python 發行版本時，也將會將翻譯滾動至新的版本。


在 Wiki_ 中有更多關於參加翻譯、翻譯風格規範、自行編譯文件等說明（待更新）。

想問問題、認識翻譯同好，歡迎加入 Telegram 聊天室 `t.me/PyDocTW`_

.. _Wiki: https://github.com/python-doc-tw/python-docs-zh-tw/wiki
.. _t.me/PyDocTW: https://t.me/PyDocTW


參加翻譯
========

如何參加翻譯
------------

實際的翻譯即為修改 po 檔，流程遵照標準的 **GitHub Flow**，請 fork 此專案並在您\
自己的 fork 裡新增一個 branch，修改 po 檔內容並 commit、push 以後對此專案發出
pull request（記得 base 是此專案的其中一個 branch；目前只有 3.6），至少有一人\
審查過翻譯以後，才可以 merge 進入此 repository 中。

在對任何檔案進行貢獻之前，請先在本專案\ **新增一個 issue**，註明您正在翻譯的頁面\
名稱，並將該 issue **assign 給自己**，讓大家知道您正在修改該頁面，以避免多人\
同時貢獻同一個檔案的衝突。

編輯 po 檔的方式主要可以分為兩種，以 Transifex 作為工具或是使用其他翻譯工具：

1. 使用 Transifex 作為翻譯工具
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

您可以註冊 Transifex 帳號並加入我們的 `Transifex 專案
<https://www.transifex.com/python-tw-doc/python-36-tw>`_，並且在上面\
編輯您所要翻譯的頁面，並且在您本機上透過 command line 從此專案的 clone 的\
根目錄位置執行以下指令：

.. code-block:: bash

  $ ./txpull <po 檔的路徑>

此指令會需要 PyPI 上的 ``transifex-client`` 和 ``poindent``，|gettext|_、
``tac`` 等指令。這個小工具可以幫您把您在 Transifex 上針對特定檔案的翻譯 pull
下來，並且修正換行格式的錯誤。您在使用 txpull 以後就可以 commit 以及 push 了。

.. |gettext| replace:: ``gettext``
.. _gettext: https://www.gnu.org/software/gettext/

2. 使用其他翻譯工具
~~~~~~~~~~~~~~~~~~~

使用 Transifex 並非強迫性，您可以使用其他翻譯工具，如：

- 推薦：`poedit <https://www.poedit.net/>`_
- gted
- gtranslator
- lokalize
- betterpoeditor
- 適當模式底下的 vim 或 emacs
- Vé on Android
- 可能還有更多其他的

編輯完檔案以後，請執行以下指令以確保檔案的換行格式一致（需要安裝
|poindent|_）：

.. |poindent| replace:: ``poindent``
.. _poindent: https://pypi.org/project/poindent/

.. code-block:: bash

  $ poindent <po 檔的路徑>

執行完 ``poindent`` 以後即可 commit、push 等。


問題回報與討論
--------------

如果有需要共同討論的問題，請開設一個新的 Issue_。如果是翻譯上遇到困難需要\
幫助，則可以使用 Telegram_。

.. _Issue: https://github.com/python-doc-tw/python-docs-zh-tw/issues
.. _Telegram: https://t.me/PyDocT

另外，此翻譯的 coordinator 為 `adrianliaw <https://github.com/adrianliaw>`_，\
您也可以透過此 email 聯繫：``adrianliaw2000 at gmail dot com``。


額外翻譯資源
------------

- Telegram group `t.me/PyDocTW`_
- `Doc-SIG mailing list <https://mail.python.org/mailman/listinfo/doc-sig>`_
- `PEP 545 <https://www.python.org/dev/peps/pep-0545/>`_
- 我們的 `Transifex 專案 <https://www.transifex.com/python-tw-doc/>`_
- 我們在 Transifex 上的 `Glossary
  <https://www.transifex.com/python-tw-doc/python-36-tw/glossary/zh-Hant/>`_


授權與 License
==============

以下為 Documentation Contribution Agreement，說明文件貢獻協議，請在貢獻以前\
務必詳讀以下內容。（後面有中文翻譯）

Documentation Contribution Agreement
------------------------------------

NOTE REGARDING THE LICENSE FOR TRANSLATIONS: Python's documentation is
maintained using a global network of volunteers. By posting this
project on Transifex, Github, and other public places, and inviting
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

中文翻譯（請盡量以原文為準）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

請注意此予翻譯專案的授權：Python 的說明文件是以全球的志工社群來維護。透過張貼\
此專案在 Transifex、GitHub 以及其他公眾場合，以及邀請您參與，我們向您提出一個\
協議：您必須將您對於 Python 說明文件或是 Python 說明文件翻譯的貢獻以 CC0\
（請參考 https://creativecommons.org/publicdomain/zero/1.0/legalcode）的方式\
授權給 PSF 使用。您可以公開地聲明您所貢獻翻譯的部分，並且如果您的翻譯被 PSF
採用，您可以（但並不須要）送出一個修改，其包含在 Misc/ACKS 或是 TRANSLATORS
檔案裡增加合適的注釋。雖然這個說明文件貢獻協議並沒有說明 PSF 有義務納入您的\
文本貢獻，您在 Python 社群的參與是受歡迎且受感激的。

您在對 PSF 送出說明文件貢獻的同時，即表示同意上述的協議。


Acknowledgement
===============

This translation project is highly influenced by python-doc-ja_ and
python-doc-fr_'s translation architecture and workflow (i.e. a shameless
copy). We truly appreciate their contributions.

.. _python-doc-ja: https://github.com/python-doc-ja/python-doc-ja
.. _python-doc-fr: https://github.com/python/python-docs-fr
