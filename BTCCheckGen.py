# Код форкнут и немного исправлен кодером самоучкой OxideDevX
# Для начала импорптируем библиотеку для генерации(random)
import random  
# Теперь импортируем бибилиотеку времени(для создания задержки)
import time
print(' ')
print('OxideDevX он же Pentester привевствует вас!')
# Это задержка
time.sleep(0.9) #время в секундах!!! 
print('......[ BTCCheckGen v 3.0 ]......')
print('Генератор чеков для телеграм бота @BTC_CHANGE_BOT')
print(' ')
time.sleep(0.8) #время в секундах!!! 
print('......[ BTCCheckGen 4.0 ]......')
print(' ')
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890' 
number = input('◾ Укажите желаемое количество ссылок для генерации:'+"\n")
print(' ')
length = input('◾Укажите длинну чека (вводим 32):'+"\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('ВНИМАНИЕ! Работа скрипта успешно завершена: ', number, ' чеков сгенерировано.')
print('ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')
print('На данный момент ведуться работы по реализации автоматической валидации')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=c_',password)
print(' ')
print(' Удачного поиска! :) ')
print()
toexit = input("Нажмите любую клавишу для завершения работы.")
