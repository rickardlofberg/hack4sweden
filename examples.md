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
    What would you like to search for? (Enter 'q' to quit)  java
    You searched for: java

    Matching jobs are:
    ('linuxguru', 0.9258593948650359)
    ('telekomtestare', 0.9074716854570961)
    ('javautvecklare', 0.9029529547592746)
    ('systemutvecklare', 0.8925645504196595)
    ('oracleutvecklare', 0.8444964547099132)
    ('civilingenjör', 0.84185)
    ('konsult', 0.8409)
    ('stordatorutvecklare', 0.8328582106322282)
    ('applikationstestare', 0.8283292636778933)
    ('prestandatestare', 0.8214184550290827)
    ('testare', 0.8190786462390438)
    ('webutvecklare', 0.81313)
    ('testmiljöansvarig', 0.807343012498905)
    ('mjukvaruutvecklare', 0.7941990835235038)
    ('telekomingenjör', 0.7914571245904709)
    ('applikationsutvecklare', 0.7818355718971925)
    ('programmerare', 0.780691190192452)
    ('it konsult', 0.77526)
    ('javaprogrammerare', 0.7676595568530793)
    ('integrationstestare', 0.7627938268655171)

    Best match in taxonomy is: mjukvaru- och systemutvecklare
    The current prognosis for job is: Mycket liten konkurrens
    The one year prognosis for job is: Mycket liten konkurrens
    The five year prognosis for job is: Mycket liten konkurrens

    Meetup events near you: {'city': {'id': 1037701, 'city': 'Stockholm', 'lat': 59.33, 'lon': 18.07, 'state': '', 'country': 'se', 'zip': 'meetup1', 'member_count': 3302}, 'events': [{'created': 1522072740000, 'duration': 118800000, 'fee': {'accepts': 'cash', 'amount': 1199.0, 'currency': 'EUR', 'description': '', 'label': 'Price', 'required': False}, 'id': '249120194', 'name': '🚀 Effective Java Software Design for Developers | Stockholm, April', 'status': 'upcoming', 'time': 1524726000000, 'local_date': '2018-04-26', 'local_time': '09:00', 'updated': 1522413664000, 'utc_offset': 7200000, 'waitlist_count': 0, 'yes_rsvp_count': 6, 'venue': {'id': 23677443, 'name': 'Informator', 'lat': 59.33544158935547, 'lon': 18.099149703979492, 'repinned': False, 'address_1': 'Karlavägen 108', 'city': 'Stockholm', 'country': 'se', 'localized_country_name': 'Sweden'}, 'group': {'created': 1522072471000, 'name': '🚀 Effective Java Training Stockholm', 'id': 27953118, 'join_mode': 'open', 'lat': 59.33000183105469, 'lon': 18.06999969482422, 'urlname': 'Effective-Java-training-Stockholm', 'who': 'Members', 'localized_location': 'Stockholm, Sweden', 'region': 'en_US'}, 'link': 'https://www.meetup.com/Effective-Java-training-Stockholm/events/249120194/', 'description': '<p>➡️ Information and tickets: <a href="http://bit.ly/2pKjYBA" class="linkified">http://bit.ly/2pKjYBA</a> ⬅️</p> <p>Do you want to feel proud of your work? Write code that your colleagues will admire? Move fast without compromising quality? Build long-living software that is easy and fun to maintain? Get out of technical debt without big upfront time investment? Professionally articulate technical decisions to your team and management? Build remarkable engineering career?</p> <p>Then this training is for you.</p> <p>During this intensive, practical and entertaining 2-day workshop you will learn principles, practices and patterns for writing readable, maintainable and effective code.</p> <p>Highlights<br/>✅ The course is based on real-world project code, stories and examples<br/>✅ The course includes practical Lab work<br/>✅ The course is updated to support Java 8/9/10 and functional programming idioms<br/>✅ The course will show many frameworks in action including Spring, Hystrix and others<br/>✅ The course runs in a small group with a lot of discussion and experience exchange<br/>✅ Attendees will receive optional coding assignment for skill polishing. Homework will be reviewed and supplemented by constructive feedback.</p> <p>Coverage<br/>✅ Understanding the economics of software design (clean code rationale, design entropy, busting "quality is expensive" myth, consequencesof bad code)<br/>✅ Design principles, rules, laws and dilemmas (use-reuse paradox, specific-generic dilemma, Law of Demeter, KISS, SOLID, DRY, YAGNI, just-enough design)<br/>✅ Effective Naming (principle of least astonishment, command-query separation, eliminating getters and setters, side-effects)<br/>✅ Effective Conditionals (how and when to avoid branching, how to eliminate nested branching, making branching easy-to-read)<br/>✅ Effective Functions (nulls vs. optionals, single level of abstraction, step-down rule, lambda or not to lambda?)<br/>✅ Effective Classes (OO meets functional, objects vs. data structures, abstraction, coupling, cohesion)<br/>✅ Effective Comments (when and how to avoid, alternatives)<br/>✅ Effective Application/Service Layer (commands, reactions, funnels)<br/>✅ Effective Domain modeling (DDD, protecting invariants, value objects, entities, aggregates, event bus, strong and eventual consistency)<br/>✅ Effective Persistence (transaction management, unit of work pattern, DAO vs. repository, testing data)<br/>✅ Effective Validation (simple and complex rule validation, why Bean Validation sucks, writing custom validator)<br/>✅ Effective Exception Handling (when and how to handle exceptions, designing exception hierarchy, checked vs. unchecked)<br/>✅ Effective Resilience (failure modes, responding to failures, stability patterns, Hystrix)<br/>✅ Effective Concurrency (CompletableFuture, RxJava, testing concurrency and asynchrony)<br/>✅ How to stay clean and move fast (incremental refactoring, effective code reviews, pairing, CoPs, brown-bags, quality forecasting with Sonar)<br/>✅ … and much more!</p> <p>➡️ Information and tickets: <ahref="http://bit.ly/2pKjYBA" class="linkified">http://bit.ly/2pKjYBA</a> ⬅️</p> ', 'visibility': 'public'},
        .
        .
        .

# How to exit interface.py
    
    What would you like to search for? (Enter 'q' to quit)  q
    Thank you for using our service! Goodbye

