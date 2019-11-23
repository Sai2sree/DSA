"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def getTelephoneNumbers(data, index, telephone_numbers):
    for i in data:
        telephone_numbers.append(i[index])
    return telephone_numbers


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    telephone_numbers = []
    getTelephoneNumbers(texts, 0, telephone_numbers)
    getTelephoneNumbers(texts, 1, telephone_numbers)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    getTelephoneNumbers(calls, 0, telephone_numbers)
    getTelephoneNumbers(calls, 1, telephone_numbers)

print("There are {} different telephone numbers in the records.".format(str(len(set(telephone_numbers)))))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
