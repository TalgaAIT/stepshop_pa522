from django.shortcuts import render

def index(request):
    title = 'главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contact.html')
