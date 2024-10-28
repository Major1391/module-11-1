import нампай as np
import pandas as pd  # Для удобства назначаем имя короче


'''Pandas — программная библиотека  для обработки и анализа данных. 
Предоставляет специальные структуры данных и операции для манипулирования числовыми таблицами и временны́ми рядами.'''
df = pd.read_excel('погода.xlsx')  # открываем наш exel файл, добавляем print и видим частичное содержимое
print(df.head(10))  # метод покажет первые 10 строк
print(df.tail(5)) #Покажет последние 5 строк
df['Город'] = 'Великий Устюг'  # Создаём новый столбец
df = df.rename(columns={'Столбец1': 'Дата'})  # переименовываем столбцы
print(df)

import requests
from apikey import API_TOKEN
'''Requests — это библиотека для языка Python, которая упрощает работу с HTTP-запросами.
Она позволяет работать с запросами любого уровня сложности, используя простой синтаксис.'''
params = {'q': 'Вологда', 'appid': API_TOKEN, 'units': 'metric'}#создал переменную с параметрами для запроса
# на сайт погоды
headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru,en;q=0.9",
        "Host": "httpbin.org",
        "Priority": "u=1, i",
        "Referer": "https://httpbin.org/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"YaBrowser\";v=\"24.7\", \"Yowser\";v=\"2.5\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-671e41da-6a039d302bc9822d3136c5bf"
    }#на тренировочном сайте узнал свои данные и скопировал их сюда с целью обойти блокировку сайта погоды,
# т.к. запрос делаю через пайчарм
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, headers=headers)#создал
#переменную c гет запросом и нашими параметрами
print(response.status_code)#проверка статуса запроса response[200] окей)
print(response.text)#позволяет получить доступ к текстовой части ответа
'''По умолчанию requests автоматически пытается узнать текущую кодировку по заголовкам HTTP,
поэтому явное указание кодировки не требуется. В редких случаях может потребоваться изменение кодировки,
для этого нужно передать значение в response.encoding'''
print(response.json())#rэто метод для преобразования JSON-данных в словарь.Он используется для получения данных из API

import numpy as np
'''NumPy (Numerical Python) — это библиотека для Python,
которая позволяет работать с многомерными массивами и матрицами.
Она подходит для научных и математических расчётов,
поскольку отличается быстротой и эффективностью.'''
np_array = np.array([[1, 2, 3], #создаём массив
                     [2, 3, 4],
                     [3, 4, 5]])
np_array2 = np.array(3)
print(np_array.ndim)#узнаём количество осей в массиве
#Математические операции можно проводить только с согласованными массивами т.е. одинаковыми по размеру
#Но ест исключения
print(np_array + 5)
print(np_array+np_array2)