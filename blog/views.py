from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from .forms import UserRegisterForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def detail(request, pk):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            print('dasdas')
            das = form.save(commit=False)
            das.author = request.user
            das.post = Post.objects.get(id=pk)
            das.save()
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk)
    form = CommentCreateForm()

    return render(request, 'detail.html', {'post': post, 'comments': comments, 'form': form})


def register(request): # функция регистрации
    print('da')
    if request.method == 'POST': # Проверка запроса на пост
        form = UserCreationForm(request.POST) # присваиваем форму для данных
        print('POST')
        if form.is_valid(): #  Проверка на валидность
            form.save() # Сохранение в базу
            print('VAlid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) # авторизация юзера
            print('hz')
            login(request, user) # авторизация юзера
            return redirect('/') # переадресация на главную страничку
    else: # если это запрос не пост
        form = UserCreationForm() # Присваивание форму

    context = {'form': form} # контекст для передачи данных для шаблона
    return render(request, 'register.html', context)


def postcreate(request):
    if str(request.user) == 'AnonymousUser':  # проверка на не авторизованного юзера
        return redirect('/register')  # переадресация на форму регистрации
    form = PostCreateForm(request.POST)  # передача формы для данных
    if request.method == 'POST':  # проверка на запрос пост
        if form.is_valid():  # проверка на валидность
            print('das')
            das = form.save(commit=False)  # пресохранения в базу данных

            das.user = request.user  # передача в столбец автора авторизованного юзера
            das.save()  # сохранения в базу
            return redirect('/')  # переадресация на главную старничку
    context = {'form': form}  # контекст для передачи данных для шаблона
    return render(request, 'postcreate.html', context)


def delety(request, pk):
    post = Post.objects.get(id=pk)

    if post.user == request.user:
        post.delete()
        return redirect('/')
    else:
        return redirect('/')