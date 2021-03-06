# Generated by Django 2.2.6 on 2019-10-20 01:51

import blog.models.signin
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0019_auto_20191010_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='end_time',
            field=models.DateTimeField(null=True, validators=[blog.models.signin.Signin.endValidator],
                                       verbose_name='sign-out time'),
        ),
        migrations.AlterField(
            model_name='signin',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, validators=[blog.models.signin.Signin.startValidator],
                                       verbose_name='sign-in time'),
        ),
        migrations.AddConstraint(
            model_name='signin',
            constraint=models.UniqueConstraint(condition=models.Q(end_time__isnull=True), fields=('user', 'meeting'),
                                               name='user_meeting_chk'),
        ),
    ]
