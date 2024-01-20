from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import QuoteForm, AuthorForm


def main(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()
    return render(request, 'quotes/main.html', {'authors': authors, 'quotes': quotes})


def author(request):
    authors = Author.objects.all()
    return render(request, 'quotes/author.html', {'authors': authors})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes/author_detail.html', {'author_id': author_id})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            return redirect('quotes:author_detail', author_id=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


def quote(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote.html', {'quotes': quotes})


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote.html', {'quotes': quotes})


def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user_profile = request.user.profile
            quote.save()
            return redirect('quotes:quote_detail', quote_id=quote.pk)
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
