from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # Import the LoginRequiredMixin
from .models import Cat, Breed

class CatList(LoginRequiredMixin, ListView):  # Apply LoginRequiredMixin to restrict access
    model = Cat
    template_name = 'cats/cat_list.html'

class CatCreate(LoginRequiredMixin, CreateView):  # Apply LoginRequiredMixin to restrict access
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):  # Apply LoginRequiredMixin to restrict access
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):  # Apply LoginRequiredMixin to restrict access
    model = Cat
    success_url = reverse_lazy('cats:all')

class BreedList(LoginRequiredMixin, ListView):  # Apply LoginRequiredMixin to restrict access
    model = Breed
    template_name = 'cats/breed_list.html'

class BreedCreate(LoginRequiredMixin, CreateView):  # Apply LoginRequiredMixin to restrict access
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):  # Apply LoginRequiredMixin to restrict access
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):  # Apply LoginRequiredMixin to restrict access
    model = Breed
    success_url = reverse_lazy('cats:all')
