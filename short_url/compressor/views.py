from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def default_view(request):
    return HttpResponse("Site working")