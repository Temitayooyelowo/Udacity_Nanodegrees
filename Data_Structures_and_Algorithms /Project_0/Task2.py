"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def solution():

    tel_dict = {}
    max_num = None

    for call in calls:
        num_seconds = int(call[3])

        if max_num is None:
            max_num = call[0]

        if(call[0] in tel_dict):
            tel_dict[call[0]] += num_seconds
        else:
            tel_dict[call[0]] = num_seconds

        if(call[1] in tel_dict):
            tel_dict[call[1]] += num_seconds
        else:
            tel_dict[call[1]] = num_seconds

        if(tel_dict[call[0]] > tel_dict[max_num]):
            max_num = call[0]
        if(tel_dict[call[1]] > tel_dict[max_num]):
            max_num = call[1]

    print(
        f"{max_num} spent the longest time, {tel_dict[max_num]} seconds, on the phone during September 2016.")


solution()
