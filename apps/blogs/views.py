from django.urls import reverse_lazy
from django.views import generic
from apps.blogs.models import Blog,Departments,About,Gallery
from apps.blogs.forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm



class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blogs/blog_create.html'
    success_url = reverse_lazy('blogs:list')


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'detail'
    pk_url_kwarg = 'pk'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blogs/blog_update.html'
    success_url = reverse_lazy('blogs:list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    form_class = BlogDeleteForm
    template_name =  'blogs/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blogs:list')


class DepartmentsListView(generic.ListView):
    model = Departments
    template_name = 'departments.html'


class AboutUsView(generic.TemplateView):
    model = About
    template_name = 'about.html'


class GalleryListView(generic.ListView):
    model = Gallery
    template_name = 'galary.html'
    context_object_name = "galleries"
