pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "Ronaldo", "Roony"]
    ],
    [
        r"(quit|exit|bye|get lost)",
        ["BBye take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"Open Youtube",
        ["Opening"]
    ],
    [
        r"Number of (teacher|teachers) in bca department",
        ["SELECT COUNT(NAME) from teachers", ]
    ],
    [
        r"which company has (highest|high|max|great) placement ?",
        ["SELECT company,package from Buddy_student where package = (Select max(package) from Buddy_student)", ]
    ],
    [
        r"Last year placement in (.*) ?",
        ["SELECT count(student_name) from Buddy_student where company = '%1'", ]
    ],
    [
        r"Placement in year (.*) ?",
        ["Select count(student_name) from Buddy_student where placed_year = '%1'",
         "Select company,count(student_name) from Buddy_student where Year ='%1' GROUP by company"]
    ],
    [
        r"Average Package of (.*)",
        ["SELECT company, avg(package) from Buddy_student where company = '%1'"]
    ],
    [
        r"Criteria Of (.*)",
        ["SELECT company_name,criteria from Buddy_company where company_name = '%1'", ]
    ],
    [
        r"Last year placement ?",
        ["SELECT company,count(student_name) from Buddy_student GROUP BY company", ]
    ],
    [
        r"(Companies|company) (of BCA|visited Till today|of last year|till|.* )",
        ["SELECT company_name from Buddy_company", ]
    ],
    [
        r"(Core|main) (Companies|company) (of BCA|visited Till today|of last year|till )",
        ["SELECT company_name from Buddy_company where is_core=True ", ]
    ],
    [
        r"(.*)",
        ["Please provide some more info", "Sorry!, Try Another", "Sorry!, But will find it out soon",
         "Sorry!, Not able to understand ", "Sorry!, Try Again", ]
    ]
]