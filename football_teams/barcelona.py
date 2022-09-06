import requests
from bs4 import BeautifulSoup


def barcelona_calendar():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/clubs/12/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')

    calendar_barcelona = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        tournament = events.find(class_='cmp').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"

        calendar_barcelona[uid] = {
            'date': date,
            'tournament': tournament,
            'match': match
        }

    return calendar_barcelona


# live_barcelona = ['(100:100)']
#
#
# def barcelona_match():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#     }
#
#     url = 'https://soccer365.ru/clubs/12/'
#     response = requests.get(url=url, headers=headers)
#     bs = BeautifulSoup(response.text, 'lxml')
#     info = bs.find('div', id='game-next').find('a', class_='game_link').get('href')
#
#     url = 'https://soccer365.ru/' + str(info)
#     response = requests.get(url=url, headers=headers)
#     bs = BeautifulSoup(response.text, 'lxml')
#     informations = bs.find_all('div', class_='block_body_nopadding padv15 live')
#
#     for info in informations:
#         time = info.find('div', class_='live_game_status').find('b').text
#         vs = f"{info.find('div', class_='live_game_ht').find('a').text} - {info.find('div', class_='live_game_at').find('a').text}"
#         score = f"({info.find('div', class_='live_game left').find('span').text}:{info.find('div', class_='live_game right').find('span').text})"
#         live_barcelona.append(score)
#
#         match = f"<i>{time}</i> | {vs} <b>{score}</b>"
#
#         return match, score
