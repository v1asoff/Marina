import requests
from bs4 import BeautifulSoup


def world_cup_A():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[1:5]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_B():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[6:10]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_C():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[11:15]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_D():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[16:20]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_E():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[21:25]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_F():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[26:30]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_G():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[31:35]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_H():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('tr')[36:40]

    table = {}

    for places in info:
        place = places.find(class_='plc').text
        team = places.find('a', rel='nofollow').text
        games = places.find('td', class_='ctr').text
        points = places.find('b').text

        table[place] = {
            'place': place,
            'team': team,
            'games': games,
            'points': points
        }
    return table


def world_cup_stats():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all("tr")[49:54]

    table = {}
    cnt = 0

    for places in info:
        cnt += 1
        name = places.find('a').text
        goals = places.find('td', class_='bkcenter').text

        table[cnt] = {
            'name': name,
            'goals': goals
        }
    return table


def world_cup_timetable1():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[:16]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable2():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[16:32]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable3():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[32:48]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable4():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[48:56]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable_quarterfinal():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[56:60]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable_semifinals():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[60:62]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table


def world_cup_timetable_final():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://soccer365.ru/competitions/742/shedule/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all('div', class_='game_block')[63:64]

    table = {}

    for events in info:
        uid = events.find(class_='game_link').get('dt-id')
        date = events.find('span').text.strip()
        home = events.find(class_='result').next_element.next_element.next_element.next_element.text.strip()
        away = events.find(class_='at').find('span').text.strip()
        score_home = events.find(class_='ht').find(class_='gls').text.strip()
        score_away = events.find(class_='at').find(class_='gls').text.strip()
        match = f"{home} - {away} ({score_home}:{score_away})"
        print(match)

        table[uid] = {
            'date': date,
            'match': match
        }
    return table
