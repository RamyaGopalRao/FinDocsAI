# FinDocsAI

## Overview

**FinDocsAI** is an intelligent document management and processing system designed to handle various financial documents, including bank statements, invoices, tax documents, contracts, and financial reports. It enables users to upload, store, and parse financial documents with structured relational data storage and robust audit tracking.

This system is built using Django, leveraging its powerful ORM for data modeling and relationship management.

---

## Features

- **Document Upload**: Supports uploading various document types (PDFs, images, etc.).
- **Parsed Data Management**: Extracts relevant metadata and structured details for specific document types.
- **Audit Logs**: Tracks creation and modification timestamps with an `AuditModel`.
- **Relational Data Structure**: Links documents to their respective parsed data for efficient access and management.
- **Scalable Design**: New document types or parsing structures can be added with minimal changes.
- **User Interface**: Displays all uploaded documents and their parsed information with clean, user-friendly templates.

---

## Project Architecture

The project follows Django's default architecture and is organized as shown below:

```plaintext
FinDocsAI/
├── FinDocsAI/
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project-level URL configuration
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
├── FinDocsAIapp/
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   ├── document_list.html  # Template for document list
│   │   └── document_details.html  # Template for document details
│   ├── static/               # Static files (CSS/JS)
│   ├── admin.py              # Admin interface configuration
│   ├── apps.py               # App-specific settings
│   ├── models.py             # Database models
│   ├── views.py              # Application views
│   ├── urls.py               # App-level URL configuration
│   └── tests.py              # Unit tests
├── manage.py                 # Django management script
└── db.sqlite3                # SQLite database
