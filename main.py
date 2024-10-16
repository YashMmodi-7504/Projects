import PyPDF2

pdfiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        merger.append(pdfFile)

merger.write('merged.pdf')
merger.close()
