from django.contrib import admin
from .models import Document, Tag, Question



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    search_fields = ("title", "text")
    list_filter = ("date", "tags", "author")
    filter_horizontal = ("tags", )

@admin.register(Question)
class QestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "document", "created_at", "author", "answer_text")
    search_fields = ("question_text",)
    list_filter = ("created_at", "document", "author")

