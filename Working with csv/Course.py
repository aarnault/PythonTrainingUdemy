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
full_name =[]

for line in data_lines[1:]:
    full_names.apend(line[1]+' '+line[2])

full_names

file_to_output = open('to_save_file.csv', mode='w', newline='')

csv_writer =csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a', 'b', 'c'])

csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()

f=open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)

csv_writer.writerow(['1', '2', '3'])