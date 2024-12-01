from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

# Настройки Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Фоновый режим
driver = webdriver.Chrome(options=options)

# URL сайта
url = "http://books.toscrape.com/"
driver.get(url)

# Задержка для загрузки страницы
time.sleep(2)

# Получение HTML-кода страницы
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Список для хранения данных
books_data = []

# Парсинг данных
books = soup.select('.product_pod')
for book in books:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    rating = book.select_one('.star-rating')['class'][1]  # Берем второй класс для рейтинга
    books_data.append({
        "title": title,
        "price": price,
        "rating": rating
    })

# Закрытие браузера
driver.quit()

# Сохранение данных в CSV
csv_file = "books_data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(books_data)

print(f"Данные успешно сохранены в {csv_file}")
