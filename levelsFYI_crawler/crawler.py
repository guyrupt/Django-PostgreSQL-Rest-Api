import requests
import os
import json
import time

'''
row_key = ['uuid', 'timestamp', 'company', 'level', 'title', 'totalyearlycompensation', 
'location', 'yearsofexperience', 'yearsatcompany', 'tag', 'basesalary', 'stockgrantvalue', 
'bonus', 'gender', 'otherdetails', 'cityid', 'dmaid']

company_key = ['name', 'icon', 'registered']

'''

data_dir = "./data"
out_path = "levelsFYI.json"

url = "https://api.levels.fyi/v1/salaries?title=Software+Engineer&limit=10&orderDesc=true&searchText=&sortBy=timestamp"

r = requests.get(url)
data_size = int(r.json()["total"])
print(data_size)

query = "https://api.levels.fyi/v1/salaries?title=Software+Engineer&limit=100&orderDesc=true&searchText=&sortBy=timestamp"



uuids = set()
data = []

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

for i in range(0, data_size, 100):
    next_token = i
    q = query + "&nextToken=" + str(next_token)
    r = requests.get(q)
    print(i, "status code: " + str(r.status_code))
    rows = r.json()["rows"]

    # ensure each row of data is unique
    for j in range(0, len(rows)):
        if rows[j]["uuid"] not in uuids:
            uuids.add(rows[j]["uuid"])
            data.append(rows[j])

    ### to avoid http 429 too many requests
    # time.sleep(0.1)

print("total: " + str(len(data)))

with open(os.path.join(data_dir , out_path), "w") as f:
    json.dump(data, f)

