import requests
from bs4 import BeautifulSoup
import json


def epl():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://ru.soccerway.com/national/england/premier-league/20222023/regular-season/r69471/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr', class_='team_rank')

    epl = {}

    for places in info:
        place = places.find('td').text.strip()
        team = places.find('a').text.strip()
        points = places.find(class_='number points').text.strip()
        games = places.find(class_='number total mp').text.strip()

        epl[team] = {
            'place': place,
            'team': team,
            'points': points,
            'games': games
        }

    with open('Marina/tournaments/epl.json', 'w', encoding='utf-8') as file:
        json.dump(epl, file, indent=4, ensure_ascii=False)


def check_updates_epl():
    with open("Marina/tournaments/epl.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://ru.soccerway.com/national/england/premier-league/20222023/regular-season/r69471/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr', class_='team_rank')

    epl = {}
    fresh_table = {}

    for places in info:
        place = places.find('td').text.strip()

        if places in news_dict:
            continue
        else:
            team = places.find('a').text.strip()
            points = places.find(class_='number points').text.strip()
            games = places.find(class_='number total mp').text.strip()

            epl[team] = {
                'place': place,
                'team': team,
                'points': points,
                'games': games
            }

            fresh_table[team] = {
                'place': place,
                'team': team,
                'points': points,
                'games': games
            }

    with open("Marina/tournaments/epl.json", "w", encoding='utf-8') as file:
        json.dump(epl, file, indent=4, ensure_ascii=False)

    return fresh_table


def main():
    epl()
    # check_updates_epl()


if __name__ == '__main__':
    main()
