from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# @ensure_csrf_cookie
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")