from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html',
                  context={
                      'name': 'Pantoja'
                  })


def about(request):
    return render(request, 'recipes/pages/contact.html',
                  context={
                      'name': 'Contato'
                  })


def contact(request):
    return HttpResponse('contact')
