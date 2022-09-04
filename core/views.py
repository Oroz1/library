from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Book, Genre
from core.servieces import IncreaseViewsBookMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from core.forms import LoginForm, BookForm


def main(request):
    books = Book.objects.all()[:4]
    return render(request, 'index.html', {'books': books})


class ListBooks(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books' 
    paginate_by = 12
       
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre"] = Genre.objects.all()
        return context
    
    
class DetailBook(IncreaseViewsBookMixin, DetailView):    
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'book'  
    pk_url_kwarg = 'id'

    
def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')    
    
    
def login_profile(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
                messages.error(request, f'Не существует пользователя или неверный паороль')
            return render(request, 'auth/login.html', {'form': form})
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})
    return redirect('/')    


@login_required(login_url='/login')
def user_area(request):
    return render(request, 'user_area/index.html', {
        'books': Book.objects.filter(owner=request.user),
        'genre': Genre.objects.all(),
    })


@login_required(login_url='/login')
def create_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Книга "{book.title}" успешно дабвлено')
            return redirect('/user_area/')
        return render(request, 'user_area/create_books.html', {'form': form})
    form = BookForm()
    return render(request, 'user_area/create_books.html', {'form': form})


class CreateBook(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    
    model = Book
    context_object_name = 'book'
    template_name = 'user_area/create_books.html'
    login_url = '/login'
    #fields = ['title', 'type']
    form_class = BookForm
    success_message = 'Книга успешно дабвлено'
    success_url = '/user_area/'
    
    def form_valid(self, form, **kwargs):
        title = self.request.POST.get('title')
        self.success_message = f'Книга "{title}" успешно дабвлено'
        return super(CreateBook, self).form_valid(form)
    
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
    #     form.fields['type'].widget = forms.Select(attrs={'class': 'form-control'})
    #     form.fields['type'].queryset = Types.objects.all()
    #     return form
    

class UpdateBook(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    context_object_name = 'book'
    template_name = 'user_area/update_books.html'
    login_url = '/login'
    #fields = ['title', 'type']
    form_class = BookForm
    success_message = ''
    success_url = '/user_area/'
    pk_url_kwarg = 'id'
    
    def form_valid(self, form, **kwargs):
        title = self.request.POST.get('title')
        self.success_message = f'Книга "{title}" успешно отредатирована!'
        return super(CreateBook, self).form_valid(form)
    
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
    #     form.fields['type'].widget = forms.Select(attrs={'class': 'form-control'})
    #     form.fields['type'].queryset = Types.objects.all()
    #     return form

# Create your views here.
