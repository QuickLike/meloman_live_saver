# [Meloman Live Saver](https://github.com/QuickLike/meloman_live_saver)

## Meloman Live Saver:
Сервис, который позволяет скачивать записи прямых трансляций с сайта [Московской Филармонии](https://meloman.ru/)

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/QuickLike/meloman_live_saver) и перейдите в него в командной строке:
```
git clone https://github.com/QuickLike/meloman_live_saver

cd meloman_live_saver
```
Создайте виртуальное окружение и активируйте его

Windows
```
python -m venv venv
venv/Scripts/activate
```

Linux/Ubuntu/MacOS
```
python3 -m venv venv
source venv/bin/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```

Запуск бота
```
python main.py
```

## Формат ссылки
Не подходящий формат (ссылка на страницу записи концерта):

https://meloman.ru/concert/.../

Подходящий (ссылка на видеозапись концерта):

https://records.meloman.facecast.net/files/.../0/KZCH/meloman/...KZCH.mp4
https://records.meloman.facecast.net/files/.../0/F2/meloman/...F2.mp4
https://records.meloman.facecast.net/files/.../0/KZF/meloman/...KZF.mp4
https://records.meloman.facecast.net/files/.../0/KZF/facecast/...KZF.mp4

## Получение ссылки
Для получения ссылки на запись вам нужно:
1. Открыть страницу с записью прямой трансляции (https://meloman.ru/concert/.../)
2. Нажать F12 для открытия панели разработчика
3. Перейти во вкладку Network/Сеть
4. Выбрать фильтр Media/Носитель
5. Кликнуть правой кнопкой по файлу видеозаписи (24-11-03-13-00-HD-KZCH.mp4) в списке (если не появляется, включите видеозапись) и скопируйте ссылку Copy -> Copy URL / Копировать -> Скопировать URL



## Автор

[Власов Эдуард](https://github.com/QuickLike)
