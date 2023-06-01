# Generated by Django 3.2.18 on 2023-06-01 02:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('language', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('py', 'Python'), ('java', 'Java'), ('js', 'JavaScript'), ('c', 'C'), ('c++', 'C++'), ('c#', 'C#'), ('ruby', 'Ruby'), ('dart', 'Dart'), ('scala', 'Scala'), ('go', 'Golang'), ('swift', 'Swift'), ('kotlin', 'Kotlin'), ('node_js', 'Node.js')], max_length=59)),
                ('capacity', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(2)])),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('days', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('월', '월요일'), ('화', '화요일'), ('수', '수요일'), ('목', '목요일'), ('금', '금요일'), ('토', '토요일'), ('일', '일요일')], max_length=13)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('join_condition', models.PositiveSmallIntegerField(choices=[(1, '승인 필요'), (2, '바로 가입')], default=1)),
                ('category', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('join_request', models.ManyToManyField(blank=True, related_name='study_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Studying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.PositiveSmallIntegerField(default=1)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.study')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='study',
            name='studying_users',
            field=models.ManyToManyField(blank=True, related_name='user_studies', through='studies.Studying', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='study',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_studies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.study')),
            ],
        ),
    ]
