import json
import os
from PyPDF2 import PdfReader
from docx import Document
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def load_config(document_type, config_file="config/config.json"):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config.get(document_type)
    except FileNotFoundError:
        raise ValueError(f"Configuration file not found: {config_file}")
    except KeyError:
        raise ValueError(f"Document type '{document_type}' not found in configuration.")

def extract_text(file_path):
    text = ""
    try:
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text()
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'
        else:
            return "Unsupported file format."
    except Exception as e:
        return f"Error reading file: {e}"
    return text



def call_openai_api(user_message, text):
    try:
        # Initialize the OpenAI client
        client = OpenAI(api_key=api_key)

        # Request a completion from the OpenAI model
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_message +text}
            ]
        )

        # Extract and clean the bot's response
        bottext = completion.choices[0].message.content.strip()
        print("Raw Bot Response:", bottext)

        # Identify the JSON content within braces
        start_index = bottext.find("{")
        end_index = bottext.rfind("}") + 1
        if start_index != -1 and end_index != -1:
            json_text = bottext[start_index:end_index]
        else:
            return "No valid JSON-like data found within braces."

        # Convert JSON text to a Python dictionary
        cleaned_data = json.loads(json_text.replace("'", '"'))
        print("Cleaned Data:", cleaned_data)

        # Return the parsed dictionary
        return cleaned_data

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return f"Error parsing JSON: {e}"
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

# Example usage



def parse_document(text, document_type, config_path='config/config.json'):
    #text = extract_text(file_path)
    if "Error" in text:
        return text

    with open(config_path) as f:
        config = json.load(f)
    prompt = config[document_type]["prompt"]
    fields = config[document_type]["fields"]

    response = call_openai_api(prompt, text)

    try:
        json_data = json.loads(response.replace("'", '"'))
        return {field: json_data.get(field, None) for field in fields}
    except json.JSONDecodeError as e:
        return f"Error parsing JSON response: {e}"

# Example usage
