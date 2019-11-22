"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telephone_numbers = []
    for i in calls:
        if i[0].startswith('(080)'):
            telephone_numbers.append(i[1])
    #telephone_numbers = set(telephone_numbers)
    area_codes = []
    bglr_nums = 0
    for i in telephone_numbers:
        if i.startswith('(0'):
            area_code = i.split(')')[0][1:]
            area_codes.append(area_code)
            if area_code == '080':
                bglr_nums += 1
        else:
            area_codes.append(i[:4])
print("The numbers called by people in Bangalore have codes:")
unique_area_codes = list(set(area_codes))
unique_area_codes.sort()
for i in unique_area_codes:
    print(i)

print(str(round(bglr_nums/len(area_codes)*100, 2)) +
      " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
