import requests
import csv

# Github api url to fetch repos
BASE_URL = 'https://api.github.com/search/repositories?q=is:public'
response = requests.get(BASE_URL)
list_of_items = list(response.json()['items'])

filtered_list = []
filter_stargazers = []

# TASK-1
"""
{
"language": "Python",
"forks": ">=200"
}

fetch repos with this constraints
"""
for item in list_of_items:
    language = item['language']
    forks = item['forks']

    if language == 'Python' and forks >= 200:
        filtered_list.append({f"language: {item['language']}", f"forks: {item['forks']}"})

# filtered items
print(filtered_list)



# TASK-2
"""
--> Store fetched repositories data into following columns in CSV file
    'name', 'description', 'html_url', 'watchers_count', 'stargazers_count', 'forks_count'
"""

my_file_1 = 'my_file_1.csv'
with open(my_file_1, 'a', newline="") as file:

    # first added column names in the file
    writer = csv.writer(file)
    columns = ('name', 'description', 'html_url', 'watchers_count', 'stargazers_count', 'forks_count')
    writer.writerow(columns)

    for item in list_of_items:

        # required items
        name = item['name']
        description = item['description']
        html_url = item['html_url']
        watchers_count = item['watchers_count']
        stargazers_count = item['stargazers_count']
        forks_count = item['forks_count']

        # created a tuple for each item and appended then into the file
        tuple1 = (name, description, html_url, watchers_count, stargazers_count, forks_count)
        writer.writerow(tuple1)

        # filter_stargazers.append(stargazers_count)



# TASK-3
"""
Store only those repositories which have more than 2000 “stargazers_count”
"""

my_file_2 = 'my_file_2.csv'

column_list = []
for i in list_of_items[0]:
    column_list.append(i)

with open(my_file_2, 'a', newline="") as file:
    column_tuple = tuple(column_list)

    writer = csv.writer(file)
    writer.writerow(column_tuple)
    for item in list_of_items:
        if item['stargazers_count'] > 2000:

            item_list = []
            for i in item:
                item_list.append(item[i])

        item_tuple = tuple(item_list)
        writer.writerow(item_tuple)
