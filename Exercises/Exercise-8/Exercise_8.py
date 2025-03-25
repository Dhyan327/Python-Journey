# In this part I will do "Exercise 8 Solution"

# Exercise :->
""" Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
    pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.
    It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well. """

# Solution :~~>
import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]
# pdf_files = ['Python Ebooks.pdf', 'The Ultimate Python Handbook.pdf']
output_file = 'merged.pdf'

for pdf in pdf_files:
    if not os.path.exists(pdf):
        print(f"Error: {pdf} does not exist.")
        exit(1)

merge_pdfs(pdf_files, output_file)
print(f'Merged file saved as {output_file}')