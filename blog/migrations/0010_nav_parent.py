# Generated by Django 2.1.7 on 2019-02-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0009_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='blog.Nav'),
        ),
    ]