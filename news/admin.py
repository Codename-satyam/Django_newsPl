from django.contrib import admin
from .models import Article, Feedback

class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    inlines = [FeedbackInline]

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created_at')
    readonly_fields = ('created_at',)
