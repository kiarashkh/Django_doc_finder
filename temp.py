from django.contrib import admin
from .models import Document, Tag, Question

class AuthorMixin:
    """Mixin to auto-assign the current user as author when saving."""
    def save_model(self, request, obj, form, change):
        if not obj.author:  # only set if not already assigned
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Document)
class DocumentAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ("title", "date", "author")
    search_fields = ("title", "text")
    list_filter = ("date", "tags", "author")
    filter_horizontal = ("tags",)


@admin.register(Question)
class QuestionAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ("question_text", "document", "created_at", "author", "answer_text")
    search_fields = ("question_text",)
    list_filter = ("created_at", "document", "author")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
