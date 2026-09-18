import gradio as gr
from config import config

def create_ui(chat_fn, reset_fn):
    with gr.Blocks(title="Multi-LLM Enterprise Engine") as demo:
        gr.Markdown("# Enterprise Multi-LLM Engine (V7)")
        gr.Markdown("Mit Datei-Upload (PDF, CSV, JSON, MD) und Bild-Analyse (Vision).")
        
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(height=450)
                msg = gr.Textbox(placeholder="Ihre Frage an das System...", label="Nachricht")
                
                with gr.Accordion("📎 Dateien & Bilder anhängen", open=False):
                    file_uploader = gr.File(
                        label="Unterstützt: Bilder, PDF, CSV, JSON, MD", 
                        file_count="multiple", 
                        type="filepath"
                    )
                
                status_bar = gr.Markdown("Bereit.")
                
                with gr.Row():
                    submit_btn = gr.Button("Senden", variant="primary")
                    clear_btn = gr.Button("Clear History")
                    
            with gr.Column(scale=1):
                gr.Markdown("### Steuerzentrale")
                model_selector = gr.Dropdown(
    choices=list(config.SUPPORTED_MODELS.keys()),
    value="Gemini Flash Latest (Google)",  # <-- ANGEPASST
    label="LLM Modell wählen"
)
                temp_slider = gr.Slider(
                    minimum=0.0, maximum=1.0, value=0.7, step=0.1, 
                    label="Temperature"
                )
                sys_prompt = gr.Textbox(
                    value="Du bist ein präziser, hilfreicher AI Assistant für Software Engineers.",
                    label="System Prompt",
                    lines=3
                )

        input_components = [msg, chatbot, file_uploader, model_selector, temp_slider, sys_prompt]
        output_components = [msg, chatbot, file_uploader, status_bar]
        
        msg.submit(chat_fn, input_components, output_components)
        submit_btn.click(chat_fn, input_components, output_components)
        clear_btn.click(reset_fn, outputs=[chatbot, status_bar])

    return demo
