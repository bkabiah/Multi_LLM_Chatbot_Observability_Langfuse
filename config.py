import os
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class LLMConfig:
    SUPPORTED_MODELS: Dict[str, str] = field(default_factory=lambda: {
        "Gemini 1.5 Pro (Google)": "gemini/gemini-1.5-pro",
        "GPT-4o (OpenAI)": "gpt-4o",
        "Claude 3.5 Sonnet (Anthropic)": "claude-3-5-sonnet-20240620",
        "Llama 3.3 70B (Groq)": "groq/llama-3.3-70b-versatile",
        "Mistral Large (Mistral)": "mistral/mistral-large-latest"
    })
    
    DEFAULT_MODEL: str = "gemini/gemini-1.5-pro"
    DEFAULT_TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 1024
    
    FALLBACK_CHAIN: List[str] = field(default_factory=lambda: [
        "gemini/gemini-1.5-pro",
        "claude-3-5-sonnet-20240620"
    ])

config = LLMConfig()
