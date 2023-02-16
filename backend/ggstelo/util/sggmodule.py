import requests
from decouple import config

headers = {"Authorization": "Bearer " + config(
    "API_KEY"), "Content-Type": 'application/json'}

# A simple function to use requests.post to make the API call. Note the json= section.


def run_query(query, variables):
    request = requests.post(url='https://api.start.gg/gql/alpha',
                            json={'query': query, 'variables': variables}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}".format(
            request.status_code))
