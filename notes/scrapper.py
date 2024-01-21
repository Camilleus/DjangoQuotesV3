import requests
from bs4 import BeautifulSoup
import os
import django
import json


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')
django.setup()


from quotes.models import Quote, Author
from users.models import Profile

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


def save_quotes_to_database(quotes_data):
    user_profile, created = Profile.objects.get_or_create(user_id=1)

    for quote_info in quotes_data:
        quote_text = quote_info['quote']
        author_name = quote_info['author']

        author, created = Author.objects.get_or_create(name=author_name)

        Quote.objects.create(text=quote_text, author=author, user_profile=user_profile)



if __name__ == "__main__":
    url = "https://quotes.toscrape.com"
    quotes_data = scrape_quotes(url)
    save_quotes_to_database(quotes_data)
