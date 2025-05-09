# Generated by Django 4.2.15 on 2025-04-03 04:47

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseshortname', models.CharField(default='True', max_length=250)),
                ('coursefullname', models.CharField(default='True', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(default='True', max_length=250)),
                ('subject2', models.CharField(default='True', max_length=250)),
                ('subject3', models.CharField(default='True', max_length=250)),
                ('subject4', models.CharField(default='True', max_length=250)),
                ('subject5', models.CharField(default='True', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(default=0)),
                ('session', models.CharField(default='True', max_length=250)),
                ('fname', models.CharField(default='True', max_length=250)),
                ('mname', models.CharField(default='True', max_length=250)),
                ('lname', models.CharField(default='True', max_length=250)),
                ('gender', models.CharField(default='True', max_length=250)),
                ('gname', models.CharField(default='True', max_length=250)),
                ('ocp', models.CharField(default='True', max_length=250)),
                ('income', models.CharField(default='True', max_length=250)),
                ('category', models.CharField(default='True', max_length=250)),
                ('ph', models.CharField(default='True', max_length=250)),
                ('nation', models.CharField(default='True', max_length=250)),
                ('mobno', models.CharField(default='True', max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(default='True', max_length=250)),
                ('state', models.CharField(default='True', max_length=250)),
                ('city', models.CharField(default='True', max_length=250)),
                ('padd', models.TextField(blank=True, default=0)),
                ('cadd', models.TextField(blank=True, default=0)),
                ('class1', models.CharField(default='True', max_length=250)),
                ('board1', models.CharField(default='True', max_length=250)),
                ('roll1', models.CharField(default='True', max_length=250)),
                ('pyear1', models.CharField(default='True', max_length=250)),
                ('class2', models.CharField(default='True', max_length=250)),
                ('board2', models.CharField(default='True', max_length=250)),
                ('roll2', models.CharField(default='True', max_length=250)),
                ('pyear2', models.CharField(default='True', max_length=250)),
                ('sub1', models.CharField(default='True', max_length=250)),
                ('marks1', models.IntegerField()),
                ('fmarks1', models.IntegerField()),
                ('sub2', models.CharField(default='True', max_length=250)),
                ('marks2', models.IntegerField()),
                ('fmarks2', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('subjects_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(upload_to='media/profile_pic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
