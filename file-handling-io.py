#For a Text file
--> Reading a File:-
with open("text.txt",w) as file_object:
  rd=file_object.reader()


#For a Binary file
--> Reading a File:-
with open('binary_file.bin', 'rb') as file:
    (Read the entire content of the file)
    binary_data = file.read()

  Example for a binary code to read and display its contents:
import struct

# Write binary data to a file
with open('binary_data.bin', 'wb') as binary_file:
    binary_file.write(struct.pack('iid', 123, 45.67, 89.12))

# Read binary data from the file
with open('binary_data.bin', 'rb') as binary_file:
    data = struct.unpack('iid', binary_file.read())

# Display the data
labels = ["Integer", "Float 1", "Float 2"]
for label, value in zip(labels, data):
    print(f"{label}: {value}")


#For CSV file:-
-->Readind a File:-
import csv
csv_file_path = 'your_file.csv'
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
