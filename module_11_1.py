import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# --------------------------- pandas -----------------------------
with open("data.csv", "a", encoding='utf-8') as file:   # Создаем файл csv
    for i in range(1, 10):                              # Цикл от одного до десяти
        file.write(f"{str(i*2)}, ")                     # Записываем в файл все i умложенное на два
df = pd.read_csv("data.csv")                            # Считываем двнные из файла
print(df.head())                                        # Выводим результаты в консоль. Просмотр первых строк
print(df.describe())                                    # Выводим результаты в консоль. Основные характеристики

# ------------------------- matplotlib ----------------------------
from random import randint                      # Импортируем из random для получения случайных чисел
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]             # Список от одного до десяти (для координата х)
y = []                                          # Создаем список, где будут находиться десять случайных чисел для оси у
for k in range(1, 11):
    y.append(randint(1, 10))              # Добавляем в список координаты у десять случайных чисел
plt.plot(x, y)                            # Отображаем график
plt.xlabel("X-axis")                            # Устанавливаем название горизонтальной оси х
plt.ylabel("Y-axis")                            # Устанавливаем название вертикальной оси у
plt.title("Line Plot")                          # Добавляем заголовок графику
plt.savefig("line_plot.png")                    # Сохраняем файл png
plt.show()                                      # Показываем график в отдельном окне

# --------------------------- pillow -----------------------------
import os                              # Импортируем из os для работы с файлами

def resize_image(image_path):          # Функция для изменения размера фотографии
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)

for i in range(1, 6):                     # Цикл для перебора фото и запуска функции resize_image
    image_path = f"./images/{i}.jpg"
    resize_image(image_path)

image_dir = "./images"                                   # Указываем путь к изображениям
images = []                                              # Создаем пустой список
for filename in os.listdir(image_dir):                   # Цикл перебора фото
    if filename.endswith(".jpg"):                        # Если файл имеет расширение jpg, то
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        images.append(image)                             # Записываем пути к фото в список

# Создание слайд-шоу
images[0].save("slideshow.gif", save_all=True, append_images=images[1:], loop=0, duration=2000)
# Созданный файл слайд-шоу можно запустить из проводника