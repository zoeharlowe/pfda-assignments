# assignment02-bankholdidays.py
# This program will print out the dates of the bank holidays in Northern Ireland
# I will also modify the the program to print out the bank holidays that are unique to Northern Ireland
# Author: Zoe McNamara Harlowe

# Import the requests and json libraries
import requests
import json

# Get the JSON data from the UK government website
url="https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Create variable for Northern Ireland events. I sliced the data to only include Northern Ireland events
ni_events = data['northern-ireland']['events']

# Print statement to introduce list of holidays
print("The dates of all bank holidays in Northern Ireland are as follows: ")
      
for event in ni_events: # For loop to print out dates of NI bank holidays
    date = event['date']
    print(date)

# Now I want to find the holidays unique to Northern Ireland
# I used Stack Overflow to help me with this part of the code https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# Create variables for England and Wales and Scotland events
ew_events = data['england-and-wales']['events']
scot_events = data['scotland']['events']

# Create empty list to store unique NI bank holidays
unique_ni = []

for ni_event in ni_events: # For loop to check if NI event is in EW or Scotland events
    if ni_event not in ew_events and ni_event not in scot_events:
        unique_ni.append(ni_event) # If NI event is not in EW or Scotland events, add to unique_ni list

# Print statement to introduce list of unique holidays
print("\nThe unique bank holidays in Northern Ireland are as follows: ")
for unique_event in unique_ni: # For loop to print out unique NI bank holidays
    print(f"{unique_event['title']} on {unique_event['date']}")