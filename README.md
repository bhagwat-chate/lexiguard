# 🛡️ LexiGuard – Compliance-Aware GenAI Advisor for AI Policy Governance

> **FAANG-Grade Project by [Bhagwat Chate](https://www.linkedin.com/in/aimlbhagwatchate)**  
> Designed for C-suite utility, real-world auditability, and structured legal GenAI answers with zero hallucinations.

## Development in progress branch - release/1.0/dev/bhagwat

## 🧠 Overview

**LexiGuard** is a modular, production-ready GenAI system designed to analyze **AI policy and legal documents** (e.g., GDPR, HIPAA, EU AI Act, DPDP) and deliver:

- 📚 Contextual answers to compliance questions  
- 🔍 Faithfulness, citation, and hallucination checks  
- 🧾 Structured outputs conforming to legal formats  
- 📌 Actionable next steps with risk classification  

Built with **AutoGen**, **LangChain**, **RAGAS**, and **Guardrails.ai**, LexiGuard is engineered to meet enterprise-grade security, validation, and observability expectations.

## 🔍 Problem Statement

Modern enterprises struggle with:
- Ambiguous compliance with AI regulations  
- No structured answers from legal teams or LLMs  
- Risk of hallucinated clauses or unverified citations  
- Siloed policy documents across regions and teams  

**LexiGuard** solves this with:
- RAG + Guardrails + Multi-Agent orchestration  
- Verified citations and jurisdiction mapping  
- Structured legal insights with “not legal advice” disclaimer  
- Logs for every query with explainable eval metrics  

## 💡 Key Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🧠 **RAG with Legal Context**    | Semantic + metadata-based hybrid search on legal documents                 |
| ✅ **Evaluation Layer**          | Faithfulness (RAGAS), Toxicity (TruLens), Hallucination & Risk detection   |
| 🛡️ **Guardrails + Pydantic**     | Schema enforcement with enums, disclaimers, and JSON output guarantees     |
| 🔄 **Multi-Agent AutoGen Orchestration** | 13 modular agents with plug-and-play extensibility                |
| 🌍 **Jurisdiction Mapping**      | Compare laws like GDPR ↔ DPDP ↔ CCPA                                        |
| 🧾 **Version Comparison**        | Tracks policy updates and change logs                                       |
| 📊 **Logs + Scorecards**        | MongoDB/JSON logs with query trace, eval scores, risk tags                 |
| ☁️ **Cloud Native & Secure**    | Dockerized, deployable on AWS EC2, S3, and MongoDB Atlas                   |

## 🧩 Architecture

```
User → FastAPI → AutoGen Orchestrator
     → Retriever → RAG Context
     → AnswerGen → Eval Layer (RAGAS, TruLens, Citation)
     → Guardrails Layer (Schema, Enums, Disclaimers)
     → Actionability + Logging
     → Structured, Verified Response
```

➡️ See: `/docs/architecture.png` for detailed visual.

## 🗂️ Project Structure

See locked folder structure in `/docs/folder_structure.md`.

## ⚙️ Tech Stack

| Layer             | Stack Used                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Agent Runtime** | AutoGen `FunctionCallingAgent`, `GroupChat`, custom orchestrator            |
| **RAG**           | LangChain loaders, chunkers, OpenAI Ada-002 + Cohere Legal embeddings       |
| **Vector Store**  | Qdrant with metadata filtering (jurisdiction, clause type, severity)        |
| **LLMs**          | OpenAI GPT-4o + Cohere Command R+ (fallback)                                |
| **Evaluation**    | RAGAS, TruLens, OpenAI Moderation API                                       |
| **Validation**    | Pydantic + Guardrails.ai enforced schemas                                   |
| **API**           | FastAPI with modular routes                                                 |
| **Infra**         | Docker, Redis, MongoDB/JSON Logs, AWS EC2/S3                                |

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/bhagwat-chate/lexiguard.git && cd lexiguard

# 2. Setup virtualenv
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Load documents into vector store
python scripts/load_documents.py

# 5. Run the FastAPI server
uvicorn api.main:app --reload
```

Optional: `docker-compose up` for full stack (Redis + MongoDB + API)

## 🧪 Example Use Cases

| Prompt                                                                 | Output Description                                               |
|------------------------------------------------------------------------|------------------------------------------------------------------|
| “Is sharing personal data with 3rd parties allowed under DPDP?”       | Cited clause, risk tag = “Medium”, follow-up = “Need DPO review”|
| “How does GDPR differ from DPDP on consent?”                          | Cross-jurisdiction expander returns clause diff summary          |
| “What changed in our privacy policy since last version?”              | Version comparator highlights added/removed sections             |

## 📈 Success Metrics

- ✅ 100% JSON-structured outputs (schema-conforming)
- ✅ 90%+ RAGAS faithfulness score
- ✅ <1% hallucination and toxicity rate
- ✅ Deployment-ready API on AWS
- ✅ Works across GDPR, HIPAA, DPDP documents

## 📚 Documentation

- `HLD.md` – High-level architecture  
- `LLD.md` – Class and component-level breakdown  
- `/docs/agent_docs/` – Each agent’s responsibility, input/output  
- `/docs/prompts.md` – Standardized prompt strategies  
- `/docs/examples/` – Sample queries and JSON responses  

## 🤝 License

MIT License — built for educational, enterprise, and interview showcase use.

## 🚀 Author

**Bhagwat Chate**  
AI/ML Lead | GenAI Architect  
📫 [LinkedIn](https://www.linkedin.com/in/aimlbhagwatchate) • [GitHub](https://github.com/bhagwat-chate)
