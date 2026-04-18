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
        
        # Log status (only first 4 chars for safety)
        if api_key:
            print(f"DEBUG: GEMINI_API_KEY loaded successfully (starts with: {api_key[:4]}...)")
        else:
            print("WARNING: GEMINI_API_KEY is not set in environment variables!")

        # The frontend expects: const apiKey = ""; 
        # We replace it robustly with regex to handle potential whitespace variations
        import re
        content = re.sub(r'const apiKey\s*=\s*".*";', f'const apiKey = "{api_key}";', content)
        
        return render_template_string(content)
    except FileNotFoundError:
        return "Error: templates/index.html not found. Please ensure the file exists."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
