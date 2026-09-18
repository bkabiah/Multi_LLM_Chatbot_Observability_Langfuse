#   Multi-LLM Chatbot Framework

## 📖 Einführung

Das **Enterprise Multi-LLM Chatbot Framework** ist eine hochverfügbare, modulare und LLM-agnostische Lösung, die speziell für professionelle Anwendungsfälle im Software-Engineering entwickelt wurde. Es kombiniert intelligentes, dynamisches Routing über LiteLLM mit einer robusten Fallback-Kette, um Zero-Downtime bei API-Ausfällen oder Rate-Limits zu garantieren. Durch die native Integration von Langfuse bietet das System Enterprise-grade Observability für präzises Token-, Kosten- und Performance-Tracking. Ein automatisierter Multimodal-Parser ermöglicht zudem die nahtlose Verarbeitung von PDFs, CSV, JSON, Markdown und Bildern (Vision) direkt im Chat-Verlauf. Dank der strikten Trennung von UI, Business-Logik und Infrastruktur ist das Framework ideal für den produktiven Einsatz und eine einfache Skalierung in Cloud-Umgebungen geeignet.
Ein robustes, LLM-agnostisches Chat-Framework mit dynamischem Routing, integrierter Telemetrie (Langfuse), Fallback-Sicherheit und nativem Multimodal-Support (PDF, CSV, JSON, MD, Bilder).

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![LiteLLM](https://img.shields.io/badge/Routing-LiteLLM-green)
![Langfuse](https://img.shields.io/badge/Observability-Langfuse-purple)

##  Warum dieses Projekt?

* 🛡️**Zero-Downtime Fallback Chain:** Automatisches Ausfall-Routing bei API-Problemen.
* 📊 **Enterprise Observability:** Langfuse Tracing für Kosten- und Tokenkontrolle.
*  **LLM-Agnostisch:** 100+ Modelle via LiteLLM nutzbar.
* 📎 **Auto-Parsing:** Automatischer Text-Import für PDF, CSV, JSON, MD & Base64 Vision für Bilder.
* 🧩 **Modulare Architektur:** Klare Trennung von Backend, UI, Memory & Utility-Dateien.

## 🛠️ Tech Stack
* Frontend: Gradio
* Routing: LiteLLM
* Observability: Langfuse
* Parsing: PyPDF2, base64, mimetypes

## 🏗️ Architektur

Das System folgt einer klar getrennten, modularen Architektur, die Wartbarkeit und Testbarkeit sicherstellt:

```mermaid
graph TD
    User([👤 Benutzer]) -->|Interaktion| UI[🖥️ Gradio UI<br/>app.py / ui.py]
    
    UI -->|1. Nachricht & Dateien| FU[📂 file_utils.py<br/>Parser & Base64]
    UI -->|2. Verlauf| MEM[🧠 ConversationMemory<br/>memory.py]
    
    FU -->|Extrahierter Text / Bilder| APP[⚙️ Chat Interface<br/>app.py]
    MEM -->|Formatierter Prompt| APP
    
    APP -->|3. Anfrage mit Metadaten| LLM[🤖 AgnosticLLMClient<br/>llm_engine.py]
    
    LLM -->|4. Primary Request| LITE[🔀 LiteLLM Router]
    LITE -->|Erfolg| EXT1((🌐 Externe LLMs<br/>GPT-4o, Claude, Gemini, Llama))
    LITE -->|Fehler| FB[🛡️ Fallback Chain<br/>config.py]
    FB -->|Retry| EXT2((🌐 Fallback LLMs))
    
    LLM -.->|5. Telemetrie & Tracing| OBS[📊 Langfuse<br/>observability.py]
    
    EXT1 -->|Antwort| LLM
    EXT2 -->|Antwort| LLM
    LLM -->|6. Formatierter Response| UI


## 🚀 Quick Start
```bash
pip install -U litellm gradio python-dotenv PyPDF2 "langfuse<=2.50.0"
python app.py
```
