import requests
from meetup_key import my_key

text = input("What do you want to find? ")
radius = "50"
key = my_key             

data = requests.get("https://api.meetup.com/find/upcoming_events?&key={}&sign=true&photo-host=public&page=20&text={}&radius={}".format(key, text, radius))

events = data.json()
eventsFound = False

for event in events["events"]:
    try:
        print(event["name"])
        print(event["description"])
        print(event["venue"]["city"])
        eventsFound = True
        print()
    except:
        continue

if not eventsFound:
    print("No matching events found")
