# Makefile for Chinese (Taiwan) Python Documentation
#
# Here is what you can do:
#
# - make  # Automatically build an html local version
# - make todo  # To list remaining tasks
# - make merge  # To merge pot from upstream
# - make fuzzy  # To find fuzzy strings
# - make progress  # To compute current progression
# - make upgrade_venv  # To upgrade the venv that compiles the doc
#
# Modes are: autobuild-stable, autobuild-dev, and autobuild-html,
# documented in gen/src/3.6/Doc/Makefile as we're only delegating the
# real work to the Python Doc Makefile.
#
# Credits: Python Documentation French Translation Team (https://github.com/python/python-docs-fr)

CPYTHON_CLONE := ../cpython/
SPHINX_CONF := $(CPYTHON_CLONE)/Doc/conf.py
LANGUAGE := zh_TW
LC_MESSAGES := $(CPYTHON_CLONE)/Doc/locales/$(LANGUAGE)/LC_MESSAGES
VENV := ~/.venvs/python-docs-i18n/
PYTHON := $(shell which python3)
MODE := autobuild-dev-html
BRANCH = $(shell git describe --contains --all HEAD)
JOBS = 1


.PHONY: all
all: $(VENV)/bin/sphinx-build $(VENV)/bin/blurb $(SPHINX_CONF)
	mkdir -p $(LC_MESSAGES)
	for dirname in $$(find . -name '*.po' | xargs -n1 dirname | sort -u | grep -v '^\.$$'); do mkdir -p $(LC_MESSAGES)/$$dirname; done
	for file in *.po */*.po; do ln -f $$file $(LC_MESSAGES)/$$file; done
	. $(VENV)/bin/activate; $(MAKE) -C $(CPYTHON_CLONE)/Doc/ SPHINXOPTS='-j$(JOBS) -D locale_dirs=locales -D language=$(LANGUAGE) -D gettext_compact=0' $(MODE)


$(SPHINX_CONF):
	git clone --depth 1 --no-single-branch https://github.com/python/cpython.git $(CPYTHON_CLONE)
	cd $(CPYTHON_CLONE) && git checkout $(BRANCH)


$(VENV)/bin/activate:
	mkdir -p $(VENV)
	$(PYTHON) -m venv $(VENV)


$(VENV)/bin/sphinx-build: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install sphinx python-docs-theme


$(VENV)/bin/blurb: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install blurb


.PHONY: upgrade_venv
upgrade_venv: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install --upgrade sphinx python-docs-theme blurb


.PHONY: progress
progress:
	@python3 -c 'import sys; print("{:.1%}".format(int(sys.argv[1]) / int(sys.argv[2])))'  \
	$(shell msgcat *.po */*.po | msgattrib --translated | grep -c '^msgid') \
	$(shell msgcat *.po */*.po | grep -c '^msgid')


.PHONY: todo
todo:
	for file in *.po */*.po; do echo $$(msgattrib --untranslated $$file | grep ^msgid | sed 1d | wc -l ) $$file; done | grep -v ^0 | sort -gr


.PHONY: merge
merge: upgrade_venv
ifneq "$(shell cd $(CPYTHON_CLONE) 2>/dev/null && git describe --contains --all HEAD)" "$(BRANCH)"
	$(error "You're merging from a different branch")
endif
	(cd $(CPYTHON_CLONE)/Doc; rm -f build/NEWS)
	(cd $(CPYTHON_CLONE)/Doc; $(VENV)/bin/sphinx-build -Q -b gettext -D gettext_compact=0 . locales/pot/)
	find $(CPYTHON_CLONE)/Doc/locales/pot/ -name '*.pot' |\
	    while read -r POT;\
	    do\
	        PO="./$$(echo "$$POT" | sed "s#$(CPYTHON_CLONE)/Doc/locales/pot/##; s#\.pot\$$#.po#")";\
	        mkdir -p "$$(dirname "$$PO")";\
	        if [ -f "$$PO" ];\
	        then\
	            case "$$POT" in\
	            *whatsnew*) msgmerge --backup=off --force-po --no-fuzzy-matching -U "$$PO" "$$POT" ;;\
	            *)          msgmerge --backup=off --force-po -U "$$PO" "$$POT" ;;\
	            esac\
	        else\
	            msgcat -o "$$PO" "$$POT";\
	        fi\
	    done


.PHONY: update_txconfig
update_txconfig:
	curl -L https://rawgit.com/python-doc-ja/cpython-doc-catalog/catalog-$(BRANCH)/Doc/locales/.tx/config |\
		grep --invert-match '^file_filter = *' |\
		sed -e 's/source_file = pot\/\(.*\)\.pot/trans.zh_TW = \1.po/' |\
		sed -n 'w .tx/config'


.PHONY: fuzzy
fuzzy:
	for file in *.po */*.po; do echo $$(msgattrib --only-fuzzy --no-obsolete "$$file" | grep -c '#, fuzzy') $$file; done | grep -v ^0 | sort -gr
