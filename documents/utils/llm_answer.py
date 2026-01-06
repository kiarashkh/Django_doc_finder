from langchain.llms import HuggingFaceHub

def answer_question_with_llm(question):
    docs_text = []
    for doc in question.documents.all():
        docs_text.append(f"{doc.title}\n{doc.text[:1000]}")

    context = "\n\n".join(docs_text)

    prompt = f"Question: {question.question_text}\n\n"
    prompt += f"Relevant documents:\n{context}\n\n"
    prompt += "Answer based only on these documents:"

    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",
        model_kwargs={"temperature": 0.0, "max_length": 256}
    )

    answer = llm(prompt)

    question.answer_text = answer
    question.save()

    return answer
