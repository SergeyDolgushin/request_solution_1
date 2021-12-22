from pprint import pprint

import requests


TOKEN = "2619421814940190"
names = ["Hulk", "Captain America", "Thanos"]
request_type = ["search", "id"]
request_stats = ["powerstats", "biography"] 

def id_request(name, request_type, TOKEN = "2619421814940190"):

    url = "https://superheroapi.com/api/" + TOKEN +"/" + request_type + "/" + name
    response = requests.get(url)
    return response

def return_ids(names, request_type = request_type[0]):
    names_ids = {}
    for name in names:
        responce = id_request(name, request_type)
        names_ids[f'{name}'] = f'{responce.json()["results"][0]["id"]}' 
        
    return names_ids

def return_stats(names_ids: dict, request_stats = request_stats[0], TOKEN = "2619421814940190"):
    names_intel = {}
    for name in names_ids:
        url = "https://superheroapi.com/api/" + TOKEN +"/" + names_ids[name] + "/" + request_stats
        responce = requests.get(url)
        names_intel[f'{name}'] = f'{responce.json()["intelligence"]}'
    return names_intel    

def compare_stats(names_stats: dict):
    sorted_names = sorted(names_stats.items(), key = lambda i: i[1])
    return sorted_names[0]


if __name__ == '__main__':
    
    
    # names_ids = {'Captain America': '149', 'Hulk': '332', 'Thanos': '655'}
    # names_intel = {'Captain America': '69', 'Hulk': '88', 'Thanos': '100'}
    names_ids = return_ids(names)
    print(names_ids)
    names_stats_intel = return_stats(names_ids)
    print(names_stats_intel)
    print(compare_stats(names_stats_intel))
