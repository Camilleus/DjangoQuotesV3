import requests
from bs4 import BeautifulSoup
import json

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

if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    quotes_data = scrape_quotes(url)

    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes_data, json_file, ensure_ascii=False, indent=2)
