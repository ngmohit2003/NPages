# N-Pages

A developer-focused knowledge management platform built with **FastAPI**, **PostgreSQL**, and **Supabase**.

N-Pages allows users to securely create, manage, search, and organize technical notes while supporting file attachments and enterprise-grade authorization through Row Level Security (RLS).

---

# Project Status

**Current Version:** v0.4

### Completed Modules

✅ Authentication

✅ User Authorization

✅ Notes CRUD

✅ Row Level Security (RLS)

✅ File Upload System

✅ File Management

✅ Storage Integration

✅ Secure Ownership Validation

---

# Project Vision

N-Pages is designed as a production-style SaaS backend demonstrating modern backend engineering practices:

* Authentication
* Authorization
* Secure Storage
* REST APIs
* Database Design
* Search Systems
* Multi-Tenant Architecture
* Future AI-Powered Knowledge Retrieval

The platform is targeted toward:

* Researchers
* Students
* Engineers
* Developers
* Technical Professionals

---

# Technology Stack

## Backend

* FastAPI
* Uvicorn
* Python 3.12+

## Database

* PostgreSQL
* Supabase PostgreSQL

## Authentication

* Supabase Auth
* JWT Tokens

## Storage

* Supabase Storage

## Security

* PostgreSQL Row Level Security (RLS)
* Ownership Validation
* JWT Authentication

---

# System Architecture

```text
┌─────────────────────┐
│      Frontend       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      FastAPI        │
│     REST APIs       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│            Supabase             │
├─────────────────────────────────┤
│ Authentication (JWT)            │
│ PostgreSQL Database             │
│ Storage Buckets                 │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────┐
│      PostgreSQL     │
│   Notes & Metadata  │
└─────────────────────┘
```

---

# Database Schema

## notes

Stores user-created notes.

```text
notes
│
├── id
├── user_id
├── title
├── content
├── created_at
└── updated_at
```

---

## note_files

Stores metadata for uploaded files.

```text
note_files
│
├── id
├── note_id
├── file_name
├── file_url
├── storage_path
└── created_at
```

---

# Storage Structure

Files are stored inside Supabase Storage.

```text
note-files/
│
├── user_id/
│   ├── uuid-file-1.png
│   ├── uuid-file-2.pdf
│   └── uuid-file-3.jpg
│
└── user_id/
    ├── uuid-file-4.png
    └── uuid-file-5.pdf
```

Each user receives an isolated folder.

---

# Authentication Flow

```text
User Login
     │
     ▼
Supabase Auth
     │
     ▼
JWT Token Issued
     │
     ▼
Authorization Header
     │
     ▼
Protected FastAPI Route
     │
     ▼
User Validation
```

---

# Row Level Security (RLS)

N-Pages uses PostgreSQL RLS to enforce ownership.

Users can:

* Read their own notes
* Create their own notes
* Update their own notes
* Delete their own notes

Users cannot access records belonging to other users.

---

# Implemented API Endpoints

## Authentication

### Login

```http
POST /login
```

---

## Notes

### Create Note

```http
POST /notes
```

### Get All Notes

```http
GET /notes
```

### Get Single Note

```http
GET /notes/{note_id}
```

### Update Note

```http
PUT /notes/{note_id}
```

### Delete Note

```http
DELETE /notes/{note_id}
```

---

## File Management

### Upload File

```http
POST /notes/{note_id}/upload
```

Features:

* Ownership verification
* UUID-based filenames
* User-specific folders
* Supabase Storage integration

---

### Get Note Files

```http
GET /notes/{note_id}/files
```

Returns all files attached to a note.

---

### Delete File

```http
DELETE /files/{file_id}
```

Removes:

1. Storage object
2. Database metadata

---

# File Upload Lifecycle

```text
User Uploads File
         │
         ▼
Validate Note Ownership
         │
         ▼
Generate UUID Filename
         │
         ▼
Upload To Storage
         │
         ▼
Generate Public URL
         │
         ▼
Store Metadata
         │
         ▼
Return Response
```

---

# File Deletion Lifecycle

```text
Delete Request
       │
       ▼
Verify Ownership
       │
       ▼
Find Storage Path
       │
       ▼
Delete Storage Object
       │
       ▼
Delete Metadata Row
       │
       ▼
Return Success
```

---

# Security Features

### Authentication

* JWT-based authentication
* Supabase Auth integration

### Authorization

* Ownership validation
* Protected routes

### Database Security

* PostgreSQL RLS
* User-level data isolation

### Storage Security

* User folder separation
* Metadata ownership verification

---

# Current Project Capabilities

### Notes

* Create notes
* Read notes
* Update notes
* Delete notes

### Files

* Upload images
* Upload PDFs
* Upload documents
* List files
* Delete files

### Security

* Multi-user support
* Data isolation
* Storage isolation

---

# Upcoming Features

## Phase 2

### Search

* PostgreSQL Full Text Search
* GIN Indexes
* Keyword Search

### Performance

* Pagination
* Sorting
* Optimized Queries

### Metadata

* Automatic updated_at triggers
* Soft Deletes

---

## Phase 3

### Organization

* Tags
* Categories
* Favorites
* Pinned Notes

### Security

* Signed URLs
* Private Storage

---

## Phase 4

### AI Features

* Embeddings
* pgvector
* Semantic Search
* AI Knowledge Retrieval

Example:

```text
Query:
"Show me notes about authentication"

Instead of:

"Find notes containing authentication"
```

---

# Development Goals

This project is being built to demonstrate:

* Backend Engineering
* Database Design
* Secure Multi-Tenant Systems
* SaaS Architecture
* API Development
* PostgreSQL Expertise
* Supabase Integration
* Search Engineering
* Future AI Integration

---

# Author

Mohit Nigote

Tech Developer | Backend Engineering | FastAPI | PostgreSQL | Supabase
