from flask import Flask, render_template_string
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    # Read the index.html file directly to avoid Flask template syntax conflicts usually found in frontend frameworks
    # or just to simply perform the string replacement as requested.
    try:
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Inject the API key
        api_key = os.getenv("GEMINI_API_KEY", "")
        # The frontend expects: const apiKey = ""; 
        # We replace it with the actual key.
        content = content.replace('const apiKey = "";', f'const apiKey = "{api_key}";')
        
        return render_template_string(content)
    except FileNotFoundError:
        return "Error: templates/index.html not found. Please ensure the file exists."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
