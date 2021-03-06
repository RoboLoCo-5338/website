from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import Http404
from blog.models.comment import Comment
from blog.models.post import Post
from django.contrib.auth.mixins import PermissionRequiredMixin


class CommentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    template_name = 'blog/create_comment.html'
    login_url = reverse_lazy('login')
    permission_required = "blog.comment_gui_can_comment"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', kwargs={'pk': self.kwargs['pk']})
