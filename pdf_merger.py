from PyPDF2 import PdfFileMerger
import os

number_of_pdf = 3 # change the value here

path = os.path.dirname(__file__)
merger = PdfFileMerger()

for i in range(number_of_pdf):
    file_name = str(i+1) + '.pdf'
    merger.append(os.path.join(path, file_name))

file_merge = os.path.join(path, "merged.pdf")
merger.write(file_merge)
merger.close()