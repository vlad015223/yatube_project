from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница супер-проекта yatube')


def group(request, any_slug):
    return HttpResponse(f'Cтраница групп супер проекта {any_slug}')
