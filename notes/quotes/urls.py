from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('add_author/', views.add_author, name='add_author'),
    path('quote/', views.quote, name='quote'),
    path('add_quote/', views.add_quote, name='add_quote'),
]