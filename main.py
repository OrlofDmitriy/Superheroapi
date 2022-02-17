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
    intelligence = int(intelligence)

    return intelligence


def comparison_intellects_of_heroes(heroes):
    intelligence_dict = {}

    for hero in heroes:
        hero_intelligence = get_hero_intelligence(hero)
        intelligence_dict[hero] = hero_intelligence

    smartest_hero = max(intelligence_dict, key=intelligence_dict.get)

    print(f'Самый умный - {smartest_hero}')


heroes = ['Hulk', 'Captain America', 'Thanos']
comparison_intellects_of_heroes(heroes)
