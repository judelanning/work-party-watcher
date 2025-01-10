import json

import requests

base_url = "https://www.wta.org/volunteer/schedule/workparties.json?"

response = requests.get(base_url)

def get_events(url):
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()

            print(f"{len(data['results']['all_items'])} work parties fetched.")
        except:
            print("Did not receive valid JSON, aborting script now.")
    
    else:
        print(f"Request failed with status code: {response.status_code}")

get_events(base_url)
