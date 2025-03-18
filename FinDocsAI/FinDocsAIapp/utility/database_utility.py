from ..models import BankStatement,Invoice,FinancialReport,TaxDocument,Contract,Document
from django.shortcuts import render, get_object_or_404
def save_parsed_data(document, parsed_data):
    """
    Saves parsed data into the appropriate model based on the document type.
    """
    if document.document_type == 'bank_statement':
        for transaction in parsed_data:
            BankStatement.objects.create(
                document=document,
                transaction_date=transaction['transaction_date'],
                description=transaction['description'],
                amount=transaction['amount'],
                balance=transaction['balance']
            )
    elif document.document_type == 'invoice':
        Invoice.objects.create(
            document=document,
            invoice_number=parsed_data['invoice_number'],
            vendor_name=parsed_data['vendor_name'],
            date_issued=parsed_data['date_issued'],
            total_amount=parsed_data['total_amount']
        )
    elif document.document_type == 'tax_document':
        TaxDocument.objects.create(
            document=document,
            taxpayer_name=parsed_data['taxpayer_name'],
            tax_year=parsed_data['tax_year'],
            income=parsed_data['income'],
            tax_paid=parsed_data['tax_paid']
        )
    elif document.document_type == 'contract':
        Contract.objects.create(
            document=document,
            parties_involved=parsed_data['parties_involved'],
            start_date=parsed_data['start_date'],
            end_date=parsed_data['end_date'],
            key_clauses=parsed_data['key_clauses']
        )
    elif document.document_type == 'financial_report':
        FinancialReport.objects.create(
            document=document,
            report_type=parsed_data['report_type'],
            period=parsed_data['period'],
            total_revenue=parsed_data['total_revenue'],
            net_profit=parsed_data['net_profit']
        )





def document_detail(request, id):
    document = get_object_or_404(Document, id=id)

    if document.document_type == 'bank_statement':
        parsed_data = BankStatement.objects.filter(document=document)
    elif document.document_type == 'invoice':
        parsed_data = Invoice.objects.filter(document=document)
    elif document.document_type == 'tax_document':
        parsed_data = TaxDocument.objects.filter(document=document)
    elif document.document_type == 'contract':
        parsed_data = Contract.objects.filter(document=document)
    elif document.document_type == 'financial_report':
        parsed_data = FinancialReport.objects.filter(document=document)
    else:
        parsed_data = None

    return render(request, 'document_detail.html', {
        'document': document,
        'parsed_data': parsed_data,
    })

