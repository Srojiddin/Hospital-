from django.shortcuts import render

from django.views import generic


from apps.comments.forms import CommentForm
from apps.comments.models import Comment


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'commment_list.html'
    # context_object_name = "products"


class CommentCreateView(generic.CreateView):
    form_class = CommentForm
    model = Comment
    success_url = 'index'
    template_name = 'comment_create.html'


class CommentUpdateView(generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'
    success_url = 'index'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.save()
        return super().form_valid(form)


class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    pk_url_kwarg = 'pk'


class CommentDeleteView(generic.DeleteView):
    model = Comment
    pk_url_kwarg = 'pk'
    template_name = 'comment_delete.html'
    success_url = 'index'