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

Demo:

Request: GET http://127.0.0.1:8000/location/taiwan

Response Sample:

    [
        {
            "id": 5173,
            "company": "{'company': 'Google', 'icon_url': 'https://logo.clearbit.com/google.com'}",
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
            "company": "{'company': 'Nvidia', 'icon_url': 'https://logo.clearbit.com/nvidia.com'}",
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

#### {host:port}/company/{company name}

Demo:

Request: GET http://127.0.0.1:8000/company/google

Response Sample:

    [
        {
            "id": 13,
            "timestamp": "2021-10-25T05:56:07Z",
            "yearsofexperience": 7,
            "yearsatcompany": 2,
            "totalyearlycompensation": 400,
            "base_salary": 165,
            "stockgrantvalue": 200,
            "bonus": 35,
            "remote": false,
            "location": null,
            "tag": null,
            "level": null,
            "gender": null,
            "race": null,
            "academic_level": null
        },
        {
            "id": 818,
            "timestamp": "2021-10-15T23:36:03Z",
            "yearsofexperience": 6,
            "yearsatcompany": 0,
            "totalyearlycompensation": 389,
            "base_salary": 200,
            "stockgrantvalue": 159,
            "bonus": 30,
            "remote": false,
            "location": null,
            "tag": null,
            "level": null,
            "gender": null,
            "race": null,
            "academic_level": null
        }
    ]

> Ref: https://art-of-engineer.blogspot.com/2021/06/python-django-postgresql-rest-api.html
