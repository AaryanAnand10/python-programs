#For a Text file
--> Reading a File:-
with open("text.txt",w) as file_object:
  rd=file_object.reader()
  
#For a Binary file
--> Reading a File:-
with open('binary_file.bin', 'rb') as file:
    (Read the entire content of the file)
    binary_data = file.read()


#For CSV file:-
-->Readind a File:-
import csv
csv_file_path = 'your_file.csv'
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
