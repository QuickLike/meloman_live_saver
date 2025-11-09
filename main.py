import os.path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from constants import HEADERS, DOWNLOADS_PATH, BLOCK_SIZE, USERNAME, PASSWORD
from utils import check_live_link, authorize


def download_live(url: str):
    try:
        response = requests.get(url=url, headers=HEADERS, stream=True)
    except Exception:
        raise RuntimeError("Ошибка при открытии страницы!")
    filename = url.split('/')[-1]
    total_size = int(response.headers.get("content-length", 0))
    filepath = DOWNLOADS_PATH + '/' + filename
    if not os.path.exists(DOWNLOADS_PATH):
        os.mkdir(DOWNLOADS_PATH)
    with tqdm(total=total_size, unit="B", unit_scale=True, desc=filename) as progress_bar:
        with open(filepath, "wb") as file:
            for data in response.iter_content(BLOCK_SIZE):
                progress_bar.update(len(data))
                file.write(data)
    if total_size != 0 and progress_bar.n != total_size:
        raise RuntimeError("Ошибка при загрузке файла!")
    return filepath


def main():
    live_link = input('Введите ссылку\n')
    filename = download_live(live_link)
    print(f'Загрузка завершена!  |  {filename}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Загрузка прервана.')
