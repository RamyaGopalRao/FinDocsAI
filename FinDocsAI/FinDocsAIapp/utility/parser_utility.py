from ..models  import Document, BankStatement, Invoice, TaxDocument, Contract, FinancialReport
from .parser import parse_document,extract_text
import json


def parse_document(file_path, document_type):
    # Extract text
    document_text = extract_text(file_path)
    if "Error" in document_text:
        return document_text

    # Load prompt and fields
    prompt, fields = load_prompt(document_type)
    if not prompt or not fields:
        return f"Unsupported document type: {document_type}"

    # Call OpenAI API
    response = call_openai_api(prompt, document_text)

    # Extract JSON from the response
    try:
        start_index = response.find("{")
        end_index = response.rfind("}") + 1
        if start_index != -1 and end_index != -1:
            json_data = response[start_index:end_index]
            parsed_data = json.loads(json_data)
            return {field: parsed_data.get(field) for field in fields}
        else:
            return "No valid JSON data found in response."
    except json.JSONDecodeError as e:
        return f"Error parsing JSON: {e}"

def parse_and_save(document):
    with open(document.file.path, 'rb') as f:
        # Example parsing logic
        if document.document_type == 'bank_statement':
            usermessage=""
            parsed_data = parse_resume(f,usermessage)
            BankStatement.objects.create(
                document=document,
                transaction_date=parsed_data['transaction_date'],
                description=parsed_data['description'],
                amount=parsed_data['amount'],
                balance=parsed_data['balance']
            )
        elif document.document_type == 'invoice':
            usermessage=""
            parsed_data = parse_document(document.file.path)
            Invoice.objects.create(
                document=document,
                invoice_number=parsed_data['invoice_number'],
                vendor_name=parsed_data['vendor_name'],
                date_issued=parsed_data['date_issued'],
                total_amount=parsed_data['total_amount']
            )
        # Add parsing logic for other document types
