# Examples of the code

This is a proof of concept on how we can query the different API:s to combine the data and get results.


# Table of Contents

1.  [Dependecy install](#orgb42f795)
2.  [Examples of running interface.py](#org47d7853)


<a id="orgb42f795"></a>

# Dependecy install

    pip install requests
    pip install distance


<a id="org47d7853"></a>

# Examples of running interface.py

    python interface.py 

    What would you like to search for? (Enter 'q' to quit)  python
    You searched for: python

    Matching jobs are:

    ('linuxguru', 0.8447319496011734)('mjukvaruutvecklare', 0.805481334954387)
    ('telekomtestare', 0.7965281548511152)
    ('testutvecklare', 0.7921523748331608)
    ('testare', 0.774033054051613)
    ('telekomingenjör', 0.7525120593308326)
    ('embeddedutvecklare', 0.723416141666541)
    ('systemutvecklare', 0.7199068329784994)
    ('bioinformatiker', 0.7093540194537394)
    ('testingenjör', 0.705553363149956)
    ('programmerare', 0.7050607894873395)
    ('systemprogrammerare', 0.6975021655052821)
    ('prestandatestare', 0.6942216705693716)
    ('teknisk testare', 0.6934168960758689)
    ('civilingenjör', 0.67055)
    ('nätverksingenjör', 0.6561321006392251)
    ('spelutvecklare', 0.6555580760315858)
    ('javaprogrammerare', 0.6482095428476315)
    ('postdoktoral forskare', 0.6463688958700884)
    ('mjukvarutestare', 0.6453797394751866)

    Best match in taxonomy is: mjukvaru- och systemutvecklare
    The current prognosis for job is: Mycket liten konkurrens
    The one year prognosis for job is: Mycket liten konkurrens
    The five year prognosis for job is: Mycket liten konkurrens

    Showing events located in Stockholm
    Event name:  GDG April 2018
    Event date:  2018-04-26
    Link to meetup:  https://www.meetup.com/Stockholm-Google-Developer-Group/events/249464612/

    -----------------**************---------------

    Event name:  How to start your network automation journey!
    Event date:  2018-05-03
    Link to meetup:  https://www.meetup.com/Network-Automation-Stockholm/events/249190532/

    -----------------**************---------------

    Event name:  Oracle Tech Talk - JavaScript Running In Your Oracle DB!
    Event date:  2018-05-15
    Link to meetup:  https://www.meetup.com/Stockholm-Oracle/events/249627422/

    -----------------**************---------------

# How to exit interface.py
    
    What would you like to search for? (Enter 'q' to quit)  q
    Thank you for using our service! Goodbye

