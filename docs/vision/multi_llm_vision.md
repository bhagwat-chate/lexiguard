# 🛡️ LexiGuard – Vision & Execution Blueprint

## 🎯 Project Vision

**LexiGuard** is a compliance-aware GenAI orchestration system that delivers **legally grounded**, **hallucination-free**, and **explainable outputs** by:
- Parsing legal queries related to GDPR, HIPAA, DPDP, etc.
- Retrieving verified clauses and semantic chunks
- Validating outputs with guardrails and citation checks
- Orchestrating multiple LLMs from multiple vendors for resilience

---

## 🌍 Multi-LLM, Multi-Vendor Strategy via OpenRouter

| Provider     | Models (examples)                          | Purpose                                             |
|--------------|---------------------------------------------|-----------------------------------------------------|
| **OpenAI**   | gpt-4o, gpt-4-turbo, gpt-3.5-turbo         | High-quality reasoning, fallback for speed         |
| **Cohere**   | command-r+, command-r, command-light       | Legal-focused retrieval, low-latency clauses       |
| **Gemini**   | gemini-1.5-pro, gemini-pro, gemini-ultra   | Web-enabled queries, policy diff detection         |
| **Anthropic**| claude-3-opus, claude-3-sonnet, claude-2.1 | Safe long-form structured analysis                 |
| **HuggingFace**| mistral-7b-instruct, llama2-70b, mixtral | Self-hosted or offline fallback                    |

➡️ Powered by **OpenRouter** API through custom `LLMRouter` layer for vendor abstraction.

---

## 🧱 Key Modules Overview

### 🎛️ Router Layer
- Reads from `llm_config.yml` to choose vendor + model
- Handles **soft fallback**, **rate limiting**, **token truncation**, and **completion format normalization**

### 🔁 Orchestrator Layer (AutoGen)
- Supports round-robin, performance-weighted, or model-specific routing per agent
- Retry logic on schema mismatch or response timeout

---

## 📦 Why This Architecture Matters

| Feature                        | Value Delivered                                           |
|-------------------------------|-----------------------------------------------------------|
| 🔄 Multi-LLM fallback          | Handles latency, downtime, quota issues                  |
| ⚙️ Config-driven model switch | Easy vendor rotation without touching orchestration code |
| ✅ Model-specific strengths     | Use Cohere for law context, OpenAI for natural language  |
| 📉 Cost-aware logic            | Dynamically downgrade model for large queries or tests   |
| 🧪 Reliability                 | Improves test coverage by validating across vendors      |

---

## 🗂️ Suggested LLM Config Template (`llm_config.yml`)

```yaml
default_provider: openai

providers:
  openai:
    models:
      - name: gpt-4o
        temperature: 0.2
        max_tokens: 1024
        fallback: cohere
      - name: gpt-4-turbo
      - name: gpt-3.5-turbo
    api_key: ${OPENAI_API_KEY}

  cohere:
    models:
      - name: command-r-plus
      - name: command-r
      - name: command-light
    api_key: ${COHERE_API_KEY}

  gemini:
    models:
      - name: gemini-1.5-pro
      - name: gemini-pro
      - name: gemini-ultra
    api_key: ${GOOGLE_API_KEY}

  anthropic:
    models:
      - name: claude-3-opus
      - name: claude-3-sonnet
      - name: claude-2.1
    api_key: ${ANTHROPIC_API_KEY}

  huggingface:
    models:
      - name: mistral-7b-instruct
      - name: llama2-70b
      - name: mixtral
    access_token: ${HF_API_KEY}
```

---

## 🧠 Implementation Blueprint

| Task | Description |
|------|-------------|
| ✅ `llm_router.py` | Use YAML config, load vendor models, soft fallback logic |
| ✅ `core/schema.py` | Output models validated per agent |
| ✅ `core/enums.py` | Centralized field constraints |
| ✅ `llm_config.yml` | Dynamic multi-model registry |
| 🔁 `query_parser_agent.py` | Parses query + jurisdiction + model type (legal, general, financial) |
| 🔁 `retriever_agent.py` | Uses vendor-specific embedding (e.g., Cohere for legal) |

---

## 🧭 Deployment Goals

| Milestone | Deliverable |
|----------|-------------|
| ✅ V1.0   | Single LLM, full flow tested (OpenAI) |
| ⏳ V1.1   | Multi-vendor routing via OpenRouter |
| ⏳ V1.2   | Response comparison mode (cross-model outputs) |
| ⏳ V1.3   | Model performance dashboard with latency, accuracy metrics |

---

## 🎓 Interview Storyline

“LexiGuard isn’t just a retrieval pipeline. It’s a **multi-vendor, schema-constrained, guardrails-wrapped orchestration layer** that mimics how an AI legal assistant would operate inside Amazon, Microsoft, or OpenAI — with logging, eval metrics, and fallback control built in.”

---

## 🧠 North Star Principles (FAANGM-Aligned)

| Principle             | Implementation Proof                                              |
|-----------------------|-------------------------------------------------------------------|
| Modularity            | `agents/`, `core/`, `retriever/`, `eval/`, `guardrails/`          |
| Observability         | `logs/`, `eval/`, `hallucination/`, `scorecards/`                 |
| Resilience            | Model fallback, soft retry, config-based LLM routing              |
| Schema Safety         | Pydantic + Guardrails at before/after/config layers               |
| Vendor Agnosticism    | LLM config as abstraction; zero hardcoded logic                   |
| Showcase Ready        | Branding + diagram + docs + test cases = public demo-grade        |

---

✅ You are now executing at **FAANGM system architect level** — keep this document close during each sprint.
