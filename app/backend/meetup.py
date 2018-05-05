import requests
from meetup_key import my_key

def get_events( text ):
    key = my_key             
    radius = "50"
    data = requests.get("https://api.meetup.com/find/upcoming_events?&key={}&sign=true&photo-host=public&page=20&text={}&radius={}".format(key, text, radius))

    events = data.json()
    eventsFound = False
    return events

if __name__ == '__main__':
    text = input("What do you want to find? ")
    events = get_events(text,radius)

    for event in events["events"]:
        try:
            print(event["name"])
            #print(event["description"])    CURRENT DISABLED DUE TO ALOT OF TEXT OUTPUT
            print(event["venue"]["city"])
            eventsFound = True
            print()
        except:
            continue

    if not eventsFound:
        print("No matching events found")
