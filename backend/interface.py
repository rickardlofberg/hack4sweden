import forecast
import ontology
import meetup
import json


class SearchInterface:

    def __init__(self):
        """ An interface which keeps the latest query
        in memory while waiting for a new query """

        # Keep track of the latest query
        self.latest_query = ''

        # A list of the top jobs and their relevance
        self.top_jobs = []
        # The "Top job" match we got
        self.top_job = ''
        # The standardized job title
        self.taxonomy_job = ''
        # Set SSYK for taxonomy job
        self.ssyk = ''        
        # The forecast for the standardized job title
        self.current_year_forecast = ''
        self.one_year_forecast = ''
        self.five_year_forecast = ''
        # Meetup events based on matched job tittle 
        self.meetup_events = ''

        # Create Forecaster object.
        self.forecaster = forecast.Forecaster()

    def search_job( self, search_query ):
        """ Searches for a job and update all the relevant
        variables with matching data """

        # Set the lateset search
        self.latest_query = search_query

        # Get the top jobs and sort them according to relevance
        self.top_jobs = ontology.get_possible_jobs( search_query )
        self.top_jobs.sort(key=lambda x: x[1], reverse=True)

        # Geet meetup events using matched job tittle
        self.meetup_events = meetup.get_events(search_query)

        # If we have correct results
        if len(self.top_jobs) > 0:
            # Set the top job
            self.top_job = self.top_jobs[0][0]
            # Get the best matching job in taxonomy
            self.taxonomy_jobs = self.forecaster.get_standard_job_name( self.top_job )
            # Get the first job in list
            self.taxonomy_job = self.taxonomy_jobs[0]

            self.ssyk = self.forecaster.job_ssyk[self.taxonomy_job]

            self.current_year_forecast = self.forecaster.get_prognosis( self.ssyk, option='now' )
            self.one_year_forecast = self.forecaster.get_prognosis( self.ssyk, option='one' )
            self.five_year_forecast = self.forecaster.get_prognosis( self.ssyk, option='five' )



        # HERE WE SHOULD ALSO UPDATE THE FORECAST



if __name__ == '__main__':
    # Run this code for debugging
    s = SearchInterface()
    
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
