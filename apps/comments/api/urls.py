from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.comments.api import views

router = DefaultRouter()
# router.register('', views.CommentViewSet, basename="comment_api")


urlpatterns = [
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='change'),
    path('comment_create/<int:pk>/', views.CommentListCreateView.as_view(), name='comment_create'),
]

urlpatterns += router.urls