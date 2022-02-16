import requests


def get_hero_intelligence(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    res = requests.get(url)

    for result in res.json()['results']:
        if result['name'] == f'{name}':
            hero_id = result['id']
        else:
            break

    url = 'https://superheroapi.com/api/2619421814940190/' + hero_id + '/powerstats'
    res = requests.get(url)

    intelligence = res.json()['intelligence']
    return intelligence
