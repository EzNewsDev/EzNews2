import os
import google.generativeai as genai
import json

def generate_summary(content, filters, length='medium'):
    """
    Generate AI summary based on content and filters using Google Gemini API.
    """
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        return {
            'error': 'Gemini API Key not found. Please set GEMINI_API_KEY in .env',
            'who': 'API Key Missing',
            'what': 'API Key Missing',
            'where': 'API Key Missing',
            'when': 'API Key Missing',
            'why': 'API Key Missing',
            'how': 'API Key Missing'
        }

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')

        # Construct dynamic JSON structure example
        json_structure = ",\n            ".join([f'"{f}": "..."' for f in filters])
        
        prompt = f"""
        Analyze the following news article and extract the specific information requested below.
        Return the result ONLY as a valid JSON object. Do not include markdown formatting like ```json ... ```.
        
        Article Content:
        "{content[:4000]}"... (truncated if too long)

        Requested Information (Filters): {', '.join(filters)}
        Target Length per section: {length}

        JSON Structure required:
        {{
            {json_structure}
        }}
        
        IMPORTANT: Only include the keys listed above ({', '.join(filters)}). Do not add any other keys. Translate the analysis to Indonesian.
        Keep the summary for each section very concise and to the point (max 1-2 sentences).
        """

        response = model.generate_content(prompt)
        
        # Clean up response if it contains markdown code blocks
        text_response = response.text.replace('```json', '').replace('```', '').strip()
        
        result = json.loads(text_response)
        
        # Strict filtering: Only return keys that were requested
        filtered_result = {k: v for k, v in result.items() if k in filters}
        
        return filtered_result

    except Exception as e:
        print(f"Gemini API Error: {e}")
        # Fallback to mock/error message if API fails
        return {k: "Gagal memuat ringkasan AI." for k in filters}

def extract_who(content, length): return ""
def extract_when(content, length): return ""
def extract_where(content, length): return ""
def extract_what(content, length): return ""
def extract_why(content, length): return ""
def extract_how(content, length): return ""
