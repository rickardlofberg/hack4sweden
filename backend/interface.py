import forecast
import ontology


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

        # If we have correct results
        if len(self.top_jobs) > 0:
            # Set the top job
            self.top_job = self.top_jobs[0][0]
            # Get the best matching job in taxonomy
            self.taxonomy_jobs = self.forecaster.get_standard_job_name( self.top_job )
            # Get the first job in list
            self.taxonomy_job = self.taxonomy_jobs[0]

            self.ssyk = self.forecaster.job_ssyk[self.taxonomy_job]

            self.current_year_forecast, self.one_year_forecast = self.forecaster.get_short_term_prognosis( self.ssyk )
            self.five_year_forecast = self.forecaster.get_long_term_prognosis( self.ssyk )

        # HERE WE SHOULD ALSO UPDATE THE FORECAST
        # AND MEETUP STUFF



if __name__ == '__main__':
    # Run this code for debugging
    s = SearchInterface()
    
    while True:
        query = input("What would you like to serach for? ")

        # Search for query
        s.search_job( query )

        # Print results
        print("You searched for: {}".format(s.latest_query))
        print("Matching jobs are:")
        for job in s.top_jobs:
            print(job)
        print()
        print("Best match in taxonomy is: {}".format(s.taxonomy_job))
        print("The current prognosis for job is: {}".format(s.current_year_forecast))
        print("The one year prognosis for job is: {}".format(s.one_year_forecast))
        print("The five year prognosis for job is: {}".format(s.five_year_forecast))
        print()
