# DocFinder: BM25 + LangChain + Q&A system

DocFinder is a modular Django-based system that alows you to post questions and retrieve answeres from it.
the program uses BM25 memory hash to speedup process. each of the commits represent a phase of project which highlights the modularity and extendabality of the project.
this project uses postgres database but it is up to the user that given the frequency of read and write to database change the database.

the system is intentionally minimal and made based on the idea of MVP and its up to others to use or extend it.

--- ## Project Structure 
``` 
documents/
├── admin.py # Admin actions for BM25 search + LLM answering
├── models.py # Document, Tag, Question models
└── utils/
    ├── bm25_cache.py # BM25 caching and making doc index logic
    ├── bm25_search.py # BM25 ranking logic
    └── llm_answer.py # LangChain-based answer generation
```
---
##  Running the System The entire project runs inside Docker. 
To start the application: 
```bash
docker compose up --build
```
application doesn't have a defualt admin but you can first connect to the web app using 
```bash
docker compose exec web bash
```
and then add admin using:
```bash
python manage.py createsuperuser
```

This launches: 
  - Django web server
  - PostgreSQL database

Once running, open the admin panel: 
``` 
http://localhost:8000/admin
```

Log in, and you can immediately: 
- Add documents
- Add questions
- Run BM25 search
- Generate answers via LLM
---

##  Sample Data 
The system supports adding sample data for demonstration:
- **3 example documents**
- **2 example questions**
- These can be created directly through the Django admin panel.
- They are used to demonstrate the BM25 ranking and LLM answer generation pipeline.
---

## How It Works 
### 1. **BM25 cache** Located in `utils/bm25_cache.py`, this module:
- Tokenizes each of the documents for bm25 to use
- saves them in cache
### 2. **BM25 Search** Located in `utils/bm25_search.py`, this module: 
- Extracts text from all documents linked to a question
- Computes BM25 scores - Returns the most relevant documents
### 3. **LLM Answer Generation** Located in `utils/llm_answer.py`, this module: 
- Builds a prompt using document context + question text
- Passes it through a LangChain chain
- Saves the generated answer back into the database
During development, a **Fake LLM** is used to avoid external API calls and ensure stable behavior.
---

##  Tests
tests can be added to validate: 
- BM25 ranking returns expected documents
- LLM pipeline runs end‑to‑end using a fake model
test structure:
```
documents/tests/test_bm25.py
documents/tests/test_llm.py
```
---

## Design Philosophy 
DocFinder is built with: 
- **Clarity over complexity**
- **Explicit utilities instead of hidden magic**
- **Modular functions** that can be tested independently
- **Admin‑driven workflows** to simplify demonstration
---
