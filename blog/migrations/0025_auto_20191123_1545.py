# Generated by Django 2.2.6 on 2019-11-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0024_auto_20191103_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmember',
            name='team',
            field=models.CharField(choices=[('None', 'None'), ('Software', 'Software'),
                                            ('CAD/Manufacturing', 'CAD/Manufacturing'), ('Outreach', 'Outreach'),
                                            ('Strategy', 'Strategy'), ('Safety', 'Safety'),
                                            ('Helping Hands', 'Helping Hand')], default='None', max_length=255,
                                   verbose_name='team name'),
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.CharField(choices=[('None', 'None'), ('Software', 'Software'),
                                            ('CAD/Manufacturing', 'CAD/Manufacturing'), ('Outreach', 'Outreach'),
                                            ('Strategy', 'Strategy'), ('Safety', 'Safety'),
                                            ('Helping Hands', 'Helping Hand')], default='None', max_length=255,
                                   verbose_name='team name'),
        ),
        migrations.AlterField(
            model_name='historicalmeeting',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='meeting end time'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='meeting end time'),
        ),
    ]
