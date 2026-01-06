from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Document
from .utils.bm25_cache import build_index

@receiver([post_save, post_delete], sender=Document)
def refresh_index_on_change(*args, **kwargs):
    build_index()

@receiver(m2m_changed, sender=Document.tags.through)
def refresh_index_on_tag_change(*args, **kwargs):
    build_index()
