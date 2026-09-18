import os
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class LLMConfig:
    SUPPORTED_MODELS: Dict[str, str] = field(default_factory=lambda: {
    "Gemini Flash Latest (Google)": "gemini/gemini-flash-latest", # <-- HIER die ID nutzen (ohne models/ Präfix, litellm fügt das hinzu)
    # ... andere Modelle können bleiben oder auskommentiert werden ...
    "GPT-4o (OpenAI)": "gpt-4o",
    "Claude 3.5 Sonnet (Anthropic)": "claude-3-5-sonnet-20240620",
    "Llama 3.1 70B (Groq)": "groq/llama3-70b-8192",
    "Mistral Large (Mistral)": "mistral/mistral-large-latest"
})
    
    DEFAULT_MODEL: str = "gemini/gemini-1.5-flash"
    DEFAULT_TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 1024
    
    FALLBACK_CHAIN: List[str] = field(default_factory=lambda: [
    "groq/llama3-70b-8192",  # Zuerst Groq versuchen
    "gemini/gemini-flash-latest"  # Dann Google
])
 	  
config = LLMConfig()
