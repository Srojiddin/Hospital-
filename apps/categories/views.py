
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.categories.models import Category



class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'categories/category_update_create.html'
    success_url = '/'
    context_object_name = "categories"


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'categories/category_update_create.html'
    success_url = '/'
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    context_object_name = 'category'
    success_url = '/'


