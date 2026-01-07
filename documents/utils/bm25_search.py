from documents.utils.bm25_cache import get_index, tokenize
from documents.models import Document

import logging
logger = logging.getLogger(__name__) 


def find_relevant_documents_bm25(question, top_k=3):
    logger.info("finding relevant docs")
    bm25, meta = get_index()

    query_tokens = tokenize(question.question_text)
    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = []

    for i in ranked_indices[:top_k]:
        score = scores[i]
        # logger.debug("went into search function") 
        # logger.info(score)
        # print(score)
        # if score <= 0:
        #     continue

        doc_id = meta[i]["id"]
        title = meta[i]["title"]

        if not question.documents.filter(id=doc_id).exists():
            question.documents.add(doc_id)

        results.append({
            "id": doc_id,
            "title": title,
            "score": float(score),
        })
    logger.info("relevant docs found")
    return results
