import requests
from distance import levenshtein as lev
import app.backend.ontology
import json
import os

class Forecaster:

    def __init__(self):
        # Initiate the forecast object and get forecast data
        self.job_ssyk, self.job_forecastId  = self.__forecast_init()  

    def __forecast_init(self):
        """ Helper method to initiate the forecast object.
        Returns a dictionary with ....
        """
        # job_to_ssyk and job_to_prog dicts
        job_to_ssyk = dict()
        job_to_prognosis_id = dict()

        # Get path to file
        SITE_ROOT = os.path.realpath(os.path.dirname(__name__))
        json_url = os.path.join(SITE_ROOT, "app/static/data", "ssyk.json")

        with open(json_url, 'r') as ssyk_data:
            data = json.load(ssyk_data)

        # Go through each jobtitle and create two dicts
        # job_to_ssyk : job_title -> ssyk
        # job_to_prognosis_id : job_title -> prognosis_id
        for job in data[0]["occupationPrognosisRefs"]:
            job_to_ssyk[job['heading'].lower()] = job['ssyk']
            job_to_prognosis_id[job['heading'].lower()] = job['prognosisId']

        return job_to_ssyk, job_to_prognosis_id

    def get_standard_job_name( self, job_name ):
        """ Take a non-standnard job name (not in taxonomy)
        and matches it to most similar job name in taxonomy """
        # The Job -> Ssyk dictionary
        ssyk = self.job_ssyk

        # The jobtitle we are trying to match
        job_to_match = job_name

        # The score for the best match
        # Start with a hundred to make sure we match
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
        return matches

    def get_prognosis( self, ssyk_number, output_format='text', option='' ):
        """ Given ssyk_number and a time option returns the prognosis for this 
        year (now, one, five years) in output format given as output_format """
        # If the prognosis time option is not available print an error message and return none.
        if option=='five':
            # A dictionary to change from whether we want text or number
            options = { 'text' :
                        { 'five' : 'assessment5YearText'},
                        'number' :
                        { 'five' : 'assessment5Year'}
                        }
            request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/longTerm/{}'.format(ssyk_number))
        elif option=='one':
            options = { 'text' :
                        { 'one' : 'assessment1yearText'},
                        'number' :
                        { 'one' : 'assessment1year'}
                        }
            request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/shortTerm/{}'.format(ssyk_number))
        elif option=='now':
            options = { 'text' :
                        { 'now' : 'assessmentNowText'},
                    'number' :
                    { 'now' : 'assessmentNow'}
                    }
            request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/shortTerm/{}'.format(ssyk_number))
        else:
                print('The prognosis time for', option,'is not available.')
                return None

        # Convert to json
        try:
            request_json = request.json()
        except:
            # Make sure it works
            return None

        
        # Get which format we want the output in
        out_format = options[output_format][option]


        
        # Get current demand and future demand in text format
        year = request_json[0][out_format]
        return year

if __name__ == '__main__':
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
