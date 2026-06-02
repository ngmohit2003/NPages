# System Overview

## Current Architecture

Client
  ↓
FastAPI
  ↓
Supabase
  ├── Auth
  ├── PostgreSQL
  └── Storage

## Future Architecture

Client
  ↓
API Gateway
  ↓
Notes Service
Search Service
Math Service
Storage Service