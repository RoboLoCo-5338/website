from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from blog.models.users import Details
from blog.models.post import Post
from django.core.exceptions import ValidationError


def startValidator(meeting):
    return meeting.start_time < timezone.now()


def endValidator(meeting):
    return meeting.end_time > timezone.now()

class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('meeting start time', auto_now_add=True, editable=True)
    end_time = models.DateTimeField('meeting end time', default=timezone.now, null=True)

    def clean(self):
        if Meeting.objects.filter(start_time__lte=timezone.now()).filter(
                Q(end_time__isnull=True) | Q(end_time__gte=timezone.now())).count() > 0:
            raise ValidationError("cannot create multiple meetings")


    def __str__(self):
        return "meeting from {start_time} to {end_time}".format(start_time=self.start_time, end_time=self.end_time)

    class Meta:
        permissions = (
            ("meeting_gui_can_create", "Can create new meetings via the GUI"),
        )
