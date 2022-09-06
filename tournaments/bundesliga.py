import requests
from bs4 import BeautifulSoup


def bundesliga():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/17/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[1:19]

    bundesliga_table = {}

    for places in info:
        place = places.find('div').text.strip()
        team = places.find('a').text.strip()
        games = places.find('a').next_element.next_element.next_element.text.strip()
        points = places.find('b').text.strip()

        bundesliga_table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points,
        }

    return bundesliga_table