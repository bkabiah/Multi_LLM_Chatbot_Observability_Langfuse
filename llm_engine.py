import litellm
from litellm import completion
from typing import Dict, Any
from config import config

# litellm.success_callback = ["langfuse"]
# litellm.failure_callback = ["langfuse"]

class AgnosticLLMClient:
    def generate_response(
        self, 
        model_name: str, 
        messages: list, 
        temperature: float = 0.7, 
        max_tokens: int = 1024,
        session_id: str = "default_session"
    ) -> Dict[str, Any]:
        
        langfuse_metadata = {
            "session_id": session_id,
            "tags": ["llm-engine", "production", model_name],
            "user_id": "colab_demo_user"
        }
        
        try:
            response = completion(
                model=model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                metadata=langfuse_metadata
            )
            return {
                "content": response.choices[0].message.content,
                "model_used": response.model,
                "tokens_used": response.usage.total_tokens,
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "fallback_triggered": False
            }
        except Exception as primary_error:
            print(f"[WARN] Primäres Modell {model_name} fehlgeschlagen: {str(primary_error)}.")
            
            for fallback_model in config.FALLBACK_CHAIN:
                if fallback_model == model_name:
                    continue
                try:
                    print(f"[INFO] Versuche Fallback-Modell: {fallback_model}")
                    
                    fallback_metadata = langfuse_metadata.copy()
                    fallback_metadata["tags"] = ["llm-engine", "fallback-triggered", fallback_model]
                    
                    response = completion(
                        model=fallback_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        metadata=fallback_metadata
                    )
                    return {
                        "content": response.choices[0].message.content,
                        "model_used": f"{response.model} (Fallback)",
                        "tokens_used": response.usage.total_tokens,
                        "prompt_tokens": response.usage.prompt_tokens,
                        "completion_tokens": response.usage.completion_tokens,
                        "fallback_triggered": True
                    }
                except Exception:
                    continue
            
            raise RuntimeError(f"Alle Modelle fehlgeschlagen. Fehler: {str(primary_error)}")
