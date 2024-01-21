import requests
from bs4 import BeautifulSoup
import json
import sqlite3

def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('.quote .text')
        authors = soup.select('.quote .author')

        data = []

        for quote, author in zip(quotes, authors):
            quote_text = quote.text.strip()
            author_name = author.text.strip()
            
            data.append({
                'quote': quote_text,
                'author': author_name
            })

        return data

def save_to_database(quotes_data, db_name='sqlite3.db'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS quotes (quote TEXT, author TEXT)')

    for quote_info in quotes_data:
        quote_text = quote_info['quote']
        author_name = quote_info['author']

        c.execute('INSERT INTO quotes (quote, author) VALUES (?, ?)', (quote_text, author_name))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    quotes_data = scrape_quotes(url)

    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes_data, json_file, ensure_ascii=False, indent=2)

    save_to_database(quotes_data, 'sqlite3.db')
