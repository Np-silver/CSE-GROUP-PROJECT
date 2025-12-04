Universal Audiobook Converter

A full-stack web application that automatically converts your documents (PDF, DOCX, TXT) into natural-sounding audiobooks (MP3) using Python, Flask, and Google's Text-to-Speech AI.

Overview

The Universal Audiobook Converter is designed to make reading materials accessible and portable. Whether you are a student wanting to listen to lecture notes while commuting, or a professional reviewing reports on the go, this tool bridges the gap between text and audio.

It features a clean, responsive web interface that allows for instant file uploads, processing, and playback directly in the browser.

Key Features

Multi-Format Support: Natively handles .pdf, .docx, and .txt files.

Smart Text Extraction: automatically cleans formatting issues (like hard line breaks) to ensure smooth speech flow.

Natural Voice Synthesis: Powered by gTTS (Google Text-to-Speech) for high-quality, non-robotic audio.

Instant Playback: Listen to the audio immediately in the browser before downloading.

Privacy Focused: Automatically deletes uploaded files after processing to ensure data security.

Responsive Design: Works seamlessly on desktops, tablets, and mobile devices.

Tech Stack

Backend: Python 3, Flask (Micro-framework)

Frontend: HTML5, CSS3, Vanilla JavaScript (Fetch API)

Libraries:

PyPDF2 - PDF parsing

python-docx - Word document parsing

gTTS - Audio synthesis API

Werkzeug - Secure file handling

Installation & Setup

Follow these steps to run the project locally on your machine.

1. Clone the Repository

git clone [https://github.com/yourusername/audiobook-converter.git](https://github.com/yourusername/audiobook-converter.git)
cd audiobook-converter


2. Set Up a Virtual Environment (Recommended)

It is best practice to use a virtual environment to keep dependencies isolated.

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

python app.py


5. Access the Web Interface

Open your web browser and navigate to:
http://127.0.0.1:5000/

Project Structure

CSE-PROJECT

├──readme.md 

├── requirements.txt

├──  app.py      

├── style.css   

└── index.html        


How to Use

Upload: Click "Choose File" and select a PDF, Word Doc, or Text file from your computer.

Convert: Click the "Convert to MP3" button.

Wait: A loading indicator will appear while the text is extracted and synthesized.

Listen: Once done, an audio player will appear. Press play to listen.

Download: Click the "Download MP3" link to save the file to your device.

Future Improvements

OCR Integration: Add support for scanned PDFs and images using Tesseract.

Multi-Language Support: Auto-detect document language and switch voice accents (e.g., Spanish, French).

Voice Customization: Allow users to select gender (Male/Female) and reading speed.

PWA Support: Turn the web app into an installable mobile app.
