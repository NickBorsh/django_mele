from django.contrib import admin
from .models import Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # отображаемые поля в списке статей
    list_filter = ('status', 'created', 'publish', 'author')  # добавляет блок фильтрации списка
    search_fields = ('title', 'body')  # добавляется строка поиска, для моделей в которых определен этот параметр
    prepopulated_fields = {'slug': ('title',)}  # ссылка генерируется автоматически из заголовка
    raw_id_fields = ('author',)  # добавляет поле поиска в поле автор
    date_hierarchy = 'publish'  # добавляет ссылки для навигации по датам, под поиском
    ordering = ('status', 'publish')  # по этим полям отсортированы статьи

