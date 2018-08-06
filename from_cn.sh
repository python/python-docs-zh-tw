#!/bin/sh

fp=$1
python_docs_zh_cn=../python-docs-zh-cn

opencc -i $python_docs_zh_cn/$fp -c s2twp.json -o /tmp/tmp.po
pofilter --nonotes --excludefilter unchanged --excludefilter untranslated /tmp/tmp.po | msgattrib --set-fuzzy -o /tmp/tmp.po
pomerge -t $python_docs_zh_cn/$fp -i /tmp/tmp.po -o /tmp/tmp.po

pofilter --nonotes --excludefilter untranslated $fp /tmp/tmp2.po
pomerge -t /tmp/tmp.po -i /tmp/tmp2.po -o /tmp/tmp3.po
msgcat --lang zh_TW /tmp/tmp3.po -o $fp

rm /tmp/tmp.po /tmp/tmp2.po /tmp/tmp3.po
