from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # в БД тип записей будет VARCHAR
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # Слаг – короткое название, содержащее только
    # буквы, цифры и нижние подчеркивания или дефисы. Используется для построения семантических URL’ов (friendly URLs)
    # для статей
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # on_delete=models.CASCADE
    # при удалении пользователя будут удаляться связанные с ним статьи в БД
    body = models.TextField()  # тип TEXT в БД
    publish = models.DateTimeField(default=timezone.now)  # дата публикации статьи
    created = models.DateTimeField(auto_now_add=True)  # дата создания статьи, заполняется автоматически при создании
    updated = models.DateTimeField(auto_now=True)  # дата редактирования статьи, авто при сохранении
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    objects = models.Manager()  # менеджер по умолчанию
    published = PublishedManager()  # новый менеджер

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


