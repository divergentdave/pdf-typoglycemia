PDF Typoglycemia
================

This is a toy that uses [Joshua Tauberer's pdf-redactor library](https://github.com/JoshData/pdf-redactor) to modify PDF documents by [scrambling the letters in the middle of each word](https://en.wikipedia.org/wiki/Typoglycemia).

## Usage
First, install `pdf-redactor` and [`qpdf`](http://qpdf.sourceforge.net/). Then, run the following command.

```
qpdf --stream-data=uncompress in.pdf - | PYTHONPATH=/path/to/pdf-redactor python3 pdf_typoglycemia.py > out.pdf
```
