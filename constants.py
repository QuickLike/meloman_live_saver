import os

from dotenv import load_dotenv

load_dotenv('.env')


HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ym_uid=1730726793718272111; _ym_d=1730726793; _ym_isad=2',
    'Host': 'records.meloman.facecast.net',
    # 'If-Range': "6725ef19-f555ccff",
    'Referer': 'https://player.meloman.facecast.net/',
    'Sec-Fetch-Dest': 'video',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 '
                  'YaBrowser/24.10.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
}

LOGIN_URL = "https://meloman.ru/account/login"

LOGIN_HEADERS = {
    'Referer': LOGIN_URL,
    'Content-Type': 'application/x-www-form-urlencoded'
}

LOGIN_FORM = {
    'this_is_the_login_form': '1',
    'submit-button': ''
}

USERNAME = os.getenv('MELOMAN_USERNAME')
PASSWORD = os.getenv('MELOMAN_PASSWORD')

DOWNLOADS_PATH = 'downloads'
BLOCK_SIZE = 2048
