from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Tag
from .forms import NoteForm, TagForm, YourTagForm


def main(request):
    notes = Note.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'noteapp/index.html', {"notes": notes})


@login_required
def tag(request):
    form = YourTagForm(request.POST or None)  
    tag_name = None
    notes = None

    if request.method == 'POST' and form.is_valid():
        tag_name = form.cleaned_data['name']
        tag, created = Tag.objects.get_or_create(name=tag_name, user=request.user)

        if created:
            print(f"Nowy tag dodany: {tag_name}")

        notes = Note.objects.filter(tags=tag, user=request.user)

    return render(request, 'noteapp/tag.html', {'form': form, 'tag_name': tag_name, 'notes': notes})


@login_required
def note(request):
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {"tags": tags, 'form': form})

    return render(request, 'noteapp/note.html', {"tags": tags, 'form': NoteForm()})


def notes_by_tag(request, tag_name):
    if tag_name:
        tag = Tag.objects.filter(name=tag_name, user=request.user).first()

        if tag:
            notes = Note.objects.filter(tags=tag, user=request.user)
            form = YourTagForm(initial={'name': tag_name})  # Initialize the form with the tag_name
            return render(request, 'noteapp/notes_by_tag.html', {'tag_name': tag_name, 'notes': notes, 'form': form})

    return redirect('noteapp:tag')


def notes_by_tag_page(request, tag_name):
    tag = Tag.objects.filter(name=tag_name, user=request.user).first()

    if tag:
        notes = Note.objects.filter(tags=tag, user=request.user)
        return render(request, 'noteapp/notes_by_tag.html', {'tag_name': tag_name, 'notes': notes})
    else:
        return redirect('noteapp:tag')


@login_required
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    return render(request, 'noteapp/detail.html', {"note": note})


@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=True)
    return redirect(to='noteapp:main')


@login_required
def delete_note(request, note_id):
    Note.objects.get(pk=note_id, user=request.user).delete()
    return redirect(to='noteapp:main')

