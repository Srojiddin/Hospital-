from rest_framework import serializers

from apps.blogs.models import Blog



class BlogSerializer(serializers.ModelSerializer):
   class Meta:
       model = Blog
       fields = '__all__'





class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'