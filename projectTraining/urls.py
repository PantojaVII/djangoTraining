from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_View(request):
    return HttpResponse('HOME')


def about(request):
    return HttpResponse('about')


def contact(request):
    return HttpResponse('contact')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_View),
    path('sobre/', about),
    path('contato/', contact),
]
""" Teste """
