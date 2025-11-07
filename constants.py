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

MAIN_URL = 'https://meloman.ru'
LOGIN_URL = MAIN_URL + "/account/login"


LOGIN_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'philang=ru; _fbp=fb.1.1732116869854.431436538344447381; carrotquest_session=au4wzivxohnkjvggdf8kfxszqr3y6w7c; carrotquest_session_started=1; carrotquest_device_guid=fef2fb34-f7ee-4052-ba79-baf17e865662; carrotquest_uid=1845568186758467466; carrotquest_auth_token=user.1845568186758467466.57994-3e6de2c0a0f614bd3cd5f22f98.f9b1fea46f01d774796f9e4998a76cc463d65f67db9277af; csrftoken=iyIvTrB2fc7zDPFdmjg4o3D464LtztGCsZA9RZ6qOgso4VCXAwljuRtPPMoKIMsi; carrotquest_jwt_access=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE3MzIxMjA0NzIsImlhdCI6MTczMjExNjg3MiwianRpIjoiYmY2ZjYwZjA4MzZlNDc5MmFjNzZmZmM0MGEwMTU3NzgiLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTczMjExNjg3Miwicm9sZXMiOlsidXNlci4kYXBwX2lkOjU3OTk0LiR1c2VyX2lkOjE4NDU1NjgxODY3NTg0Njc0NjYiXSwiYXBwX2lkIjo1Nzk5NCwidXNlcl9pZCI6MTg0NTU2ODE4Njc1ODQ2NzQ2Nn0.iN8bmVNAUQUQfT4OPd6NKunVSkwuzcNfVlKgIZPZCOE; carrotquest_realtime_services_transport=wss',
    'Origin': MAIN_URL,
    'Referer': LOGIN_URL,
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "YaBrowser";v="24.10", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

LOGIN_FORM = {
    'this_is_the_login_form': '1',
    'submit-button': ''
}

USERNAME = os.getenv('MELOMAN_USERNAME')
PASSWORD = os.getenv('MELOMAN_PASSWORD')

DOWNLOADS_PATH = 'downloads'
BLOCK_SIZE = 2048
