from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from celery import shared_task
from django.core import management

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    if request.user.is_authenticated:
        t = Template('<h1> Hi {{ username }}! You are now logged in! </h1>')
        c = Context({'username': request.user.username})
        return HttpResponse(t.render(c))
    else:
        t = Template('<p>You are not logged in</p> \
                    <a href="{{ login }}">Log in<br></a> \
                    <a href="{{ signup }}">New user? Signup here.</a>'
        )
        c = Context({
            'login': "{% url 'login' %}",
            'signup': "{% url 'signup' %}"
        })
        return HttpResponse(t.render(c))
    