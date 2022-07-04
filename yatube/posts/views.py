from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group(request, any_slug):
    return HttpResponse(f'Cтраница групп супер проекта {any_slug}')
