import json
import csv
import re

# text = "  Hello World!  "

# #? Remove whitespace
# text.strip()  # "Hello World!"
# text.lstrip()  # "Hello World!  "
# text.rstrip()  # "  Hello World!"

# #? Change case
# text.lower()  # "  hello world!  "
# text.upper()  # "  HELLO WORLD!  "
# text.title()  # "  Hello World!  "

# #? Replace
# text.replace('World', 'Python')  # "  Hello Python!  "

# #? Split into list
# text.split()  # ['Hello', 'World!']
# "a,b,c".split(',')  # ['a', 'b', 'c']

# #? Join list into string
# words = ['Hello', 'World']
# ' '.join(words)  # "Hello World"

# #? Check contents
# 'Hello' in text  # True
# text.startswith('  H')  # True
# text.endswith('!')  # True

# #? Remove characters
# text.strip().replace('!', '')  # "Hello World"

# #? Format strings (f-strings)
# name = "Alice"
# age = 25
# message = f"{name} is {age} years old"



#?----------------------------------------------------------------
#? --------------------File Handling------------------------------
#?-----------------------------------------------------------------

# txt = "  Hello World!!!!!  "

# file_path = "sample.txt"

# try:
#     with open(file=file_path, mode='a') as file:          #? open file in write mode, 'r' to read , 'r+' to read and write
#         file.write("\n" + txt)                            #? 'x' to create new file, 'a' to append , 'r' to read
#         print(f"File {file_path} written successfully.")
# except FileExistsError:
#     print("File already exists.")


# employees = ["John Doe", "Jane Smith", "Alice Johnson"]

# file_path = "employees.txt"

# try:
#     with open(file=file_path, mode='w') as file:
#         for employee in employees:             #? Write each employee name on a new line
#             file.write(employee + "\n")
#         print(f"Employee data written to {file_path}.")
# except FileExistsError:
#     print("File already exists.")


# ------ D I C T I O N A R Y   M E T H O D S ------

# employee = {
#     "name": "John Doe",
#     "job": "Developer",
#     "age": 30,
# }

# file_path = "employee.json"


##? json dump to write dictionary to json file
# try:
#     with open(file=file_path, mode='w') as file:
#         json.dump(employee, file, indent=4)               #? Write dictionary (employee, file, indent=4 for pretty print)
#         print(f"Employee data written to {file_path}.")
# except FileExistsError:
#     print("File already exists.")


##? json load to read from json file
# try:
#     with open(file=file_path, mode='r') as file:
#         data = json.load(file)
#         print("Employee data read from file:")
#         print(data)
# except FileNotFoundError:
#     print("File not found.")


#?-------------------------------------------------
#? ----------- C S V   M O D U L E ----------------
#?-------------------------------------------------
#TODO - CSV (Comma Separated Values) module
#TODO - CSV files are text files where each line represents a row, and fields are separated by commas.

# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 25, "New York"],
#     ["Bob", 30, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]

# file_path = "data.csv"

# try:
#     with open(file=file_path, mode='w', newline='') as file: #? Open file in write mode, newline='' to avoid extra blank lines
#         writer = csv.writer(file) #? Create a CSV writer object to write to the file
#         for row in data:
#             writer.writerow(row)  #? Write each row to the CSV file
#         print(f"Data written to {file_path}.")
# except FileExistsError:
#     print("File already exists.")


#? read from csv file
# file_path = "data.csv"
# try:
#     with open(file=file_path, mode='r') as file:
#         reader = csv.reader(file)  #? Create a CSV reader object to read from the file
#         for row in reader:
#             print(row)  #? Print each row read from the CSV file
# except FileNotFoundError:
#     print("File not found.")


# #?-----------------------------------------------------
# #? R E G U L A R   E X P R E S S I O N S (R E G E X)
# #?-----------------------------------------------------

#TODO - Regular Expressions (Regex) are sequences of characters that form search patterns, mainly for string pattern matching.

#? Note
# re.search(pattern, text)                   #? finds pattern anywhere
# re.match(pattern, text)                    #? matches only at start
# re.fullmatch(pattern, text, re.IGNORECASE) #? matches entire string and ignore case
# re.findall(pattern, text)                  #? returns all matches as a list
# re.sub(r"\s+", " ", text)                  #? replace multiple spaces with single space
# pattern = r"(?:com|org|net)"               #? for matching 'com', 'org', or 'net'
 


# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)"  #? list pattern to match email addresses

# user_input = input("Enter your email address: ")

# if re.fullmatch(pattern, user_input): #? check full string match
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


#? replace specific part of string
# pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"  #? Pattern to match phone numbers in the format XXX-XXX-XXXX
# new_pattern = r"\1\2\3"                   #? New pattern to replace dashes with dots
# user_input = input("Enter your phone number: ")
# new_user_input = re.sub(pattern, new_pattern, user_input) #?(pattern, replacement, string) substitute dashes with nothing
# print("Formatted phone number:", new_user_input)


# pattern = r"^(\d{3})-(\d{3})-(\d{4})$"  #? 'r' before string makes it a raw string 
#                                         #? ^ start of string, $ end of string
#                                         #? \d{3} exactly 3 digits
                                        
# user_input = input("Enter your phone number: ")

# if re.fullmatch(pattern, user_input):                         #? check full string match
#     new_user_input = re.sub(pattern, r"\1.\2.\3", user_input) #? substitute dashes with dots
#     print("Formatted phone number:", new_user_input)
# else:
#     print("Invalid format — expected XXX-XXX-XXXX")


































