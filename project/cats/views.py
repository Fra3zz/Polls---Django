from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed

class CatList(ListView):
    model = Cat
    template_name = 'cats/cat_list.html'

class CatCreate(CreateView):
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatUpdate(UpdateView):
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatDelete(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')

class BreedList(ListView):
    model = Breed
    template_name = 'cats/breed_list.html'

class BreedCreate(CreateView):
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(UpdateView):
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedDelete(DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')
