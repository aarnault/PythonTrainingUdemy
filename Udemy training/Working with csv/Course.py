#CSV (Common S V)

import csv

#open the file
data = open('example.csv', encoding = 'utf-8')

#csv.reader

csv_data = csv.reader(data)
#reformat it inot a python object list in lists
data_lines = list(csv_data)

data_lines[0]
len(data_lines)

for line in data_lines[:5]:
    print(line)

data_lines[10] [3]

all_emails = []
for line in data_lines [1:]:
    all_emails.append(line[3])


all_emails

#full name
full_names =[]

for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])

full_names

file_to_output = open('to_save_file.csv', mode='w', newline='')

csv_writer =csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a', 'b', 'c'])

csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()

f=open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)

csv_writer.writerow(['1', '2', '3'])

f.close()

#PDF(Portable Document Format) needs to be readable by PyPDF2

import PyPDF2

f= open('working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages

page_one=pdf_reader.getPage(0)
page_one_text =page_one.extractText()
page_one_text

f.close()

f=open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(first_page)

#open a new file

pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)

f.close()

pdf_output.close()

#grab all the text from a pdf

f=open('Working_Business_Proposal.pdf', 'rb')

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page =pdf_reader.getPage(num)
    pdf_text.append(page.extractText())
    print(pdf_text[1])