from langchain_core.language_models.fake import FakeListLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def answer_question_with_llm(question):
    docs_text = [f"{doc.title}\n{doc.text}" for doc in question.documents.all()]
    context = "\n\n".join(docs_text)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You must answer the question using ONLY the information below.

Documents:
{context}

Question:
{question}

Answer:"""
    )

    llm = FakeListLLM(
        responses=[
            "This is a fake answer for testing purposes.",
            "Another fake answer to simulate multiple calls.",
            "Yet another placeholder answer."
        ]
    )

    chain = prompt | llm | StrOutputParser()

    output = chain.invoke({
        "context": context,
        "question": question.question_text
    })

    question.answer_text = output
    question.save()
    return output
