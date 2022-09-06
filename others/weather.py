import requests
from bs4 import BeautifulSoup


def weather_zheldor():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://www.gismeteo.ru/weather-zheleznodorozhny-10907/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all(class_='section section-content section-bottom-collapse')

    weather_info = {}

    for wet in info:
        weather = wet.find('a', class_='weathertab weathertab-link tooltip').get('data-text')
        temperature_indication = wet.find('span', class_='sign').text.strip()
        temperature = wet.find('span', class_='sign').next_element.next_element.text.strip()

        weather_info = {
            'weather': weather,
            'temperature_indication': temperature_indication,
            'temperature': temperature
        }

    return weather_info


def weather_moscow():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    url = 'https://www.gismeteo.ru/weather-moscow-4368/'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    info = bs.find_all(class_='section section-content section-bottom-collapse')

    weather_info = {}

    for wet in info:
        weather = wet.find('a', class_='weathertab weathertab-link tooltip').get('data-text')
        temperature_indication = wet.find('span', class_='sign').text.strip()
        temperature = wet.find('span', class_='sign').next_element.next_element.text.strip()

        weather_info = {
            'weather': weather,
            'temperature_indication': temperature_indication,
            'temperature': temperature
        }

    return weather_info
