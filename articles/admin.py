from django.contrib import admin

from articles.models import Article
from articles.models import Comment

admin.site.register(Comment)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    inlines = [
        CommentInline,
    ]
