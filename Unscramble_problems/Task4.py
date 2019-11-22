"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telemarketers = []
    for i in calls:
        if i[0].startswith('140'):
            telemarketers.append(i[0])
    telemarketers = list(set(telemarketers))
    telemarketers.sort()
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
