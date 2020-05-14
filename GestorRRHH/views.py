from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect


def inicio(request):
    if request.user.is_authenticated:
        return render(request,"inicio.html")
    else :
        return redirect('/login')

#{% load staticfiles %} esto despues del extends va
#style="background-image:url('{% static 'img/fondo.jpeg' %}');"


