from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView



urlpatterns = [
    path('create/blog', BlogCreateView.as_view(), name='create'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('blog//delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
