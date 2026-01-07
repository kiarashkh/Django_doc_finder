from rank_bm25 import BM25Okapi
from documents.models import Document
import re
from typing import List, Tuple, Dict

import logging
logger = logging.getLogger(__name__)

_bm25 = None
_doc_meta = None 

STOPWORDS = {"the", "is", "and", "of", "to", "a", "in"}

def tokenize(text: str):
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [t for t in tokens if t not in STOPWORDS]

def build_index() -> None:
    logger.info("building bm_25 indexes")
    global _bm25, _doc_meta

    qs = Document.objects.prefetch_related("tags").all()

    corpus = []
    meta = []

    for doc in qs:
        combined = (
            f"{doc.title} "
            f"{doc.text[:6000]} "
            f"{' '.join(tag.name for tag in doc.tags.all())}"
        )

        corpus.append(tokenize(combined))
        meta.append({
            "id": doc.id,
            "title": doc.title,
        })

    _bm25 = BM25Okapi(corpus)
    _doc_meta = meta
    logger.info("building bm_25 indexes done")


def get_index() -> Tuple[BM25Okapi, List[Dict]]:
    if _bm25 is None or _doc_meta is None:
        build_index()

    return _bm25, _doc_meta
