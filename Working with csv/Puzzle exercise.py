import csv

#open the file
data = open('find_the_link.csv', encoding = 'utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)

link_str = ''
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]


import PyPDF2

f= open('find_the_phone_number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)
pdf.numPages

import re

pattern = r'\d{3}'

all_text=''

for n in range(pdf.numPages):
    page=pdf.getPage(n)
    page_text =page.extractText()

    all_text = all_text +' '+ page_text

re.findall(pattern, all_text)

for match in re.findinter(pattern, all_text):
    print(match)

all_text[41790:41808+20]

# edit the pattern now:
pattern = r'\d{3].\d{3}.\{4}' #and rerun all the rest.