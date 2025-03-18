from django.urls import path
from . import views

urlpatterns = [
    # Route to upload documents
    path('upload/', views.upload_document, name='upload_document'),

    # Route for success page (optional)
    path('success/', views.success_page, name='success_page'),

    # Route to list all processed documents (optional)
    path('documents/', views.document_list, name='document_list'),

    # Route to view the details of a single document (optional)
    path('documents/<int:id>/', views.document_detail, name='document_detail'),
]
