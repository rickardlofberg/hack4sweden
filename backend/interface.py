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
        # The forecast for the standardized job title
        self.taxonomy_job_forecast = []

        # Create Forecaster object.
        self.forecaster = forecast.Forecaster()

    def search_job( self, search_query ):
        """ Searches for a job and update all the relevant
        variables with matching data """

        # Set the lateset search
        self.self.latest_query = search_query

        # Get the top jobs and sort them according to relevance
        self.top_jobs = ontology.get_possible_jobs( search_query )
        self.top_jobs.sort(key=lambda x: x[1], reverse=True)

        # If we have correct results
        if len(self.top_jobs) > 0:
            # Set the top job
            self.top_job = top_jobs[0][0]
            # Get the best matching job in taxonomy
            self.taxonomy_job = self.forecaster.get_best_standard_job_name( self.top_job )

            # HERE WE SHOULD ALSO UPDATE THE FORECAST
            # AND MEETUP STUFF
        
