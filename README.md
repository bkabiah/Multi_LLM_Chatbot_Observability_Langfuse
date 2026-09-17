#  Enterprise Multi-LLM Chatbot Framework

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

## 🚀 Quick Start
```bash
pip install -U litellm gradio python-dotenv PyPDF2 "langfuse<=2.50.0"
python app.py
```
