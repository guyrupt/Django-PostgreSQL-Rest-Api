# Django PostgreSQL Rest Api

Prereqs: Python 3.9

Clone this repo, then in the directory run

    pipenv install

If pipenv is not installed, run `pip install pipenv`

Run `pip -V` to make sure you are on virtual environment, output should be like

```
pip 21.2.4 from {your_user_dir}\.virtualenvs\imdb_mid_project-ybDDyv4O\lib\site-packages\pip (python 3.9)
```

If you are not on virtual environment, run `pipenv shell`

To run server, run the following

`python manage.py runserver`

## Database

The database of this project is on the Azure cloud, which means you **DO NOT** need to setup local database and import data. You can access the database directly with password.

To monitor the database with pgAdmin

Click **Add New Server** on the main page of pgAdmin

Name can be whatever

Hostname/address is **imdb-midterm-postgres.postgres.database.azure.com**

The password of the DB server is **!Password**

![](https://i.gyazo.com/57f5a53d4438f17e927336bb41731acb.png)

**DO NOT EXECUTE DJANGO MIGRATE WITHOUT PERMISSION**

**THIS IS A MUTUAL DATABASE**

## APIs

### GET

#### {host:port}/location/{location}

for _location_, type in USPS Abbreviation for states in U.S., other countries type in full country name.

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

#### {host:port}/company/

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

#### {host:port}/locations/

Purpose: get all location 

Request: GET http://127.0.0.1:8000/locations

Response Sample:

````
[
    {
        "location_name": "1A Coruna, GA, Spain"
    },
    {
        "location_name": "Aachen, NW, Germany"
    },
]
````
#### {host:port}/companylevels/{company}/

Purpose: get all levels of a specific company

Request: GET http://127.0.0.1:8000/companylevels/Google

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

#### {host:port}/tags/

Purpose: get all tags 

Request: GET http://127.0.0.1:8000/tags

Response Sample:

````
[
    {
        "tag_name": "5g"
    },
    {
        "tag_name": "aa"
    },
]

````

### POST

#### {host:port}/search

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

## To Start Frontend

Prereqs: Nodejs

After setting up the django server, run

    cd frontend
    npm install

then,

    npm run dev

The webpage is on http://localhost:3000
