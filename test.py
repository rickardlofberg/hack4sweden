import sys
import json
from app import app
from app.backend import interface
from app.backend import ontology
from app.backend import meetup
from app.backend import forecast

def interface_test():
    # Run this code for debugging
    s = interface.SearchInterface()
    
    while True:
        query = input("What would you like to search for? (Enter 'q' to quit)  ")

        if query == "q": 
            print("Thank you for using our service! Goodbye ")
            break

        # Search for query
        s.search_job( query )

        # Print results
        print("You searched for: {}".format(s.latest_query))
        print()
        print("Matching jobs are:")
        for job in s.top_jobs:
            print(job)
        print()
        print("Best match in taxonomy is: {}".format(s.taxonomy_job))
        print("The current prognosis for job is: {}".format(s.current_year_forecast))
        print("The one year prognosis for job is: {}".format(s.one_year_forecast))
        print("The five year prognosis for job is: {}".format(s.five_year_forecast))
        print()

        r = json.dumps(s.meetup_events)
        jsonObjectInfo = json.loads(r)
        print("Showing events located in {0}".format(jsonObjectInfo["city"]["city"]))
        for eachJsonObject in jsonObjectInfo['events']:
            print("Event name:  {0}".format(eachJsonObject["name"]))
            print("Event date:  {0}".format(eachJsonObject["local_date"]))
            #print("Meetup description:  {0}".format(eachJsonObject["description"]))   OPTIONAL - CURRENT DISABLED DUE TO ALOT OF TEXT OUTPUT
            print("Link to meetup:  {0}".format(eachJsonObject["link"]))
            print()
            print("-----------------**************---------------")
            print()

def ontology_test():
        # Terms to seach for
    search_text = input("What would you like to search for? ")

    jobs = ontology.get_possible_jobs(search_text)

    jobs.sort(key=lambda x: x[1], reverse=True)

    for job in jobs:
        print(job)
    
    if not jobs:
        print("We couldn't find a job to match your skills, try something different!")

def meetup_test():
    text = input("What do you want to find? ")

    events = meetup.get_events(text)

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

def forecast_test():
    search_text = input("Describe what you want to work with: ")

    # Get the best job match
    job = ontology.get_top_job(search_text)

    if len(job) == 0:
        print("Unfortunatly we didn't find a match")
        exit

    # Get job to ssyk to dictionary
    job_to_ssyk = get_jobs_to_ssyk()

    # Get the best profession fro job match
    best_job_match = best_profession_job_name_match( job_to_ssyk, job )

    # Get the ssyk for our "top match"
    best_job_ssyk = job_to_ssyk[best_job_match]

    # Get short term prognosis
    current_year_demand = get_prognosis( best_job_ssyk, 'now' )
    one_year_demand = get_prognosis( best_job_ssyk, 'one' )
    five_year_demand = get_prognosis( best_job_ssyk, 'five' )

    print("The prognosis for finding a job as a {} is: \n".format(best_job_match))
    print("Current demand: {}".format(current_demand))
    print("One year demand: {}".format(one_year_demand))
    print("Five year demand: {}".format(five_year_demand))
    print()

tests = {'int' : interface_test,
         'ont' : ontology_test,
         'met' : meetup_test,
         'for' : forecast_test}

if __name__ == '__main__':
    # If we have an arg
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # If it is correct arg
        if tests.get(arg, -1) != -1:
            tests[arg]()
        else:
            print("You need to give one of the following arguments: \nint \nont \nmet \nfor")
    else:
        print("You need to give one of the following arguments: \nint \nont \nmet \nfor")

            

