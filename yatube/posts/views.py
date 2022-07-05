from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница проекта Yatube',
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, any_slug):
    return HttpResponse(f'Cтраница групп супер проекта {any_slug}')
