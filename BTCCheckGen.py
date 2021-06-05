# Подключение библиотек
import random 
print (' ')
print('////////OxideDevX привевствует вас!')
print('......[ BTCCheckGen 1.0 ]......')
print('Генератор чеков для @BTC_CHANGE_BOT')
print('Разработчик: t.me/pwntt')
print(' ')
print('......[ BTCCheckGen 1.0 ]......')
print(' ')
# Задаем данные которые будут использоваться для генерации.
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('◾ Укажите желаемое количество ссылок для генерации:'+ "\n")
print(' ')
length = input('◾ Укажите длинну чека (рекомендовано 32):'+ "\n")
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
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)
print(' ')
print('➕ Удачного поиска! :) ')
print()
toexit = input("[BTCCheckGen]  Нажмите любую клавишу для завершения работы.")
