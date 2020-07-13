# Generated by Django 3.0.8 on 2020-07-12 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20200712_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_staff': True}, null=True, related_name='assistant', to=settings.AUTH_USER_MODEL, verbose_name='Assistant of Lecturer'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lecturer',
            field=models.ManyToManyField(limit_choices_to={'is_staff': True}, null=True, related_name='lecturer', to=settings.AUTH_USER_MODEL, verbose_name='Lecturers of Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='participant',
            field=models.ManyToManyField(limit_choices_to={'is_staff': False}, null=True, related_name='participant', to=settings.AUTH_USER_MODEL, verbose_name='Participants Of Course'),
        ),
        migrations.AlterField(
            model_name='site',
            name='logo',
            field=models.ImageField(upload_to='images/site/', verbose_name='Logo'),
        ),
    ]