from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse


def index(request):
    return HttpResponse("Great, you are in the poll content!")


