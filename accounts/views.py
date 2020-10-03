from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:register_done')


class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'
