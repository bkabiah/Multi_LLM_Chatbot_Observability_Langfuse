import uuid
from dotenv import load_dotenv
load_dotenv() 

from config import config
from memory import ConversationMemory
from llm_engine import AgnosticLLMClient
from observability import init_langfuse
from ui import create_ui
from file_utils import process_files

client = AgnosticLLMClient()
memory = ConversationMemory(max_history_turns=10)

def chat_interface(user_message, history, files, model_display_name, temperature, system_prompt):
    if not user_message.strip() and not files:
        return "", history, files, "Bitte Nachricht oder Datei eingeben."
    
    session_id = str(uuid.uuid4())[:8]
    model_identifier = config.SUPPORTED_MODELS[model_display_name]
    
    doc_text, base64_images = process_files(files)
    
    final_user_text = user_message
    if doc_text:
        final_user_text += f"\n\n--- Angehängte Dokumente ---\n{doc_text}"
        
    if base64_images:
        content = [{"type": "text", "text": final_user_text or "Bitte beschreibe das angehängte Bild."}]
        for img in base64_images:
            content.append({"type": "image_url", "image_url": {"url": img}})
    else:
        content = final_user_text
        
    memory.add_message("user", content)
    formatted_messages = memory.get_messages(system_prompt=system_prompt)
    
    try:
        result = client.generate_response(
            model_name=model_identifier,
            messages=formatted_messages,
            temperature=temperature,
            max_tokens=config.MAX_TOKENS,
            session_id=session_id
        )
        
        reply = result["content"]
        memory.add_message("assistant", reply)
        
        status_info = (
            f" Modell: **{result['model_used']}** | "
            f" Token: **{result['tokens_used']}** | "
            f" Session: `{session_id}`"
        )
        if result["fallback_triggered"]:
            status_info = "⚠️ **Fallback ausgelöst!** " + status_info
            
        ui_msg = user_message
        if files:
            ui_msg = f"📎 [{len(files)} Anhänge] " + ui_msg
            
        history.append((ui_msg, reply))
        return "", history, None, status_info 

    except Exception as e:
        if memory.history:
            memory.history.pop()
        error_msg = f"Fehler bei der Ausführung: {str(e)}"
        return user_message, history, files, f"❌ {error_msg}"

def reset_chat():
    memory.clear()
    return [], "Chat zurückgesetzt."

if __name__ == "__main__":
    init_langfuse()
    demo = create_ui(chat_fn=chat_interface, reset_fn=reset_chat)
    demo.launch(share=True, debug=True)
