from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .utility.parser import extract_text,parse_document,load_config
from .utility.database_utility import save_parsed_data
from django.shortcuts import render
from .models import Document

# Success page view
def success_page(request):
    return render(request, 'FinDocsAIapp/success.html')

# List all documents
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'FinDocsAIapp/document_list.html', {'documents': documents})

# View a specific document's details
def document_detail(request, id):
    document = Document.objects.get(id=id)
    return render(request, 'FinDocsAIapp/document_detail.html', {'document': document})


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            # Extract text from the uploaded file
            text = extract_text(document.file.path)

            # Load configuration based on document type
            config = load_config(document.document_type)

            # Parse the document using the text and configuration
            parsed_data = parse_document(text, config)

            # Save parsed data to the database
            save_parsed_data(document, parsed_data)

            # Redirect to success page
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'FinDocsAIapp/upload.html', {'form': form})



def parse_documents(text,document_type,):
    """
    Parses the document using configuration prompts and fields.
    """
    parse_document(text,document_type)

    # Here, integrate OpenAI or any parsing mechanism with the configuration
