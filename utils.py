import re

from getpass import getpass
import requests

from constants import LOGIN_URL, LOGIN_HEADERS, LOGIN_FORM, USERNAME, PASSWORD


def check_live_link(link: str):
    pattern = (r'https://records\.meloman\.facecast\.net/files/[a-zA-Z0-9\-\_]{22}/0/(KZCH|F2|KZF)/('
               r'meloman|facecast)/[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-HD-(KZCH|F2|KZF)\.mp4')
    if re.match(pattern, link) is None:
        raise ValueError('Некорректная ссылка!')


def authorize(username: str = None, password: str = None, next_url: str = '') -> requests.Session | None:
    session = requests.Session()
    response = session.get(LOGIN_URL)
    response.raise_for_status()
    csrf_token = session.cookies.get('csrftoken')
    if username is None:
        username = input('Введите ваш E-Mail:\n')
    if password is None:
        password = getpass('Введите ваш пароль:\n')
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'username': username,
        'password': password,
        'next': next_url
    }
    print(username, password)
    login_response = session.post(LOGIN_URL, data=dict(**LOGIN_FORM, **login_data), headers=LOGIN_HEADERS)
    login_response.raise_for_status()
    if login_response.ok:
        print("Вход выполнен успешно!")
        return session
    else:
        print("Ошибка входа.")


if __name__ == '__main__':
    authorize(USERNAME, PASSWORD)
    # check_live_link(input('Ссылка:\n'))
