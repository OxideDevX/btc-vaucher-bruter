# BTC vaucher generator
***Привет. Данный проект создан кодером OxideDevX(Pentester). Telegram: @pwntt .***

*Что это такое?*
Генератор BTC чеков. 
Скрипт генерирует ссылки для обнала BTC чеков в боте @btc_change_bot.
Генерируем ссылки и переходим по ним, если повезет обналичиваем чек.
Для работы нужен ПК либо сервер под управлением ОС Linux.
Как установить: 

    apt update -y && apt upgrade -y

    apt install git python -y

    pip install requests

Скачиваем сам скрипт:

    git clone https://github.com/OxideDevX/btc-vaucher-bruter.git

    cd BTCVoucherGen

Запускаем скрипт командой:

    python BTCCheckGen.py

Далее запустится скрипт, и начнет генерировать ссылки.
Если все сделали правильно то скрипт сгенерирует вам ссылки такого типа:
    https://t.me/BTC_CHANGE_BOT?start=b_6aAjgfhfjhdg4754BLa6aZIFedRlvcET5Ea1N5
Удачи в поисках!