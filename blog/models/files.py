from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import mimetypes


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    fil = models.FileField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        # Handle no extension files
        ext = self.fil.name.split('.')[-1]
        return reverse('blog:download_file', kwargs={'pk': self.pk, 'ext': ext})

    def __str__(self):
        return '"{title}" by {name}'.format(title=self.title,
                                            name=self.user.details.display() or self.user.first_name)

    def get_s3_url(self):
        return self.fil.url

    def get_content_type(self):
        return mimetypes.guess_type(self.fil.name) or 'application/octet-stream'

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
