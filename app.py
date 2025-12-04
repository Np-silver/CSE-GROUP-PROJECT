from flask import Flask, render_template, request, send_file
from gtts import gTTS
import PyPDF2
import docx
import os

app = Flask(__name__)

def extract_text(file_path, ext):
    text = ""
    try:
        if ext == 'pdf':
            reader = PyPDF2.PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text() or ""
        elif ext == 'docx':
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + " "
        elif ext == 'txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    ext = file.filename.split('.')[-1].lower()
    input_path = f"temp_input.{ext}"
    file.save(input_path)

    text = extract_text(input_path, ext)

    if not text.strip():
        return "Could not extract text", 400

    output_path = "output_audio.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

    os.remove(input_path)
    
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

