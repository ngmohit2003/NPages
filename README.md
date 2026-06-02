![Python](https://img.shields.io/badge/Python-3.11-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

![Supabase](https://img.shields.io/badge/Supabase-Auth%20%2B%20Storage-success)

![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

![License](https://img.shields.io/badge/License-MIT-purple)



# 🚀 N-Pages — Smart Multi-User Research Notes Platform

> A backend-first knowledge management system for researchers, students, engineers, and technical professionals.

N-Pages combines secure note management, mathematical computation, full-text search, and document storage into a scalable architecture built with FastAPI, PostgreSQL, and Supabase.

---

## 🎯 Vision

Most note-taking applications focus on UI.

N-Pages focuses on:

* Knowledge storage
* Mathematical reasoning
* Searchability
* Security
* Scalability

The goal is to build a production-style SaaS backend demonstrating modern backend engineering practices.

---

# Current Development Status

| Module               | Status         |
| -------------------- | -------------- |
| FastAPI Backend      | ✅ Working      |
| Supabase Integration | ✅ Working      |
| Authentication       | ✅ Working      |
| JWT Sessions         | ✅ Working      |
| User Notes CRUD      | 🟡 In Progress |
| RLS Security         | 🟡 Testing     |
| Full Text Search     | ⏳ Planned      |
| Storage Buckets      | ⏳ Planned      |
| Markdown Rendering   | ⏳ Planned      |
| LaTeX Rendering      | ⏳ Planned      |
| Auto Tagging         | ⏳ Planned      |
| Edge Functions       | ⏳ Planned      |
| Math Engine          | ⏳ Planned      |

---

# System Architecture

```text
                    ┌───────────────┐
                    │    Client     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    └───────┬───────┘
                            │
      ┌─────────────────────┼─────────────────────┐
      ▼                     ▼                     ▼

┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Supabase Auth│   │ PostgreSQL   │   │   Storage    │
│ + JWT        │   │ + RLS        │   │ + Buckets    │
└──────────────┘   └──────────────┘   └──────────────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │ Full Text Search│
                  │ Triggers/Views  │
                  └─────────────────┘
```

---

# Core Features

## Authentication

* User Registration
* Login
* JWT Session Management
* Supabase Auth

---

## Secure Multi-Tenant Notes

Every note belongs to exactly one user.

```sql
auth.uid() = user_id
```

Implemented using PostgreSQL Row Level Security (RLS).

---

## Research Notes

Each note supports:

* Markdown
* LaTeX
* References
* Images
* PDFs

Example:

```markdown
# Bayesian Inference

Bayes theorem:

P(A|B)=P(B|A)P(A)/P(B)
```

---

## Full Text Search

Powered by PostgreSQL:

* tsvector
* tsquery
* GIN Indexes

Example:

```sql
SELECT *
FROM notes
WHERE content_tsv @@ plainto_tsquery('postgres');
```

---

## Storage

Supabase Storage Buckets:

```text
note-assets/
 ├── user-id/
 │   ├── note-id/
 │   │   ├── image.png
 │   │   ├── paper.pdf
```

---

## Mathematical Workspace

Planned capabilities:

* Expression Evaluation
* Equation Solving
* Simplification
* Derivatives
* Integrals

Powered by SymPy.

Example:

```python
simplify("(x+1)^2")
```

Result:

```python
x**2 + 2*x + 1
```

---

# Database Design

## Notes

```text
notes
│
├── id
├── user_id
├── title
├── content
├── content_tsv
├── created_at
└── updated_at
```

---

## Attachments

```text
note_assets
│
├── id
├── note_id
├── file_path
└── file_type
```

---

## Tags

```text
note_tags
│
├── id
├── note_id
└── tag
```

---

# Planned PostgreSQL Features

## Triggers

Automatic search-vector updates.

## Views

* Recent Notes
* Most Referenced Notes

## Functions

Automatic note tagging.

## Indexes

GIN indexes for search performance.

---

# Project Structure

```text
N-Pages/

├── app/
│
├── routes/
│   ├── auth.py
│   ├── notes.py
│
├── models/
│   ├── schemas.py
│
├── db/
│   ├── supabase_client.py
│
├── services/
│
├── utils/
│
├── tests/
│
└── main.py


v2: 
N-Pages/
│
├── app/
│   ├── db/
│   │   └── supabase_client.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── notes.py
│   │
│   ├── services/
│   │   └── auth_service.py
│   │
│   ├── utils/
│   │
│   └── __init__.py
│
├── docs/
│   ├── architecture/
│   └── development-journal.md
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

# Tech Stack

## Backend

* FastAPI
* Python

## Database

* PostgreSQL
* Supabase

## Authentication

* Supabase Auth
* JWT

## Search

* PostgreSQL Full Text Search

## Storage

* Supabase Storage

## Mathematics

* SymPy

## Future Frontend

* React
* Next.js

---

# Engineering Goals

This project is intentionally designed to demonstrate:

* API Design
* Authentication
* Authorization
* Database Design
* Search Systems
* Storage Systems
* PostgreSQL Internals
* Event Driven Patterns
* Scalable Architecture

---

# Development Log

## Phase 1

* [x] FastAPI Setup
* [x] Supabase Integration
* [x] Signup
* [x] Login
* [x] JWT Authentication

## Phase 2

* [ ] Complete Notes CRUD
* [ ] Verify RLS
* [ ] Storage Integration

## Phase 3

* [ ] Full Text Search
* [ ] Triggers
* [ ] Views
* [ ] Functions

## Phase 4

* [ ] Math Engine
* [ ] Auto Tagging
* [ ] Edge Functions

---

# Why This Project Exists

Most portfolio projects stop at CRUD.

N-Pages explores what happens after CRUD:

* Secure multi-user systems
* Search infrastructure
* PostgreSQL automation
* Knowledge management
* Mathematical computation
* Scalable backend architecture

Built in public. Iterated continuously.
