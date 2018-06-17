import json
from app.backend import ontology

def load_queries(q_file):
    with open(q_file,"r") as rf:
        queries=json.load(rf)
    return queries
queries=load_queries("sample.json")
keywords=queries["keywords"]

def test_function(func_name,input):
    print("Function "+str(func_name.__name__)+" for "+str(input)+" returns:")
    result=func_name(input)
    print(result)
    return result

#Test query in each function
print("These are the queries we will test:"+str(keywords))

all_skills=[]
for query in keywords:
    #Test find_skills and find_occupations on each query
    possible_skills=test_function(ontology.find_skills,query)
    all_skills.append(possible_skills)
    test_function(ontology.find_occupations,query)
    #Once the skills are found test find_jobs_related_to_skill
    possible_skills=ontology.find_skills(query)
    test_function(ontology.find_jobs_related_to_skill,possible_skills)

print("***Conclusion:***")
print("You tested "+str(len(all_skills))+" queries")

skill_counts=[]
for skill_list in all_skills:
    skill_counts.append(len(skill_list))
from collections import Counter
skill_counts=Counter(skill_counts)

#Show the number of queries that return a certain number of skill_list
#for instance:
#find_skills had 3 queries that matched 2 skill(s)
#find_skills had 4 queries that matched 1 skill(s)
for key in skill_counts:
    print("find_skills had "+str(skill_counts[key]) + " queries that returned " + str(key) + " skill(s)")


#TODO: same loop for the sentences
