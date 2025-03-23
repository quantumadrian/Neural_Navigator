import google.generativeai as genai
import PyPDF2
from dotenv import load_dotenv
import os


load_dotenv()
class Flashcards:
    def setup_gemini(self):
        api_key=os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-flash')

    # Extract text from PDF
    def extract_text_from_pdf(self,uploaded_file):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    # Generate flashcards using Gemini
    def generate_flashcards(self,text, gemini_model):
        prompt = f"""
        Generate flashcards from the following text. For each key concept, create a question and a concise answer.
        Format each flashcard as:
        Q: [question]
        A: [answer]

        Text:
        {text}
        """
        try:
            response = gemini_model.generate_content(prompt)
            print("Gemini Response:", response.text)
            return response.text
        except Exception as e:
            print(f"Error generating flashcards: {e}")
            return f"Error generating flashcards: {str(e)}"
        