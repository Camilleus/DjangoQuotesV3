from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('author_detail/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quote_detail/<int:quote_id>/', views.quote_detail, name='quote_detail'),
]