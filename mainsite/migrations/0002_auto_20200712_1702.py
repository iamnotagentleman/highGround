# Generated by Django 3.0.8 on 2020-07-12 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainsite.app_models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaluser',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical User'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='gender',
            field=models.CharField(blank=True, choices=[('E', 'Male'), ('K', 'Female')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('E', 'Male'), ('K', 'Female')], max_length=1, verbose_name='Gender'),
        ),
        migrations.CreateModel(
            name='HistoricalCourse',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Course Name')),
                ('description', models.CharField(max_length=5000, null=True, verbose_name='Description of Course')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mainsite.Site', verbose_name='Course Site')),
            ],
            options={
                'verbose_name': 'historical course',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Course Name')),
                ('description', models.CharField(max_length=5000, null=True, verbose_name='Description of Course')),
                ('assistant', models.ManyToManyField(limit_choices_to={'is_staff': True}, related_name='assistant', to=settings.AUTH_USER_MODEL, verbose_name='Assistant of Lecturer')),
                ('lecturer', models.ManyToManyField(limit_choices_to={'is_staff': True}, related_name='lecturer', to=settings.AUTH_USER_MODEL, verbose_name='Lecturers of Course')),
                ('participant', models.ManyToManyField(limit_choices_to={'is_staff': False}, related_name='participant', to=settings.AUTH_USER_MODEL, verbose_name='Participants Of Course')),
                ('site', models.ForeignKey(on_delete=models.SET(mainsite.app_models.courses.get_sentinel_site), to='mainsite.Site', verbose_name='Course Site')),
            ],
            options={
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]