from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'board/index.html')


def post_list(request):
    return render(request, 'board/post_list.html')
