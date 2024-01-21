import sqlite3
import json 
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')
django.setup()


from quotes.models import Quote, Author


def load_quotes_from_database():
    quotes_data = Quote.objects.values('text', 'author')
    return list(quotes_data)


if __name__ == "__main__":
    quotes_data = load_quotes_from_database()
    
    
    with open('quotes.json', 'w', encoding='utf-8') as json_file:
        json.dump(quotes_data, json_file, ensure_ascii=False, indent=2)
