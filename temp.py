from rank_bm25 import BM25Okapi
from documents.models import Document
import re
from typing import List, Tuple

_bm25: BM25Okapi | None = None
_documents: List[Document] | None = None


STOPWORDS = {"the", "is", "and", "of", "to", "a", "in"}

def tokenize(text: str):
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [t for t in tokens if t not in STOPWORDS]


def build_index() -> None:
    global _bm25, _documents

    documents = list(
        Document.objects.prefetch_related("tags").all()
    )

    corpus = []

    for doc in documents:
        combined_text = (
            f"{doc.title} "
            f"{doc.text[:3000]} "
            f"{' '.join(tag.name for tag in doc.tags.all())}"
        )
        corpus.append(tokenize(combined_text))

    _bm25 = BM25Okapi(corpus)
    _documents = documents


def get_index() -> Tuple[BM25Okapi, List[Document]]:
    if _bm25 is None or _documents is None:
        build_index()

    return _bm25, _documents
