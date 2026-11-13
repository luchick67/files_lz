import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
import docx  # Импорт библиотеки для работы с документами Word
import re  # Импорт модуля для работы с регулярными выражениями
from collections import Counter  # Импорт счетчика для подсчета повторений элементов
import pandas as pd  # Импорт библиотеки для работы с таблицами данных

f = docx.Document(r"lion.docx")  # Открываем наш документ docx
text = []  # Создаем пустой список для хранения текста абзацев

for paragraph in f.paragraphs:  # Перебираем каждый абзац в документе
    text.append(paragraph.text)  # Добавляем текст абзаца в список

text = ' '.join(text)  # Объединяем все абзацы в одну строку через пробел

words = re.findall(r'\b\w+\b', text.lower())  # Извлекаем слова в нижнем регистре без знаков препинания

nwords = Counter(words)  # Считаем количество повторений каждого слова
vsego_words = sum(nwords.values())  # Вычисляем общее количество слов в тексте
df_words = pd.DataFrame(nwords.items(), columns=['Слово', 'Частота'])  # Создаем таблицу со словами и их частотой
df_words['Процент'] = (df_words['Частота'] / vsego_words) * 100  # Вычисляем процентную долю каждого слова

df_words.to_csv('sasa.csv', index=False, sep=';', encoding='utf-8-sig')  # Сохраняем таблицу в CSV в текущую папку

letters = re.findall(r'[а-яА-ЯёЁ]', text.lower())  # Извлекаем все русские буквы в нижнем регистре
nletters = Counter(letters)  # Считаем количество повторений каждой буквы
df_letters = pd.DataFrame(nletters.items(), columns=['Буква', 'Частота'])  # Создаем таблицу с буквами и их частотой

plt.figure(figsize=(10, 6))  # Задаем размер окна с графиком
plt.bar(df_letters['Буква'], df_letters['Частота'], color='green')  # Строим столбчатую диаграмму зеленого цвета
plt.title('Частота встречаемости букв')  # Задаем заголовок графика
plt.xlabel('Буквы')  # Подписываем горизонтальную ось X
plt.ylabel('Частота')  # Подписываем вертикальную ось Y
plt.grid(axis='y')  # Включаем горизонтальную сетку для удобства чтения значений

plt.tight_layout()  # Автоматически выравниваем элементы графика, чтобы подписи не обрезались
plt.show()  # Выводим готовый график на экран