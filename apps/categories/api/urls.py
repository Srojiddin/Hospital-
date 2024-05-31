from django.urls import path
from apps.categories.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.CategoryCreateView, basename='category_api')

urlpatterns = [
    path('category/<int:pk>/', views.CategoryUpdateDeleteRetrieveAPIView.as_view(), name='category'),
]
urlpatterns += router.urls
