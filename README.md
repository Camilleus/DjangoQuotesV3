# DjangoQuotesV3

tutaj chyba działa, jeszcze nad tym pracuję

DjangoQuotesV3
├─ .gitattributes
├─ notes
│ ├─ manage.py
│ ├─ media
│ │ ├─ default_avatar.png
│ │ └─ profile_images
│ │ └─ download.png
│ ├─ noteapp
│ │ ├─ admin.py
│ │ ├─ apps.py
│ │ ├─ forms.py
│ │ ├─ migrations
│ │ │ ├─ 0001_initial.py
│ │ │ ├─ 0002_remove_quote_author_remove_quote_user_note_user_and_more.py
│ │ │ └─ **init**.py
│ │ ├─ models.py
│ │ ├─ static
│ │ │ └─ noteapp
│ │ │ └─ styles.css
│ │ ├─ templates
│ │ │ └─ noteapp
│ │ │ ├─ base.html
│ │ │ ├─ detail.html
│ │ │ ├─ index.html
│ │ │ ├─ note.html
│ │ │ └─ tag.html
│ │ ├─ templatetags
│ │ │ └─ extract_tags.py
│ │ ├─ tests.py
│ │ ├─ urls.py
│ │ ├─ views.py
│ │ └─ **init**.py
│ ├─ notes
│ │ ├─ asgi.py
│ │ ├─ settings.py
│ │ ├─ urls.py
│ │ ├─ wsgi.py
│ │ └─ **init**.py
│ ├─ quotes
│ │ ├─ admin.py
│ │ ├─ apps.py
│ │ ├─ forms.py
│ │ ├─ migrations
│ │ │ ├─ 0001_initial.py
│ │ │ └─ **init**.py
│ │ ├─ models.py
│ │ ├─ templates
│ │ │ └─ quotes
│ │ │ ├─ add_author.html
│ │ │ ├─ add_quote.html
│ │ │ ├─ author.html
│ │ │ ├─ author_detail.html
│ │ │ ├─ author_list.html
│ │ │ ├─ index.html
│ │ │ ├─ quote.html
│ │ │ ├─ quote_detail.html
│ │ │ └─ quote_list.html
│ │ ├─ tests.py
│ │ ├─ urls.py
│ │ ├─ views.py
│ │ └─ **init**.py
│ └─ users
│ ├─ admin.py
│ ├─ apps.py
│ ├─ forms.py
│ ├─ migrations
│ │ ├─ 0001_initial.py
│ │ └─ **init**.py
│ ├─ models.py
│ ├─ signals.py
│ ├─ templates
│ │ └─ users
│ │ ├─ login.html
│ │ ├─ profile.html
│ │ └─ signup.html
│ ├─ tests.py
│ ├─ urls.py
│ ├─ views.py
│ └─ **init**.py
├─ poetry.lock
├─ pyproject.toml
└─ README.md
