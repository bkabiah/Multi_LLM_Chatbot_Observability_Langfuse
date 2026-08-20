import os

def init_langfuse():
    """Prüft und setzt Langfuse-Schlüssel für LiteLLM."""
    pub_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
    
    if pub_key and secret_key:
        os.environ["LANGFUSE_PUBLIC_KEY"] = pub_key
        os.environ["LANGFUSE_SECRET_KEY"] = secret_key
        os.environ["LANGFUSE_HOST"] = host
        return True
    return False
