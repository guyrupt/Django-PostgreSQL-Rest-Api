# SWE EXPLORE APP

Prereqs: Python 3.9

## Quick Installation Guide

### 1. Start Django Backend

Clone this repo, then in the directory run

    pipenv install

If pipenv is not installed, run `pip install pipenv`

Run `pip -V` to make sure you are on virtual environment, output should be like

```
pip 21.2.4 from {your_user_dir}\.virtualenvs\imdb_mid_project-ybDDyv4O\lib\site-packages\pip (python 3.9)
```

If you are not on virtual environment, run `pipenv shell`

To run server, run the following

    python manage.py runserver

## 2. Monitor Database (Optional)

You **DO NOT** need to set up your local database for this App.

The database of this project is on the Azure cloud and the data has already been imported.

Also, the connection to the database is already hard-coded. 

To monitor the database with pgAdmin,

Click **Add New Server** on the main page of pgAdmin.

Name can be whatever.

Hostname/address is **imdb-midterm-postgres.postgres.database.azure.com**.

The password of the DB server is **!Password**.

![](https://i.gyazo.com/57f5a53d4438f17e927336bb41731acb.png)

**DO NOT MODIFY/DJANGO MIGRATE TO DATABASE WITHOUT PERMISSION**

**THIS IS A MUTUAL DATABASE**

### 3. Start Frontend

This project has two frontend with different features and UI. 

Prereqs: Nodejs 14+

#### Frontend 1: Svelte + Tailwind CSS

After setting up the django server, run

    cd frontend_svelte
    npm install

then,

    npm run dev

The webpage is on http://localhost:3001

#### Frontend 2: React

Prereqs: Nodejs, Yarn

After setting up the django server, run

    cd frontend_syl
    yarn

then,

    yarn start

The webpage is on http://localhost:3000

## APIs

### GET

#### ```/location/<location>```

Params: for _location_, type in USPS Abbreviation for states in U.S., other countries type in full country name.

Purpose: get all employee data in a specific location

Request: GET http://127.0.0.1:8000/location/taiwan

Response Sample:

    [
        {
            "id": 5173,
            "company": {'company': 'Google', 'icon_url': 'https://logo.clearbit.com/google.com'},
            "location": "Taipei, TP, Taiwan",
            "tag": "Embedded Systems",
            "level": "L6",
            "gender": "male",
            "race": "Asian",
            "academic_level": "Doctorate (PhD)",
            "timestamp": "2021-08-26T18:10:05Z",
            "yearsofexperience": 11,
            "yearsatcompany": 9,
            "totalyearlycompensation": 276,
            "base_salary": 148,
            "stockgrantvalue": 90,
            "bonus": 38,
            "remote": false
        },
        {
            "id": 10165,
            "company": {'company': 'Nvidia', 'icon_url': 'https://logo.clearbit.com/nvidia.com'},
            "location": "Taipei, TP, Taiwan",
            "tag": "System",
            "level": "IC5",
            "gender": "null",
            "race": "null",
            "academic_level": "null",
            "timestamp": "2021-06-26T13:32:55Z",
            "yearsofexperience": 13,
            "yearsatcompany": 13,
            "totalyearlycompensation": 270,
            "base_salary": 178,
            "stockgrantvalue": 93,
            "bonus": 0,
            "remote": false
        }
    ]

#### ```/company/```

Params: none
    
Purpose: get all companies 

Request: GET http://127.0.0.1:8000/company

Response Sample:

````

[
    {
        "id": 769,
        "company_name": "1Password",
        "icon_url": "https://logo.clearbit.com/1password.com"
    },
    {
        "id": 560,
        "company_name": "2U",
        "icon_url": "https://logo.clearbit.com/2u.com"
    },
]
````

#### ```/companyloc/<company>```

Params: company name for **company**
    
Purpose: get all location 

Request: GET http://127.0.0.1:8000/companyloc/netflix

Response Sample:

````
[
    {
        "location_name": "Amsterdam, NH, Netherlands"
    },
    {
        "location_name": "Los Angeles, CA"
    },
]
````
#### ```companylevel/<company>/<location>```

Params: company name for **company** and its **location**
    
Purpose: get all levels of a specific company in the location

Request: GET http://127.0.0.1:8000/companylevel/google/taiwan

Response Sample:

````
[
    {
        "level_name": "3"
    },
    {
        "level_name": "4"
    },
]

````

#### ```companytag/<company>/<location>/<level>```

Params: company name for **company** and its **location** and the **level** of the job
    
Purpose: get all tags of a specific company in the location with certain level

Request: GET http://127.0.0.1:8000/companytag/google/taiwan/l5

Response Sample:

````
[
    {
        "tag_name": "Data"
    },
    {
        "tag_name": "DevOps"
    },
    {
        "tag_name": "Full Stack"
    }
]

````

#### ```/companystats/<company>```

Params: company name for **company**

Purpose: get gender, race, academic level, salary stats of company

Request: GET http://127.0.0.1:8000/companystats/netflix

Response Sample:

````
[
    {
        "count": 61,
        "company": {
            "id": 33,
            "company_name": "Netflix",
            "icon_url": "https://logo.clearbit.com/netflix.com"
        },
        "gender": {
            "null": 21,
            "male": 32,
            "female": 8,
            "other": 0
        },
        "race": {
            "null": 26,
            "White": 24,
            "Asian": 6,
            "Hispanic_Latino": 1,
            "Two_or_More_Races": 1,
            "Black_or_African_American": 3,
            "Native_Hawaiian_or_Other_Pacific_Islander": 0,
            "American_Indian_or_Alaska_Native": 0
        },
        "academic_level": {
            "null": 16,
            "Master": 14,
            "Bachelor": 23,
            "Doctorate_PhD": 4,
            "Some_college_coursework_completed": 2,
            "High_school_or_equivalent": 2,
            "Technical_or_occupational_certificate": 0,
            "Associate_Degree": 0
        },
        "levels": [
            {
                "level_name": "No level",
                "avg_salary": {
                    "totalyearlycompensation__avg": 700.0
                }
            },
            {
                "level_name": "L5",
                "avg_salary": {
                    "totalyearlycompensation__avg": 562.5
                }
            },
            {
                "level_name": "Senior Software Engineer",
                "avg_salary": {
                    "totalyearlycompensation__avg": 558.5892857142857
                }
            },
            {
                "level_name": "L6",
                "avg_salary": {
                    "totalyearlycompensation__avg": 540.0
                }
            },
            {
                "level_name": "Only one level across Netflix",
                "avg_salary": {
                    "totalyearlycompensation__avg": 435.0
                }
            }
        ],
        "totalyearlycompensation": {
            "totalyearlycompensation__avg": 558.7049180327868
        }
    }
]
````

### POST

#### ```/search```

Purpose: get list of employee with requested conditions

Request must be in JSON form and must contain **["company", "location", "level", "tag"]**. 

Request: POST http://127.0.0.1:8000/search

Request Body:

````
{
        "company" : "Google",
        "location" : null,
        "level" : "l6",
        "tag" : null
}
````

Response Sample:

```
[
    {
        "id": 3898,
        "company": {
            "company": "Google",
            "icon_url": "https://logo.clearbit.com/google.com"
        },
        "location": "Mountain View, CA",
        "tag": "Distributed Systems (Back-End)",
        "level": "Manager (L6)",
        "gender": "male",
        "race": "Asian",
        "academic_level": "Doctorate (PhD)",
        "timestamp": "2021-09-10T22:34:15Z",
        "yearsofexperience": 8,
        "yearsatcompany": 8,
        "totalyearlycompensation": 849,
        "base_salary": 224,
        "stockgrantvalue": 535,
        "bonus": 89,
        "remote": false
    },
    {
        "id": 8869,
        "company": {
            "company": "Google",
            "icon_url": "https://logo.clearbit.com/google.com"
        },
        "location": "Sunnyvale, CA",
        "tag": "Distributed Systems (Back-End)",
        "level": "L6",
        "gender": "male",
        "race": "Asian",
        "academic_level": "Master",
        "timestamp": "2021-07-14T20:14:25Z",
        "yearsofexperience": 18,
        "yearsatcompany": 5,
        "totalyearlycompensation": 600,
        "base_salary": 270,
        "stockgrantvalue": 240,
        "bonus": 90,
        "remote": false
    },
]
```
