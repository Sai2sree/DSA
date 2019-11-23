"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv


def get_telephone_numbers(calls, telephone_numbers, index):
    for i in calls:
        telephone_numbers.append(i[index])
    return telephone_numbers


def get_call_details(telephone_numbers, calls):
    for i in telephone_numbers:
        call_duration = 0
        for j in calls:
            if i in j:
                call_duration += int(j[3])
        call_details.append((i, call_duration))
    return call_details


def get_longest_call(call_details):
    print(call_details[0])
    longest_call = 0
    for i in call_details:
        if i[1] > longest_call:
            longest_call = i[1]
            telephone_number = i[0]
    return telephone_number, longest_call


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telephone_numbers = []
    call_details = []
    get_telephone_numbers(calls, telephone_numbers, 0)
    get_telephone_numbers(calls, telephone_numbers, 1)
    telephone_numbers = set(telephone_numbers)
    get_call_details(telephone_numbers, calls)
    telephone_number, longest_call = get_longest_call(call_details)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    telephone_number, str(longest_call)))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
