from rest_framework import viewsets, generics
from apps.categories.api.serializers import CategorySerializer, CategoryCreateSerializer
from apps.categories.models import Category


class CategoryCreateView(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return CategoryCreateSerializer
        elif self.action == 'retrieve':
            return CategorySerializer
        return CategorySerializer


class CategoryUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

