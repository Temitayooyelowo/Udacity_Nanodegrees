"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def solution():
    unique_telephone_numbers = set()

    for val in texts:
        unique_telephone_numbers.add(val[0])
        unique_telephone_numbers.add(val[1])

    for val in calls:
        unique_telephone_numbers.add(val[0])
        unique_telephone_numbers.add(val[1])

    print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")

solution()