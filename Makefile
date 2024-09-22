# Makefile for Chinese (Taiwan) Python Documentation
#
# Here is what you can do:
#
# - make all # Automatically build an html local version
# - make build <po-file>  # To build a single .po file
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

.DEFAULT_GOAL := help # Sets default action to be help

define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("%-10s %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section

CPYTHON_CLONE := ../cpython
VERSION := $(or $(VERSION), 3.13)
SPHINX_CONF := $(CPYTHON_CLONE)/Doc/conf.py
LANGUAGE := zh_TW
LC_MESSAGES := $(CPYTHON_CLONE)/Doc/locales/$(LANGUAGE)/LC_MESSAGES
VENV := ~/.venvs/python-docs-i18n/
MODE := autobuild-dev-html
JOBS := 4

.PHONY: all
all: prepare_deps ## Automatically build an html local version
	for dirname in $$(find . -name '*.po' | xargs -n1 dirname | sort -u | grep -v '^\.$$'); do mkdir -p $(LC_MESSAGES)/$$dirname; done
	for file in *.po */*.po; do ln -f $$file $(LC_MESSAGES)/$$file; done
	. $(VENV)/bin/activate; $(MAKE) -C $(CPYTHON_CLONE)/Doc/ SPHINXOPTS='-j$(JOBS) -D locale_dirs=locales -D language=$(LANGUAGE) -D gettext_compact=0' $(MODE)

.PHONY: build
build: prepare_deps ## Automatically build an html local version for a single file
	@$(eval target=$(filter-out $@,$(MAKECMDGOALS)))
	@if [ -z $(target) ]; then \
		echo "\x1B[1;31m""Please provide a file argument.""\x1B[m"; \
		exit 1; \
	fi
	@if [ "$(suffix $(target))" != ".po" ]; then \
		echo "\x1B[1;31m""Incorrect file extension. Only '.po' files are allowed.""\x1B[m"; \
		exit 1; \
	fi
	@if [[ ! -f "$(target)" ]] ; then \
		echo "\x1B[1;31m""ERROR: $(target) not exist.""\x1B[m"; \
		exit 1; \
	fi

	@$(eval dir=`echo $(target) | xargs -n1 dirname`) ## Get dir
	@mkdir -p $(LC_MESSAGES)/$(dir)
	@ln -f ./$(target) $(LC_MESSAGES)/$(target)

	@. $(VENV)/bin/activate; $(MAKE) -C $(CPYTHON_CLONE)/Doc/ SPHINXOPTS='-j$(JOBS) -D language=$(LANGUAGE) -D locale_dirs=locales -D gettext_compact=0' SOURCES='$(basename $(target)).rst' html


help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: prepare_deps
prepare_deps: $(VENV)/bin/sphinx-build $(VENV)/bin/blurb upgrade_venv prepare_cpython  ## Prepare dependencies

.PHONY: prepare_cpython
prepare_cpython:  ## Prepare CPython clone at `../cpython/`.
	git clone --depth 1 --no-single-branch https://github.com/python/cpython.git $(CPYTHON_CLONE)  || echo "cpython exists"
	cd $(CPYTHON_CLONE) && git checkout $(VERSION) && git pull origin $(VERSION)
	mkdir -p $(LC_MESSAGES)


$(VENV)/bin/activate:
	python3 -m venv $(VENV)

$(VENV)/bin/sphinx-build: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install sphinx python-docs-theme

$(VENV)/bin/sphinx-lint: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install sphinx-lint

$(VENV)/bin/blurb: $(VENV)/bin/activate
	. $(VENV)/bin/activate; python3 -m pip install blurb


.PHONY: upgrade_venv
upgrade_venv: $(VENV)/bin/activate ## Upgrade the venv that compiles the doc
	@. $(VENV)/bin/activate; python3 -m pip install -q --upgrade sphinx python-docs-theme blurb sphinx-lint


.PHONY: progress
progress: ## Compute current progression
	@python3 -c 'import sys; print("{:.1%}".format(int(sys.argv[1]) / int(sys.argv[2])))'  \
	$(shell msgcat *.po */*.po | msgattrib --translated | grep -c '^msgid') \
	$(shell msgcat *.po */*.po | grep -c '^msgid')


.PHONY: todo
todo: ## List remaining tasks
	for file in *.po */*.po; do echo $$(msgattrib --untranslated $$file | grep ^msgid | sed 1d | wc -l ) $$file; done | grep -v ^0 | sort -gr


.PHONY: merge
merge: prepare_deps  ## To merge pot from upstream
	(cd $(CPYTHON_CLONE)/Doc; rm -f build/NEWS)
	(cd $(CPYTHON_CLONE)/Doc; $(VENV)/bin/sphinx-build -Q -b gettext -D gettext_compact=0 . locales/pot/)
	find $(CPYTHON_CLONE)/Doc/locales/pot/ -name '*.pot' |\
	    while read -r POT;\
	    do\
	        PO="./$$(echo "$$POT" | sed "s#$(CPYTHON_CLONE)/Doc/locales/pot/##; s#\.pot\$$#.po#")";\
	        mkdir -p "$$(dirname "$$PO")";\
	        if [ -f "$$PO" ];\
	        then\
	            msgmerge --lang=$(LANGUAGE) --backup=off --force-po -U "$$PO" "$$POT";\
	        else\
	            msgcat --lang=$(LANGUAGE) -o "$$PO" "$$POT";\
	        fi\
	    done


.PHONY: update_txconfig
update_txconfig:
	curl -L https://rawgit.com/python-doc-ja/cpython-doc-catalog/catalog-$(VERSION)/Doc/locales/.tx/config |\
		grep --invert-match '^file_filter = *' |\
		sed -e 's/source_file = pot\/\(.*\)\.pot/trans.zh_TW = \1.po/' |\
		sed -n 'w .tx/config'


.PHONY: fuzzy
fuzzy: ## Find fuzzy strings
	for file in *.po */*.po; do echo $$(msgattrib --only-fuzzy --no-obsolete "$$file" | grep -c '#, fuzzy') $$file; done | grep -v ^0 | sort -gr

.PHONY: rm_cpython
rm_cpython: ## Remove cloned cpython repo
	rm -rf $(CPYTHON_CLONE)

.PHONY: lint
lint:  $(VENV)/bin/sphinx-lint  ## Run sphinx-lint
	$(VENV)/bin/sphinx-lint --enable default-role

# This allows us to accept extra arguments (by doing nothing when we get a job that doesn't match, rather than throwing an error)
%:
	@:
