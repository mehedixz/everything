from PyPDF2 import PdfMerger

all = ["1.pdf","2.pdf"]
our_merger = PdfMerger()
for pdf in all:
    our_merger.append(pdf)

our_merger.write("my pdf.pdf")
our_merger.close()
