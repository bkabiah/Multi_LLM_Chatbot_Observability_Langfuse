import base64
import mimetypes
import PyPDF2
import os

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_files(file_paths):
    extracted_text = ""
    images = []

    if not file_paths:
        return extracted_text, images

    for path in file_paths:
        mime_type, _ = mimetypes.guess_type(path)
        ext = path.split('.')[-1].lower()
        file_name = os.path.basename(path)

        if mime_type and mime_type.startswith('image'):
            base64_img = encode_image(path)
            images.append(f"data:{mime_type};base64,{base64_img}")
        elif ext == 'pdf':
            try:
                with open(path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    text = ""
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted:
                            text += extracted + "\n"
                    extracted_text += f"\n--- Inhalt von {file_name} ---\n{text}\n"
            except Exception as e:
                extracted_text += f"\n[Fehler beim Lesen der PDF {file_name}: {str(e)}]\n"
        elif ext in ['csv', 'json', 'md', 'txt']:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    extracted_text += f"\n--- Inhalt von {file_name} ---\n{content}\n"
            except Exception as e:
                extracted_text += f"\n[Fehler beim Lesen der Datei {file_name}: {str(e)}]\n"
        else:
            extracted_text += f"\n[Datei {file_name} wurde ignoriert (Nicht unterstütztes Format)]\n"

    return extracted_text, images
