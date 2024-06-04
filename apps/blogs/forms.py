from django import forms
from apps.blogs.models import Blog

class BlogBaseForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'image_for_blogs',
            'creation_date'
        )

class BlogCreateForm(BlogBaseForm):
    pass

class BlogDetailForm(BlogBaseForm):
    pass

class BlogUpdateForm(BlogBaseForm):
    pass

class BlogDeleteForm(BlogBaseForm):  
    pass
