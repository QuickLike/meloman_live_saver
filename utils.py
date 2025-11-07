import re

from bs4 import BeautifulSoup
from getpass import getpass
import requests

from constants import LOGIN_URL, LOGIN_HEADERS, LOGIN_FORM, USERNAME, PASSWORD, MAIN_URL


def check_live_link(link: str):
    pattern = (r'https://records\.meloman\.facecast\.net/files/[a-zA-Z0-9\-\_]{22}/0/(KZCH|F2|KZF)/('
               r'meloman|facecast)/[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-HD-(KZCH|F2|KZF)\.mp4')
    if re.match(pattern, link) is None:
        raise ValueError('Некорректная ссылка!')


def authorize(username: str = None, password: str = None) -> requests.Session | None:
    if username is None:
        username = input('Введите ваш E-Mail:\n')
    if password is None:
        password = getpass('Введите ваш пароль:\n')

    session = requests.Session()
    session.auth = (username, password)
    resp = session.get(MAIN_URL, headers=LOGIN_HEADERS)
    soup = BeautifulSoup(resp.text, 'lxml')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'username': username,
        'password': password,
    }
    print(username, password)
    login_response = session.post(
        LOGIN_URL,
        data=dict(**LOGIN_FORM, **login_data),
        headers=LOGIN_HEADERS,
        allow_redirects=True,
    )
    login_response.raise_for_status()
    if login_response.ok:
        print("Вход выполнен успешно!")
        return session
    else:
        print("Ошибка входа.")


if __name__ == '__main__':
    authorize(USERNAME, PASSWORD)
    # check_live_link(input('Ссылка:\n'))
