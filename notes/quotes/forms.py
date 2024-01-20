from django import forms
from .models import Quote, Author

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'description', 'image']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError('This field is required.')
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError('This field is required.')
        return image
