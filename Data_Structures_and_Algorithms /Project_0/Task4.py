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

# SET A: create set of people that make outgoing calls

# SET B: create set of people that send texts, receive texts, and receive incoming calls

# SET R: create set of results 
    # If person is in SET A but NOT in SET B then add to SET C

def solution():
    people_outgoing_calls = set()
    criteria = set()
    results = set()

    for call in calls:
        people_outgoing_calls.add(call[0]) # make outgoing call
        criteria.add(call[1]) # receive incoming calls

    for text in texts:
        criteria.add(text[0]) # send text
        criteria.add(text[1]) # receive text

    for caller in people_outgoing_calls:
        if(caller not in criteria):
            results.add(caller)

    print("These numbers could be telemarketers: ")
    for result in results:  
        print(f"{result}")

solution()


