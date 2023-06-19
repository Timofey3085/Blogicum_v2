from django.shortcuts import render
from django.http import HttpResponse


def about(request) -> HttpResponse:
    return render(request, 'pages/about.html')


def rules(request) -> HttpResponse:
    return render(request, 'pages/rules.html')
