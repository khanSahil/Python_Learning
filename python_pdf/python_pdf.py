# PDF stands for Portable Document Format and developed by Adobe
# in 1990s.

# The most important thing to keep in mind is that while PDFs share
# the same extensions and can be viewed in PDF readers, many PDFs are
# not machine readable through Python

# Since PDFs mainly encapsulate and display a fixed-layout flat document,
# there is no machine readable standard format, unline CSV files.

# This means that a PDF that was simply scanned is highly unlikely to be readable.

# Addition to PDFs such as images, tables, format adjustments can also render
# a PDF unreadable by Python.

# There are many paid PDF programs that can read and extract form these files, but
# we will use the open-source and free PyPDF2 library.

import PyPDF2

f = open("Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(page_one)
print(page_one_text)

f.close()

f = open("Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(f)
page_one = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open('Some_Brand_New_PDF_File', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

f = open("Working_Business_Proposal.pdf", 'rb')
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)
for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[0]
    pdf_text.append(page_one.extract_text())

print(pdf_text[1])