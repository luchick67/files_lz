import pandas as pd  # Импорт библиотеки для работы с таблицами данных
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков

df = pd.read_parquet('titanic.parquet')  # Читаем исходный файл в формате parquet
df.to_csv('titanic.csv', index=False)  # Конвертируем в csv и сохраняем в текущую папку без индексов

df = pd.read_csv('titanic.csv')  # Читаем созданный csv-файл по условию задания

survive = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)  # Группируем по классу и статусу (1 - выжил, 0 - погиб), заполняя пустоты нулями
survive_percentage = survive.div(survive.sum(axis=1), axis=0) * 100  # Вычисляем долю выживших и погибших в процентах для каждого класса

survive_percentage.plot(kind='bar', stacked=True, figsize=(10, 6))  # Строим столбчатую диаграмму с накоплением (данные в одном столбце) и задаем размер

plt.title('Выживаемость пассажиров Титаника')  # Задаем заголовок графика
plt.xlabel('Класс билета')  # Подписываем горизонтальную ось X
plt.xticks(rotation=0)  # Выравниваем подписи классов на оси X горизонтально
plt.legend(['Не выжили', 'Выжили'])  # Добавляем легенду для обозначения цветов

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))  # Форматируем значения на оси Y со знаком процента
plt.ylim(0, 100)  # Устанавливаем границы оси Y от 0 до 100%
plt.grid(axis='y')  # Добавляем горизонтальные линии сетки для наглядности

plt.tight_layout()  # Автоматически выравниваем элементы графика, чтобы подписи не обрезались
plt.show()  # Выводим готовый график на экран