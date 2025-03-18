from django.db import models

# Parent Model to Store Uploaded Files
class Document(models.Model):
    DOCUMENT_TYPES = [
        ('bank_statement', 'Bank Statement'),
        ('invoice', 'Invoice'),
        ('tax_document', 'Tax Document'),
        ('contract', 'Contract Agreement'),
        ('financial_report', 'Financial Report'),
    ]
    title = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Parsed Data for Bank Statements
class BankStatement(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    description = models.TextField()
    amount = models.FloatField()
    balance = models.FloatField()

# Parsed Data for Invoices
class Invoice(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=255)
    date_issued = models.DateField()
    total_amount = models.FloatField()

# Parsed Data for Tax Documents
class TaxDocument(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    taxpayer_name = models.CharField(max_length=255)
    tax_year = models.IntegerField()
    income = models.FloatField()
    tax_paid = models.FloatField()

# Parsed Data for Contracts
class Contract(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    parties_involved = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    key_clauses = models.TextField()

# Parsed Data for Financial Reports
class FinancialReport(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=255)
    period = models.CharField(max_length=100)
    total_revenue = models.FloatField()
    net_profit = models.FloatField()
