import requests
from bs4 import BeautifulSoup


def ligue1():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/18/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[1:21]

    ligue1_table = {}

    for places in info:
        place = places.find('div').text.strip()
        team = places.find('a').text.strip()
        games = places.find('a').next_element.next_element.next_element.text.strip()
        points = places.find('b').text.strip()

        ligue1_table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points,
        }

    return ligue1_table