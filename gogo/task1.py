# Напишите программу для безопасного сближения с Солнцем в зависимости от наличия мозга.
# Формат ввода:
# Вводится начальная дата - последнее сближение с Солнцем(не рассматривается как подходящая)
# Затем вводится 1 или 0 - есть мозг или нет.
# Затем период обращения вокруг Солнца.
# Количество требуемых дат
# Пример:
# Вводные данные:
# 25.03.2022
# 1
# 2
# 4
# Результат:
# 31 March 22
# 06 April 22
# 12 April 22
# 18 April 22

import datetime

input_date = input('Введите дату последнего сближения с Солнцемв формате(дд.мм.гггг):')
input_date = list(map(int,input_date.split('.')))
start_date = datetime.date(input_date[2], input_date[1], input_date[0])
brain_having = int(input('Если у вас есть мозг, введите единицу. Если нет - введице цифру ноль:'))
daylight_hours = int(input('Введите число, обозначающее сколько земных дней будет в одном световом дне: '))
number_of_dates = int(input('Введите число, обозначающее сколько вы хотите видеть ближайших дат безопасног осближения с Солнцем: '))
temp_day = input_date[0]
count = 0
if brain_having == 1:
    for i in range(number_of_dates):
        start_date += datetime.timedelta(days=3*daylight_hours)
        print(f'{str(start_date)[8:]} {start_date.strftime("%B")} {str(start_date)[2:4]}')
else: 
    for i in range(2022):
        start_date += datetime.timedelta(days=daylight_hours)
        if start_date.strftime("%A") == 'Thursday':
            print(f'{str(start_date)[8:]} {start_date.strftime("%B")} {str(start_date)[2:4]}')
            count += 1
            if count == number_of_dates:
                break



    


