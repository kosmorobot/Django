from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



def index(request):
    tasks = Task.objects.order_by('-id') #[:5] выбрано кол-во записей
    return render(request,'main/index.html', {'title': 'Главная старница сайта', 'tasks': tasks})


def about(request):
    return render(request,'main/about.html')


def ksushon(request):
    return render(request,'main/ksushon.html')


def lexa(request):
    return render(request,'main/lexa.html')


def jun(request):
    return render(request,'main/jun.html')


def mashka(request):
    return render(request,'main/mashka.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'main/create.html', context)



