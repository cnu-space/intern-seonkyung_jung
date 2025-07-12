# $LastChangedBy: kyungguk $
# $LastChangedDate: 2024-12-24 14:25:59 +0900 (Tue, 24 Dec 2024) $
# $Revision: 3240 $
# $Id: Makefile 3240 2024-12-24 05:25:59Z kyungguk $


FILENAME=main

DOCUMENT:=$(FILENAME)
SOURCES:=$(DOCUMENT).tex


all: article

article: $(DOCUMENT)

$(DOCUMENT): $(SOURCES)
	pdflatex $(DOCUMENT) || :
	pdflatex $(DOCUMENT) || :
	pdflatex $(DOCUMENT) || :

clean:
	rm -rvf $(DOCUMENT).pdf
	rm -rvf _minted/
	rm -rvf main.aux main.log main.out main.toc
