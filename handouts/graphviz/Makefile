GV_FILES = $(wildcard *.gv)
PDF_FILES = $(GV_FILES:.gv=.pdf)

all: $(PDF_FILES)

%.pdf: %.gv
	dot -Tpdf $^ > $@

clean:
	rm *.pdf
