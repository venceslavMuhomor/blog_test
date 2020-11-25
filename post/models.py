from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from pytils.translit import slugify


class Category(models.Model):
    """модель категорий"""
    name = models.CharField(verbose_name='имя', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """модель Постов"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='заголовок', max_length=200)
    slug = models.SlugField(verbose_name='url', unique=True)
    subtitle = models.CharField('Под заголовок', max_length=100, null=True, blank=True)
    mini_text = models.TextField(verbose_name='краткий текст')
    text = models.TextField(verbose_name='полный текст')
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    edit_date = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, verbose_name='Категория', blank=True)
    template = models.CharField('Шаблон', max_length=500, default='blog/post_detail.html')
    published = models.BooleanField('Опубликовать?', default=True)
    viewed = models.PositiveIntegerField('Просмотрено', default=0)
    rating = models.IntegerField('Рейтинг', default=0)

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = "{title} - {author}".format(title=self.title, author=str(self.author))
        self.slug = slugify(value)
        self.mini_text = self.text[:100]
        super(Post, self).save()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField('комментарий')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active_status = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return 'Комментарий от {} к посту {}'.format(self.author, self.post)

