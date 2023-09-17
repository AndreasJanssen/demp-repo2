# source of this code is https://realpython.com/creating-modifying-pdf/

from PyPDF2 import PdfWriter

merger = PdfWriter()
for pdf in ["sample.pdf", "Vattenfall AB 2023_03_05.pdf"]:
    merger.append(pdf)

merger.write("Vattenfall AB 2023_03_05.pdf")
merger.close()