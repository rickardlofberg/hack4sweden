import requests
import json

def find_skills( key_words ):
    # The response from keywords
    response = requests.post('http://ontologi.arbetsformedlingen.se/ontology/v1/text-to-structure', data=key_words)

    # Covert to json
    response = response.json()

    # List of skills
    skills = []
    
    for match in response:
        if match["type"] == "skill":
            skills.extend(match['terms'])

    return skills

def find_occupations( key_words ):
# The response from keywords
    response = requests.post('http://ontologi.arbetsformedlingen.se/ontology/v1/text-to-structure', data=key_words)

    # Covert to json
    response = response.json()

    # List of skills
    occupations = []
    for match in response:
        if match["type"] == "occupations":
            skills.extend(match['terms'])

    return occupations

def find_jobs_related_to_skill( skills ):
    # List of tupples with job title and match percentange
    possible_jobs = []
        
    for skill in skills:
        url = "http://ontologi.arbetsformedlingen.se/ontology/v1/skill/{}/related/occupation".format(skill)
        data = requests.get(url).json()

        for job in data["relations"]:
            possible_jobs.append((job["name"].lower(), job["score"]))

    return possible_jobs

def find_jobs_related_to_occupation( occupation ):

    # List of tupples with job title and match percentange
    possible_jobs = []
 
    for occupation in occupations:
        url = "http://ontologi.arbetsformedlingen.se/ontology/v1/skill/{}/related/occupation".format(occupation)
        data = requests.get(url).json()
    
        for job in data["relations"]:
            possible_jobs.append((job["name"].lower(), job["score"]))

    return possible_jobs

def get_possible_jobs( search_text ):
    # Get possible skills and occupations
    possible_skills = find_skills(search_text)
    possible_occupation = find_occupations(search_text)

    # Find jobs related to skill
    possible_jobs = find_jobs_related_to_skill(possible_skills)
    # Find jobs related to occupation
    possible_jobs.extend(find_jobs_related_to_skill(possible_occupation))

    return possible_jobs

def get_top_job( search_text ):
    # Return the top matching job from search
    jobs = get_possible_jobs(search_text)

    # Sort by relevance
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Make sure we have a match
    if len(jobs) > 0:
        return jobs[0][0]
    else:
        return None
    
if __name__ == '__main__':
    # Terms to seach for
    search_text = input("What would you like to search for? ")

    jobs = get_possible_jobs(search_text)

    jobs.sort(key=lambda x: x[1], reverse=True)

    for job in jobs:
        print(job)

