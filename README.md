# BTC vaucher generator
***Привет. Данный проект создан кодером OxideDevX.***

КОД НАПИСАН В ИССЛЕДОВАТЕЛЬСКИХ ЦЕЛЯХ В РАМКАХ ПРОВЕРКИ БЕЗОПАСНОСТИ И ТЕОРИТИЧЕСКОЙ ВОЗМОЖНОСТИ ХАКИНГА ДАННОГО БОТА. 
ЗА ЛЮБЫЕ ПОБОЧНЫЕ ДЕЙСТВИЯ - ОТВЕСТВЕННОСТЬ НЕСЁТ КОНЕЧНЫЙ ПОТРЕБИТЕЛЬ. 


*Что это такое?*
Генератор BTC чеков. 
Скрипт генерирует ссылки для обнала BTC чеков в боте @btc_change_bot.
Генерируем ссылки и переходим по ним, если повезет обналичиваем чек.
Для работы нужен ПК либо сервер где есть Python(либо просто онлайн сервис по типу "programiz.com").

Как установить(для Linux и Termux): 

    apt update -y && apt upgrade -y

    apt install git python -y

    pip install requests

Скачиваем сам скрипт:

    git clone https://github.com/OxideDevX/btc-vaucher-bruter.git

    cd btc-vaucher-bruter

Запускаем скрипт командой:

    python3 BTCCheckGen.py

Далее запустится скрипт, и начнет генерировать ссылки.
Если все сделали правильно то скрипт сгенерирует вам ссылки такого типа:
    https://t.me/BTC_CHANGE_BOT?start=c_6aAjgfhfjhdg4754BLa6aZIFedRlvcET5Ea1N5
UPD!!! Можно запустить скрипт на любом онлайн сервисе, 
пример: https://www.programiz.com/python-programming/online-compiler/
Для этого нужно просто скопировать Python код в поле для ввода на вышеуказанном сайте и нажать кнопку "Run".
Удачи в поисках!
