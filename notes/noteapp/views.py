from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Author, Quote, Note, Tag
from .forms import AuthorForm, QuoteForm


def main(request):
    return render(request, 'noteapp/index.html')
    
    
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})

    return render(request, 'noteapp/tag.html', {'form': TagForm()})


def note(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {"tags": tags, 'form': form})

    return render(request, 'noteapp/note.html', {"tags": tags, 'form': NoteForm()})


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'noteapp/detail.html', {"note": note})


def author(request):
    authors = Author.objects.order_by('last_name')

    
@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


def quote(request):
    queutes = Quote.objects.order_by(quote)

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('quotes_list')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})