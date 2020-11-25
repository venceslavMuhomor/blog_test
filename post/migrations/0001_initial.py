# Generated by Django 3.1.3 on 2020-11-25 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Под заголовок')),
                ('mini_text', models.TextField(verbose_name='краткий текст')),
                ('text', models.TextField(verbose_name='полный текст')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='Главная фотография')),
                ('template', models.CharField(default='blog/post_detail.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('viewed', models.PositiveIntegerField(default=0, verbose_name='Просмотрено')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='post.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='комментарий')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active_status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]