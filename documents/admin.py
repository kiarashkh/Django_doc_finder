from django.contrib import admin
from .models import Document, Tag, Question
# from .utils.bm25_cache import build_index
from .utils.bm25_search import find_relevant_documents_bm25

import logging


@admin.action(description="Run BM25 search for selected questions")
def run_bm25(modeladmin, request, queryset):
    logger = logging.getLogger(__name__) 
    logger.debug("went into action function") 
    logger.info("so far good")
    for question in queryset:
        results = find_relevant_documents_bm25(question)
    
    modeladmin.message_user(request, f"Question '{question}' → {len(results)} relevant docs found")


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
    list_display = ("question_text", "created_at", "author", "answer_text")
    search_fields = ("question_text",)
    list_filter = ("created_at", "documents", "author")
    filter_horizontal = ("documents",)
    actions = [run_bm25]

