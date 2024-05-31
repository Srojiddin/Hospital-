from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.comments.api.serializers import CommentSerializer, CommentCreateSerializer

from apps.comments.models import Comment



class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return CommentCreateSerializer
    elif self.action == 'retrieve':
        return CommentSerializer
    return self.serializer_class


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


