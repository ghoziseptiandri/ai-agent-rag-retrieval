# AI Agent with Gemini + Python - #MakeItPublic Part 3

**Disclaimer: This project is a hands-on learning exercise. The code and structure have evolved through experimentation, debugging, and conversations with ChatGPT. It is a learning project, not a production-ready system.**

This repository is **Phase 3 (last part)** of my AI agent learning journey. 

It builds on the agent foundations from Part 1 and the tools, safety controls, and SQLite-backed memory from Part 2. This phase focuses on Retrieval-Augmented Generation (RAG).

**Learning journey:**

1. [Part 1 - Core Agent Foundations](https://github.com/ghoziseptiandri/ai-agent-template)
2. [Part 2 - Tools, Safety & Database Memory](https://github.com/ghoziseptiandri/ai-agent-api-database)
3. **Part 3 - RAG & Retrieval** (this repository)

> This is a learning project!

## Phase 3 - RAG & Retrieval

The goal of this phase is to let the agent answer questions using a local document collection, rather than relying only on the model's built-in knowledge.

### What this phase covers

- Document loading
- Text chunking
- Gemini embedding generation
- 3072-dimensional embeddings
- Cosine similarity
- Semantic retrieval
- Top-K retrieval
- Similarity thresholding
- A safe “not enough information” response
- Persistent local vector storage
- Document indexing
- RAG answer generation
- Automated vector-store and similarity tests

## What has been added in this project?

### 1. Document loading

Documents are loaded from the local `documents/` directory. For example:

```text
documents/company_policy.txt
```

The loaded text becomes the input to the chunking and indexing workflow.

### 2. Text chunking

Long documents are divided into smaller chunks so retrieval can select the most relevant passages instead of sending an entire document for every question.

For example, a refund policy can be split into chunks describing the policy, processing time, and refund conditions.

### 3. Embedding generation

The project uses Google's Gemini embedding model, `gemini-embedding-001`, to turn text into numerical vectors. The configured embedding output is **3072 dimensions**.

Example (shortened):

```text
[-0.018460063, 0.040452424, ...]
```

Embeddings represent text in a form that can be compared for semantic similarity.

### 4. Cosine similarity and semantic retrieval

The similarity utility compares a question embedding with document-chunk embeddings using cosine similarity. The retriever uses these scores to rank candidate chunks and return the most relevant results.

Example question:

```text
How long does a refund take?
```

A relevant result may contain:

```text
Refunds are normally processed within 5 business days...
```

The score helps rank the result; the similarity threshold can prevent low-relevance chunks from being used.

### 5. Persistent vector storage

The indexed chunks and their embeddings are saved to:

```text
data/vectors.json
```

This separates document indexing from question answering. Embeddings can be generated during indexing and reused for later queries instead of regenerating document embeddings every time.

### 6. RAG answer generation and fallback behavior

The intended RAG flow retrieves relevant passages and supplies them as context for Gemini to formulate an answer grounded in the documents.

For example:

**Question:** How long does a refund take?

**Answer:** Based on the provided context, refunds are normally processed within 5 business days after the request is approved.

If the documents do not contain enough relevant information, the agent should respond:

```text
I don't have enough information in the provided documents.
```

This fallback helps reduce unsupported answers. The answer should be based on retrieved document context, not invented details.

## Architecture

### Indexing flow

```text
Source document
      |
      v
Document loading
      |
      v
Text chunking
      |
      v
Embedding generation
      |
      v
data/vectors.json
```

### Query flow

```text
User question
      |
      v
Question embedding
      |
      v
Similarity search
      |
      v
Top-K relevant chunks
      |
      v
Similarity threshold check
      |
      v
Retrieved context
      |
      v
Gemini answer generation
      |
      v
Grounded answer or “not enough information”
```

## Project structure

The current repository is organized around the existing agent foundation plus the RAG-specific tools and scripts:

```text
ai-agent-rag-retrieval/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── database.py
├── logger.py
├── long_term_memory.py
├── main.py
├── manual_agent.py
├── memory.py
├── prompts.py
├── documents/
│   ├── black_glutinous_rice_porridge.txt
│   ├── company_policy.txt
│   └── eminem.txt
├── scripts/
│   ├── embed_document.py
│   ├── index_document.py
│   └── test_retrieval.py
├── tools/
│   ├── calculator.py
│   ├── chunker.py
│   ├── declarations.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── file_reader.py
│   ├── rag.py
│   ├── registry.py
│   ├── retriever.py
│   ├── similarity.py
│   ├── time_tool.py
│   ├── tool_permissions.py
│   ├── vector_store.py
│   └── weather.py
└── tests/
    ├── test_calculator.py
    ├── test_database.py
    ├── test_file_reader.py
    ├── test_memory.py
    ├── test_rag.py
    ├── test_registry.py
    ├── test_similarity.py
    ├── test_tool_permissions.py
    └── test_weather.py
```

Key RAG files:

- `tools/document_loader.py` — loads document text.
- `tools/chunker.py` — splits text into chunks.
- `tools/embeddings.py` — generates embeddings using Gemini.
- `tools/similarity.py` — calculates cosine similarity.
- `tools/retriever.py` — searches for relevant chunks.
- `tools/vector_store.py` — saves and loads the local vector store.
- `tools/rag.py` — connects retrieval with the answer workflow.
- `scripts/index_document.py` — indexes the company policy document.
- `scripts/test_retrieval.py` — runs a retrieval example.
- `tests/test_similarity.py` and `tests/test_rag.py` — test similarity and vector-store behavior.

## Why RAG matters

A normal language-model response is generated from the model's context and learned parameters. RAG adds a retrieval step, the application searches its own documents and provides relevant passages to the model at answer time.

This project demonstrates the main steps:

1. Prepare and chunk documents.
2. Embed the chunks.
3. Store embeddings for reuse.
4. Embed the user's question.
5. Retrieve and rank relevant chunks.
6. Filter weak matches with a similarity threshold.
7. Generate an answer from retrieved context.
8. Return a clear fallback when the available documents do not answer the question.

## Current scope and limitations

This  project focused on understanding RAG building blocks rather than hiding them behind a large framework. The current vector store is a local JSON file, which keeps the indexing and retrieval process visible and easy to inspect.

It is not presented as a production-ready retrieval service. Before using a system like this in production, additional work would be needed around document access controls, robust ingestion, observability, evaluation, vector-store scaling, and deployment.

## References

- [Part 1 - AI Agent Template](https://github.com/ghoziseptiandri/ai-agent-template)
- [Part 2 - AI Agent API & Database](https://github.com/ghoziseptiandri/ai-agent-api-database)
- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [Python documentation](https://docs.python.org/3/)
- [pytest documentation](https://docs.pytest.org/)

---

This last phase is moving from an agent that can call tools and store memory to an agent that can retrieve relevant information from documents and use it to produce grounded answers.
