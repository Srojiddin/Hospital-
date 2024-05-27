from django.urls import path

from apps.comments.views import CommentCreateView, CommentDeleteView, CommentListView,  CommentUpdateView, CommentDetailView


urlpatterns = [
    path('comment/list/', CommentListView.as_view(), name="comment_list"),
    path('comment/create/', CommentCreateView.as_view(), name="comment_create"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment_delete"),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name="comment_detail"),

]