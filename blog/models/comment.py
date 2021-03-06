from django.contrib.auth.models import User
from django.db import models
from blog.models.users import Details
from blog.models.post import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return '"{body}..." on {post_title} by {name}'.format(
            body=self.body[:20],
            post_title=self.post.title,
            name=Details.name(self.user),
        )

    class Meta:
        permissions = (
            ("comment_gui_can_comment", "Can create new comments via the GUI"),
        )
