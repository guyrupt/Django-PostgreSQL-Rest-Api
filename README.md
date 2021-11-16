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

#### {host:port}/companyloc/{company}

Purpose: get all location of a specific company 

Request: GET http://127.0.0.1:8000/companyloc/Google

Response Sample:

````
[
    {
        "location_name": "Atlanta, GA"
    },
    {
        "location_name": "Austin, TX"
    },
    {
        "location_name": "Bangalore, KA, India"
    },
    {
        "location_name": "Belo Horizonte, MG, Brazil"
    },
]

````
#### {host:port}/companylevel/{company}/{location}

Purpose: get all levels of a specific company in {location}

Request: GET http://127.0.0.1:8000/companylevel/Google/San Francisco, CA

Response Sample:

````
[
    {
        "level_name": "L5"
    },
    {
        "level_name": "L6"
    },
]

````

#### {host:port}/companytag/{company}/{location}/{level}

Purpose: get all tags of a specific company in {location} with level of {level}

Request: GET http://127.0.0.1:8000/companytag/Google/San Francisco, CA/L5

Response Sample:

````
[
    {
        "tag_name": "Android"
    },
    {
        "tag_name": "API Development (Back-End)"
    },
]

````

### POST

#### {host:port}/search

Purpose: get list of employee with requested conditions

Request must be in JSON form and must contain **["company", "location", "level", "tag"]**. 

The values of **["company", "location", "level", "tag"]** can be null,
but if any previous item is null, the value should be null.

For example, the following is fine:

````
{
        "company" : null,
        "location" : null,
        "level" : null,
        "tag" : null
}
````

This is fine as well:

````
{
        "company" : "Google",
        "location" : "Taiwan",
        "level" : null,
        "tag" : null
}
````

BUT THESE ARE NOT:

```
{
        "company" : null,
        "location" : null,
        "level" : null,
        "tag" : "Embedded Systems" // SHOULD BE SET null
}
```
```
{
        "company" : "Google",     
        "location" : null,
        "level" : "L5",           // SHOULD BE SET null 
        "tag" : null 
}
```
Request: POST http://127.0.0.1:8000/search

Request Body:

````
{
        "company" : "Google",
        "location" : "Taiwan",
        "level" : "l6",
        "tag" : "embedded"
}
````

Response Sample:

```
[
    {
        "id": 5173,
        "company": {
            "company": "Google",
            "icon_url": "https://logo.clearbit.com/google.com"
        },
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
    }
]
```

## To Start Frontend

After setting up the django server, run

    cd frontend
    npm install

then,

    npm run dev

The webpage is on http://localhost:3000
