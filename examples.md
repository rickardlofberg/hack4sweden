
# Table of Contents

1.  [Dependecy install](#orgb42f795)
2.  [Examples of running ontology.py](#org47d7853)
3.  [Examples of running forecast.py](#org0757e9e)
4.  [Examples of running meetups.py](#orgacba218)


<a id="orgb42f795"></a>

# Dependecy install

    pip install requests
    pip install distance


<a id="org47d7853"></a>

# Examples of running ontology.py

    python ontology.py 
    What would you like to search for? jag vill jobba med djur
    ('djurvårdare', 0.88835)
    ('personlig assistent', 0.88429)
    ('veterinär', 0.88363)
    ('smådjursskötare', 0.8534360220193862)
    ('distriktsveterinär', 0.84416)
    ('djursjukskötare', 0.84254)
    ('assistent', 0.82636)
    ('djurskötare', 0.81057)
    ('mjölkbonde', 0.7994144934158178)
    ('smågrisskötare', 0.7961384149933194)
    ('djuruppfödare', 0.7837233956048464)
    ('fjäderfäskötare', 0.7703286341891962)
    ('rökare', 0.76773)
    ('djurskyddshandläggare', 0.74137)
    ('svinskötare', 0.7386281626421483)
    ('grönsaksodling', 0.7318677313934263)
    ('hunddagisfröken', 0.7295494675425186)
    ('slakteriarbetare', 0.7292180788532757)
    ('jordbruksarbetare', 0.7246199424109089)
    ('hundskötare', 0.7121193986607802)


<a id="org0757e9e"></a>

# Examples of running forecast.py

    python forecast.py 
    Describe what you want to work with: djur människor
    The prognosis for finding a job as a vårdare och boendestödjare is: 
    
    Current demand: Liten konkurrens
    One year demand: Liten konkurrens
    Five year demand: Balans


<a id="orgacba218"></a>

# Examples of running meetups.py

Note that you need to add your won API file called `meetup_key.py` with your key assigned to the varible `my_key`.

    python meetup.py
    What do you want to find? java
    🚀 Effective Java Software Design for Developers | Stockholm, April
    <p>➡️ Information and tickets: <a href="http://bit.ly/2pKjYBA" class="linkified">http://bit.ly/2pKjYBA</a> ⬅️</p> <p>Do you want to feel proud of your work? Write code that your colleagues will admire? Move fast without compromising quality? Build long-living software that is easy and fun to maintain? Get out of technical debt without big upfront time investment? Professionally articulate technical decisions to your team and management? Build remarkable engineering career?</p> <p>Then this training is for you.</p> <p>During this intensive, practical and entertaining 2-day workshop you will learn principles, practices and patterns for writing readable, maintainable and effective code.</p> <p>Highlights<br/>✅ The course is based on real-world project code, stories and examples<br/>✅ The course includes practical Lab work<br/>✅ The course is updated to support Java 8/9/10 and functional programming idioms<br/>✅ The course will show many frameworks in action including Spring, Hystrix and others<br/>✅ The course runs in a small group with a lot of discussion and experience exchange<br/>✅ Attendees will receive optional coding assignment for skill polishing. Homework will be reviewed and supplemented by constructive feedback.</p> <p>Coverage<br/>✅ Understanding the economics of software design (clean code rationale, design entropy, busting "quality is expensive" myth, consequences of bad code)<br/>✅ Design principles, rules, laws and dilemmas (use-reuse paradox, specific-generic dilemma, Law of Demeter, KISS, SOLID, DRY, YAGNI, just-enough design)<br/>✅ Effective Naming (principle of least astonishment, command-query separation, eliminating getters and setters, side-effects)<br/>✅ Effective Conditionals (how and when to avoid branching, how to eliminate nested branching, making branching easy-to-read)<br/>✅ Effective Functions (nulls vs. optionals, single level of abstraction, step-down rule, lambda or not to lambda?)<br/>✅ Effective Classes (OO meets functional, objects vs. data structures, abstraction, coupling, cohesion)<br/>✅ Effective Comments (when and how to avoid, alternatives)<br/>✅ Effective Application/Service Layer (commands, reactions, funnels)<br/>✅ Effective Domain modeling (DDD, protecting invariants, value objects, entities, aggregates, event bus, strong and eventual consistency)<br/>✅ Effective Persistence (transaction management, unit of work pattern, DAO vs. repository, testing data)<br/>✅ Effective Validation (simple and complex rule validation, why Bean Validation sucks, writing custom validator)<br/>✅ Effective Exception Handling (when and how to handle exceptions, designing exception hierarchy, checked vs. unchecked)<br/>✅ Effective Resilience (failure modes, responding to failures, stability patterns, Hystrix)<br/>✅ Effective Concurrency (CompletableFuture, RxJava, testing concurrency and asynchrony)<br/>✅ How to stay clean and move fast (incremental refactoring, effective code reviews, pairing, CoPs, brown-bags, quality forecasting with Sonar)<br/>✅ … and much more!</p> <p>➡️ Information and tickets: <a href="http://bit.ly/2pKjYBA" class="linkified">http://bit.ly/2pKjYBA</a> ⬅️</p> 
    Stockholm
    .
    .
    .

