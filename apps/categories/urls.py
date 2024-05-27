from django.urls import path
from apps.categories.views import CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView


urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update//<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
