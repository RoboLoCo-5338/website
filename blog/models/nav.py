from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from blog.models.users import Details


class Nav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, unique=True)
    link = models.SlugField(max_length=10, unique=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE,
                               limit_choices_to={'parent': None})

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {name}'.format(title=self.title,
                                            name=Details.name(self.user))

    def has_children(self):
        """ Do we have child navs """
        return Nav.objects.filter(parent=self).count() > 0

    def kids(self):
        return self.children.order_by('title').all()
