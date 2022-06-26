from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request, "index.html")


def premium(request: HttpRequest) -> HttpResponse:
    return render(request, "blog.html")


def support(request: HttpRequest) -> HttpResponse:
    return render(request, "podcast.html")


def download(request: HttpRequest) -> HttpResponse:
    return render(request, "events.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")
