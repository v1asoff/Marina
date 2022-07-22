import requests
from bs4 import BeautifulSoup
import json


def laliga():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://ru.soccerway.com/national/spain/primera-division/20222023/regular-season/r69450/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr', class_='team_rank')

    laliga = {}

    for places in info:
        place = places.find('td').text.strip()
        team = places.find('a').text.strip()
        points = places.find(class_='number points').text.strip()
        games = places.find(class_='number total mp').text.strip()

        laliga[team] = {
            'place': place,
            'team': team,
            'points': points,
            'games': games
        }

    with open('Marina/tournaments/laliga.json', 'w', encoding='utf-8') as file:
        json.dump(laliga, file, indent=4, ensure_ascii=False)


def check_updates_laliga():
    with open("Marina/tournaments/laliga.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://ru.soccerway.com/national/spain/primera-division/20222023/regular-season/r69450/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr', class_='team_rank')

    laliga = {}
    fresh_table = {}

    for places in info:
        place = places.find('td').text.strip()

        if places in news_dict:
            continue
        else:
            team = places.find('a').text.strip()
            points = places.find(class_='number points').text.strip()
            games = places.find(class_='number total mp').text.strip()

            laliga[team] = {
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

    with open("Marina/tournaments/laliga.json", "w", encoding='utf-8') as file:
        json.dump(laliga, file, indent=4, ensure_ascii=False)

    return fresh_table


def main():
    laliga()
    check_updates_laliga()


if __name__ == '__main__':
    main()
