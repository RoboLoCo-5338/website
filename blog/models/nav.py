from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Nav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    link = models.SlugField(max_length=10)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title,
                                                username=self.user.username)