import requests

url = 'https://superheroapi.com/api/2619421814940190/'
my_list = ['Hulk', 'Captain America', 'Thanos']


def super_hero(list_name):
    max_intelligence = 0
    for name in list_name:
        res = requests.get(url + 'search/' + name)
        if int(res.json()['results'][0]['powerstats']['intelligence']) > max_intelligence:
            max_intelligence = int(res.json()['results'][0]['powerstats']['intelligence'])
            name_max_intelligence = name
    print (f'Самый умный {name_max_intelligence}')


super_hero(my_list)
