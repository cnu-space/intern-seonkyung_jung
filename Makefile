# $LastChangedBy: kyungguk $
# $LastChangedDate: 2024-12-24 14:25:59 +0900 (Tue, 24 Dec 2024) $
# $Revision: 3240 $
# $Id: Makefile 3240 2024-12-24 05:25:59Z kyungguk $


LATEXMK=latexmk
BUILDDIR=build
ARGS=
TEXFLAGS=-bibtex -pdflatex -outdir=$(BUILDDIR) $(ARGS)

FILENAME=document
SI_FILENAME=SIdocument

DOCUMENT:=$(FILENAME)
SECTIONS:=sections
SOURCES:=$(DOCUMENT).tex \
	bib/bib_list.bib \
	$(shell find ./$(SECTIONS) -type f -name "*.tex" -not -name "SI*.tex")

SI_DOCUMENT:=$(SI_FILENAME)
SI_SOURCES:=$(SI_DOCUMENT).tex \
	bib/bib_list.bib \
	$(shell find ./$(SECTIONS) -type f -name "SI*.tex")


all: article

reply:
	$(MAKE) -C RevisionReport INSTALL_PREFIX=$(PWD)

article: $(DOCUMENT)

SI: $(SI_DOCUMENT)

$(DOCUMENT): $(SOURCES)
	$(LATEXMK) $(TEXFLAGS) $(DOCUMENT)
	(test -f $@.pdf && cmp -s $(BUILDDIR)/$@.pdf $@.pdf) || \
		cp -v $(BUILDDIR)/$@.pdf $@.pdf

$(SI_DOCUMENT): $(SI_SOURCES)
	$(LATEXMK) $(TEXFLAGS) $(SI_DOCUMENT)
	(test -f $@.pdf && cmp -s $(BUILDDIR)/$@.pdf $@.pdf) || \
		cp -v $(BUILDDIR)/$@.pdf $@.pdf

clean:
	$(LATEXMK) $(TEXFLAGS) -C
	rm -rvf $(BUILDDIR) $(DOCUMENT).pdf $(SI_DOCUMENT).pdf
	$(MAKE) -C RevisionReport INSTALL_PREFIX=$(PWD) clean
