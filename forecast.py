import requests
import ontology as ont
from distance import levenshtein as lev

def get_jobs_to_ssyk():
    """ Returns a dictionary with job titles as key_words and the
    ssyk id as value. And a dictionary with job title as key_words
    and prognosisID as value """
    job_to_ssyk = dict()
    #job_to_progons_id = dict()
    
    # Get all the information
    request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalArea/forcastsRefs/list')

    # Convert to data
    data = request.json()
    
    # Go through this table
    for job in data[0]["occupationPrognosisRefs"]:
        # Get the heading (job title) and ssykn
        job_to_ssyk[job['heading'].lower()] = job['ssyk']

        # break out into other function
        # Get the heading (job title) and prognosisId
        #job_to_progons_id[job['heading'].lower()] = job['prognosisId']

    # This should possibly be broken into two functions
    #return job_to_ssyk, job_to_progons_id
    
    return job_to_ssyk

    

def best_profession_job_name_match( job_to_ssyk, job_name ):
    # The Job -> Ssyk dictionary
    ssyk = job_to_ssyk

    # The jobtitle we are trying to match
    job_to_match = job_name

    # The score for the best match
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

    # Return the FIRST MATCH, IT SHOULD RETURN THE BEST MATCH!
    # This needs to be updated...
    if len(matches) != 0:
        return matches[0]
    
    # Return the matches for the search
    return matches

def get_short_term_prognosis( ssyk ):
    request = requests.get('http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/shortTerm/{}'.format(ssyk))

    # Convert to json
    request_json = request.json()

    # Get current demand and future demand in text format
    now = request_json[0]["assessmentNowText"]
    one_year = request_json[0]["assessment1yearText"] 
    
    return now, one_year

def get_long_term_prognosis( ssyk ):    
    pass

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

    print("
    
    
    # Get longterm and shortterm prognosis
    print(best_job_match)

""""
http://api.arbetsformedlingen.se:80/af/v2/forecasts/occupationalGroup/shortTerm/221            

            
print(matches)
print(best_match)
"""
