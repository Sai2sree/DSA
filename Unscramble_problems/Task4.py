"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def get_text_telephone_numbers(texts):
    text_telephone_numbers = []
    for i in texts:
        text_telephone_numbers.append(i[0])
        text_telephone_numbers.append(i[1])
    return set(text_telephone_numbers)


def get_telemarketers(calls):
    answering_numbers = []
    incoming_numbers = []
    for i in calls:
        answering_numbers.append(i[1])
        incoming_numbers.append(i[0])
    answering_numbers = set(answering_numbers)
    incoming_numbers = set(incoming_numbers)
    telemarketers = list(incoming_numbers -
                         answering_numbers - text_telephone_numbers)
    telemarketers.sort()
    return telemarketers


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    text_telephone_numbers = get_text_telephone_numbers(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telemarketers = get_telemarketers(calls)
    print("These numbers could be telemarketers: ")
    for i in telemarketers:
        print(i)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
