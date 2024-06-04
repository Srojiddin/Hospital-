from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.blogs.api import views


router = DefaultRouter()
router.register('blog', views.BlogViewSet, basename="blog_api")

urlpatterns = [
    path('blog/<int:pk>/', views.BlogUpdateDeleteRetrieveAPIView.as_view(), name='blog'),
]
urlpatterns += router.urls