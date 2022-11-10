from django.urls import path, include
from .views import SignUpView
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]