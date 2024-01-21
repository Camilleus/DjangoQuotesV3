import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('.quote .text')
        authors = soup.select('.quote .author')

        for quote, author in zip(quotes, authors):
            print(f'Quote: {quote.text.strip()}')
            print(f'Author: {author.text.strip()}')
            print('---')

if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    scrape_quotes(url)
