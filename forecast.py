import requests
import ontology as ont
from distance import levenshtein as lev

class Forecaster:

    def __init__(self, url_to_forecast):
        # Initiate the forecast object and get forecast data
        self.job_ssyk, job_forecastId  = self.__forecast_init()
        
        

    def __forecast_init(self):
        """ Helper method to initiate the forecast object.
        Returns a dictionary with ....
        """
        # If we don't send in url to get forecast data
        if not url_to_forecast:
            # Use this link manually
            request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalArea/forcastsRefs/list')
        else:
            # Use given URL
            requests = requests.get(url_to_forecast)

        # Avoid brekage if URL data is not correct
        try:
            # Read the data as json
            data = request.json()
        except:
            # If URL is not correct, return None
            return None

        # Ge through each jobtitle and create two dicts
        # job_to_ssyk : job_title -> ssyk
        # job_to_prognosis_id : job_title -> prognosis_id
        for job in data[0]["occupationPrognosisRefs"]:
            job_to_ssyk[job['heading'].lower()] = job['ssyk']
            job_to_prognosis_id[job['heading'].lower()] = job['prognosisId']
            

        return job_to_ssyk, job_to_prognosis_id

    def get_standard_job_names( self, job_name ):
        """ Take a non-standnard job name (not in taxonomy)
        and matches it to most similar job name in taxonomy """
        # The Job -> Ssyk dictionary
        ssyk = self.job_to_ssyk

        # The jobtitle we are trying to match
        job_to_match = job_name

        # The score for the best match
        # Start with a hundread to make sure we match
        best_match = 100.0
        
        # The match(es) for that job
        matches = []

        for job_title in ssyk.keys():
            # Split the title and clean it
            for word in job_title.split():
                w = word.strip(".,-_'* ")

                if lev(w, job_to_match) < best_match:
                    best_match = lev(w, job_to_match)
                    matches = [job_title]
                elif lev(w, job_to_match) == best_match:
                    matches.append(job_title)

        # Return matching jobs
        return matchesa

    def get_best_standard_job_name(self, job_name):
        """ Return the job which has the best match to the
        job we compare against. """

        # FIX: Currently we only return the first match
        # NOT THE BEST MATCH!
        
        matching_jobs = self.get_standard_job_names( job_name )
        try:
            # Assume the first job is the best (this is bad)
            return matching_jobs[0]
        except:
            # Escape and return None if false
            return None

    def get_short_term_prognosis( self, ssyk_number, output_format ):
        """ Return the short term prognosis for a given
        ssyk_number. 

        """
        # A dictionary to change from whether we want text or number
        options = { 'text' :
                    { 'now' : 'assessmentNowText',
                      'one' : 'assessment1yearText'},
                    'number' :
                    { 'now' : '',
                      'one' : ''}
                    }

        # If we can't find the output option in the given output
        # formats return None
        if options.get(output_format, -1) == -1:
            return None
        
        # Get the data for the ssyk
        request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/shortTerm/{}'.format(ssyk))

        # NOTE: The below is done in serveral places, break out
        # into its own method?
        # Convert to json
        try:
            request_json = request.json()
        except:
            # Make sure it works
            return None

        # Get which format we want the output in
        now_out_format = options[output_format]['now']
        one_out_format = options[output_format]['one']

        # Get the demand for the given format
        now = request_json[0][now_out_format]
        one_year = request_json[0][one_out_format]

        return now, one_year

    def get_long_term_prognosis( self, ssyk_number, output_format ):
        """ Given ssyk_number returns the long term (five year)
        prognosis in output format given as output_format """

        # A dictionary to change from whether we want text or number
        options = { 'text' :
                    { 'five' : 'assessment5YearText'},
                    'number' :
                    { 'five' : ''}
        }

        # If we can't find the output option in the given output
        # formats return None
        if options.get(output_format, -1) == -1:
            return None
        
        request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/longTerm/{}'.format(ssyk))

        # NOTE: The below is done in serveral places, break out
        # into its own method?
        # Convert to json
        try:
            request_json = request.json()
        except:
            # Make sure it works
            return None

        # Get which format we want the output in
        now_out_format = options[output_format]['five']

        # Get current demand and future demand in text format
        five_year = request_json[0][now_out_format]

        return five_year

if __name__ == '__main__':
    search_text = input("Describe what you want to work with: ")

    # Get the best job match
    job = ont.get_top_job(search_text)

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
    current_demand, one_year_demand = get_short_term_prognosis( best_job_ssyk )
    five_year_demand = get_long_term_prognosis( best_job_ssyk )

    print("The prognosis for finding a job as a {} is: \n".format(best_job_match))
    print("Current demand: {}".format(current_demand))
    print("One year demand: {}".format(one_year_demand))
    print("Five year demand: {}".format(five_year_demand))
