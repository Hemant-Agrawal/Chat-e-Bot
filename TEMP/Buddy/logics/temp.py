pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Chattybot and I'm a chatbot ", ]
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
        r"i'm(.*| doing) (good|fine|alright|ok)",
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
        r"(.*) created ?",
        ["GLA Buddies created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(quit|exit|bye|get lost)",
        ["BBye take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"Number of (teacher|teachers) in bca department",
        ["Currently there are 32 teachers in BCA department ", ]
    ],
    [
        r"which company has (highest|high|max|great) placement ?",
        ["Capgemini has the highest placement as it recruits more than 60 students last year", ]
    ],
    [
        r"Last year placement in (.*) ?",
        ["Last year placement in  %1 is 1", "Last year placement in  %1 is 43", "Last year placement in  %1 is 23", "Last year placement in  %1 is 3",]
    ],
    [
        r"Placement in year (.*) ?",
        ["Placement in year %1 is 143", "Placement in year %1 is 184", "Placement in year %1 is 175",
         "Placement in year %1 is 168", ]
    ],
    [
        r"Average Package of (.*)",
        ["Average Package of %1 is 3.6 lakh p.a.", "Average Package of %1 is 2.4 lakh p.a.",
         "Average Package of %1 is 3.0 lakh p.a.", "Average Package of %1 is 2.15 lakh p.a.", ]
    ],
    [
        r"Criteria Of (.*)",
        ["Criteria Of %1 is 6.0", "Criteria Of %1 is 65", ]
    ],
    [
        r"Last year placement ?",
        ["SAP labs :- 1<br>Capgemini :- 43<br>Wipro :- 37", ]
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