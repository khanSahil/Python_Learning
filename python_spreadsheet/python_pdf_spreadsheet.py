# CSV - Comma Separated Variables
# Name, Hours, Rate
# David, 20, 15

# While it is possible to export excel files and Google
# Spreadsheets to .csv files, it only exports the information.

# Things like formulas, images, and macros cannot be within
# a CSV file.
# Simply put, a .csv file only contains the raw data from the
# spreadhseet.

# We will work with built-in csv module for python, which will 
# allow us to grab columns, rows, and values from a .csv file
# as well as write to a .csv file.

# keep in mind, this is very popular space for outside libraries,
# which you may want to explore on your own.

# Other library to consider:
#   Pandas:
#   https://pandas.pydata.org/
#       Full Data analysis library, can work with almost any tabular data type.
#       Runs visualizations and analysis.
#       Teached in various data science course.
#
#   Openpyxl
#       Designed specially for excel files
#       Retain a lot of Excel specific functionality
#       Supports Excel formulas
#
#   Google Sheets Python API
#       Direct python interface for working with google spreadsheets.
#       Allows you to directly make changes to the spreadsheets hosted online.
#       More complex syntax but available in many programming languages.


# THE COMMON FACTOR BETWEEN ALL OF THESE SPREADHSEETS PROGRAMS IS THAT THEY
# CAN ALWAYS EXPORT TO .CSV FILE.
# LET'S EXPLORE PYTHON BUILT-IN CSV MODULE!

import csv
# open the file
data = open('example.csv', encoding='utf-8')
# csv.reader
cvs_data = csv.reader(data)
# csv.reformat it into python objects list of lists
data_lines = list(cvs_data)
print(data_lines[0])
print(len(data_lines)) # 1000 data points and first line is header

for line in data_lines[:5]:
    print(line) 


print(data_lines[2][3])
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
    
print(all_emails)


full_names = []
for line in data_lines[1:15]:
    full_names.append(f"{line[1]} {line[2]}")

print(full_names)

file_to_output = open('output.csv', 'w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['Full Name', 'Email'])
for i in range(len(full_names)):
    csv_writer.writerow([full_names[i], all_emails[i]])

file_to_output.close()










