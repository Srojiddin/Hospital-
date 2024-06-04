from rest_framework import viewsets, generics

from apps.blogs.api.serializers import BlogSerializer, BlogCreateSerializer
from apps.blogs.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return BlogCreateSerializer
        return self.serializer_class



class BlogUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


