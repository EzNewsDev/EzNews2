from app.services.ai_summary import generate_summary
import os
from dotenv import load_dotenv

load_dotenv()

print(f"API Key present: {bool(os.getenv('GEMINI_API_KEY'))}")

content = "Presiden Joko Widodo meresmikan jembatan baru di Kalimantan hari ini."
filters = ["who", "what", "where", "when"]

print("Generating summary...")
result = generate_summary(content, filters)
print(f"Result: {result}")
