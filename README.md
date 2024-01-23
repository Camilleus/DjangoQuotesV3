# DjangoQuotesV3

tutaj działa, jeszcze nad tym pracuję

## Instalacja

1. Sklonuj repozytorium: `git clone https://github.com/Camilleus/DjangoQuotesV3.git`
2. Przejdź do folderu projektu: `cd DjangoQuotesV3`
3. Zainstaluj zależności: `poetry install`
4. Uruchom serwer: `poetry run python manage.py runserver`

## Przyszłe Rozszerzenia

Top Ten Tags
Ulubione Cytaty

## Kontrybucje

Czekamy na Twoje pull requesty!```

Powyższy kod markdown wykorzystuje blok kodu do przedstawienia struktury projektu w formie drzewa. Dodatkowo, dodano sekcję "Instalacja" i "Kontrybucje" jako przykłady, które można dostosować do swoich potrzeb.

## Struktura Projektu

DjangoQuotesV3

- .gitattributes
- notes
  - manage.py
  - media
    - default_avatar.png
    - profile_images
      - download.png
  - noteapp
    - admin.py
    - apps.py
    - forms.py
    - migrations
      - 0001_initial.py
      - 0002_remove_quote_author_remove_quote_user_note_user_and_more.py
      - **init**.py
    - models.py
    - static
      - noteapp
        - styles.css
    - templates
      - noteapp
        - base.html
        - detail.html
        - index.html
        - note.html
        - tag.html
    - templatetags
      - extract_tags.py
    - tests.py
    - urls.py
    - views.py
    - **init**.py
  - notes
    - asgi.py
    - settings.py
    - urls.py
    - wsgi.py
    - **init**.py
  - quotes
    - admin.py
    - apps.py
    - forms.py
    - migrations
      - 0001_initial.py
      - **init**.py
    - models.py
    - templates
      - quotes
        - add_author.html
        - add_quote.html
        - author.html
        - author_detail.html
        - author_list.html
        - index.html
        - quote.html
        - quote_detail.html
        - quote_list.html
    - tests.py
    - urls.py
    - views.py
    - **init**.py
  - users
    - admin.py
    - apps.py
    - forms.py
    - migrations
      - 0001_initial.py
      - **init**.py
    - models.py
    - signals.py
    - templates
      - users
        - login.html
        - profile.html
        - signup.html
    - tests.py
    - urls.py
    - views.py
    - **init**.py
- poetry.lock
- pyproject.toml
- README.md
