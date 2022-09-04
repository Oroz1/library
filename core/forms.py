from dataclasses import fields
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from core.models import Book


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Имя пользователя', max_length=150, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'oroz...'})
    )
    
    password = forms.CharField(
        max_length=150, required=True, label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password' })
    )
    


class BookForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['genre'].empty_label = 'Выберите жанр'
        self.fields['author'].empty_label = 'Выберите автора'
        
    
    class Meta:
        model = Book
        #exclude = ('likes', 'views')
        fields = (
            'title',
            'file',
            'genre',
            'tags',
            'image',
            'description',
            'author',
            'owner',
        )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': CKEditorUploadingWidget(),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.HiddenInput()
        }