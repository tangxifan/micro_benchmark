# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PYTHON_EXEC   ?= python3

PAPER =
PAPEROPT_a4 = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALL_SPHINXOPTS = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(SOURCEDIR)

.ONESHELL:

# Put it first so that "make" without argument is like "make help".
export COMMENT_EXTRACT

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@${PYTHON_EXEC} -c "$$COMMENT_EXTRACT"

livehtml:
	sphinx-autobuild -b html $(ALL_SPHINXOPTS) $(BUILDDIR)/html

clean:
	rm -rf $(BUILDDIR)/*

.PHONY: help clean Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#html:
#	$(SPHINXBUILD) -b html $@ "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

# Functions to extract comments from Makefiles
define COMMENT_EXTRACT
import re
with open ('Makefile', 'r' ) as f:
    matches = re.finditer('^([a-zA-Z-_]*):.*\n#(.*)', f.read(), flags=re.M)
    for _, match in enumerate(matches, start=1):
        header, content = match[1], match[2]
        print(f"  {header:10} {content}")
endef


