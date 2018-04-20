# hack4sweden

Hack for Sweden 2018

 **TEAM**: The Breakfast Club <br />
 **Category**: AI have a dream <br />
 **Challenge**: Who Seeks Shall Find
 
 
 Example code not up to date!
 
 [Example of code](./examples.md)
 
 [TODO](./todo.md)
 
 > **“Breaching the gap between newcomers and the job market by providing networking and job forecast.”** <br />

Today it takes about 5 years for a newcomer to become employed in Sweden. A lot can happen in 5 years!
A third of newcomers have an education equal to or higher than high school diploma (they have an easier time finding a job). Today it takes ~5 years to get a job, for newcomers. Social networking can lead to finding relevant contacts within one’s field of work. It also helps developing language skills. So, not only is properly guided job seeking important but so is associative time, where networking can enable connecting with the right people. This can increase better matchmaking between job and skills. We present a service that through user input suggests related occupations to their skills and suggesting meet-ups events related to their interests. This is done through combining Arbetsförmedlingen APIs and an open source API from Meetup.

**Tech:** API Data from Arbetsförmedlingen (Ontologi & Job forcast), SCB and maybe migrationsverket? PHP and python User interface: Javascript, JQuery, Bootstrap

**Target audience:** Job seeking newcomers.

**Mission:**
To facilitate job seeking and enable establishing oneself/family for newcomers in Sweden
Build social networks relevant to skills e.g. Engineers finds engineers

**Vision:**
To decrease the discrimination and increase opportunities for all people in the society
Decrease overqualification on the job market / Matching skills better

**License:** [Creative Commons license](./LICENSE)

# Instructions

To try out the app (launch it locally) do the following:
1. Download the git
2. Unzip and go into directory
3. pip install -r requierments.txt
4. export FLASK_APP=h4s.py
4.1 export FLASK_DEBUG=1 #(For debug mode)
5. flask run
