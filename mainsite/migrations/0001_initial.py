# Generated by Django 3.0.8 on 2020-07-12 12:15

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import mainsite.app_models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=999, verbose_name='Home Address')),
                ('note', models.CharField(blank=True, max_length=2500, verbose_name='Note about User')),
                ('phone_number', models.CharField(blank=True, max_length=13, verbose_name='Mobil phone number')),
                ('birth_date', models.DateField(default=django.utils.datetime_safe.date(2000, 1, 1), verbose_name='Birth Date')),
                ('job', models.CharField(max_length=40, verbose_name='Job')),
                ('gender', models.CharField(choices=[('E', 'Male'), ('K', 'Female')], max_length=1, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='UK', max_length=2, verbose_name='Nationality')),
                ('current_education', models.CharField(choices=[('mid', 'Middle School'), ('high', 'High School'), ('univ', 'University'), ('mas', 'Master'), ('doc', 'Doctorate'), ('none', 'Not a Student')], max_length=4, verbose_name='Current Education')),
                ('organization', models.CharField(blank=True, max_length=200, null=True, verbose_name='Organization')),
                ('experience', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Work Experience')),
                ('emergency_contact_information', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Emergency Contact Information')),
                ('profile_photo', models.ImageField(help_text='Maximum 5 MB file is allowed.', upload_to=mainsite.app_models.users.user_directory_path, verbose_name='Profile Picture')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Site Name')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('logo', models.ImageField(upload_to='images/', verbose_name='Logo')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('home_url', models.CharField(max_length=128, null=True, verbose_name='Home Url')),
                ('domain', models.CharField(help_text='To parse incoming requests and show correct page', max_length=128, null=True, verbose_name='domain')),
                ('application_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Course Application Start Date')),
                ('application_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Course Application End Date')),
                ('event_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Event Start Date')),
                ('event_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Event End Date')),
                ('update_accommodation_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Accommodation Update End Date')),
                ('docs_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Docs End Date')),
                ('morning', models.FloatField(default=3.0, verbose_name='Total course hours at morning for one day')),
                ('afternoon', models.FloatField(default=3.5, verbose_name='Total course hours at afternoon for one day')),
                ('evening', models.FloatField(default=2.5, verbose_name='Total course hours at evening for one day')),
                ('needs_document', models.BooleanField(default=True, verbose_name='Site requires document')),
            ],
            options={
                'get_latest_by': 'year',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('address', models.CharField(blank=True, max_length=999, verbose_name='Home Address')),
                ('note', models.CharField(blank=True, max_length=2500, verbose_name='Note about User')),
                ('phone_number', models.CharField(blank=True, max_length=13, verbose_name='Mobil phone number')),
                ('birth_date', models.DateField(default=django.utils.datetime_safe.date(2000, 1, 1), verbose_name='Birth Date')),
                ('job', models.CharField(max_length=40, verbose_name='Job')),
                ('gender', models.CharField(choices=[('E', 'Male'), ('K', 'Female')], max_length=1, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(default='UK', max_length=2, verbose_name='Nationality')),
                ('current_education', models.CharField(choices=[('mid', 'Middle School'), ('high', 'High School'), ('univ', 'University'), ('mas', 'Master'), ('doc', 'Doctorate'), ('none', 'Not a Student')], max_length=4, verbose_name='Current Education')),
                ('organization', models.CharField(blank=True, max_length=200, null=True, verbose_name='Organization')),
                ('experience', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Work Experience')),
                ('emergency_contact_information', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Emergency Contact Information')),
                ('profile_photo', models.TextField(help_text='Maximum 5 MB file is allowed.', max_length=100, verbose_name='Profile Picture')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSite',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Site Name')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('logo', models.TextField(max_length=100, verbose_name='Logo')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('home_url', models.CharField(max_length=128, null=True, verbose_name='Home Url')),
                ('domain', models.CharField(help_text='To parse incoming requests and show correct page', max_length=128, null=True, verbose_name='domain')),
                ('application_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Course Application Start Date')),
                ('application_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Course Application End Date')),
                ('event_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Event Start Date')),
                ('event_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Event End Date')),
                ('update_accommodation_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Accommodation Update End Date')),
                ('docs_end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Docs End Date')),
                ('morning', models.FloatField(default=3.0, verbose_name='Total course hours at morning for one day')),
                ('afternoon', models.FloatField(default=3.5, verbose_name='Total course hours at afternoon for one day')),
                ('evening', models.FloatField(default=2.5, verbose_name='Total course hours at evening for one day')),
                ('needs_document', models.BooleanField(default=True, verbose_name='Site requires document')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical site',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]