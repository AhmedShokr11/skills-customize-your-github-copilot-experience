```markdown
# 📘 Assignment: Building REST APIs with FastAPI

**Due Date:** 2025-12-23
**Path:** assignments/building-rest-apis-fastapi

## 🎯 Objective

Build a RESTful API using the FastAPI framework to practice designing endpoints, request/response validation, and basic CRUD operations.

## 🎯 Learning Outcomes

- Design REST endpoints that follow clear semantics
- Use Pydantic models for request validation and response typing
- Implement CRUD operations with in-memory state
- Run and test a FastAPI application locally with `uvicorn`

## 📝 Tasks

### 🛠️ Task 1 — Core API

#### Description
Create a small REST API that manages a collection of items (create, read, update, delete). Use FastAPI and Pydantic models for request validation.

#### Requirements

- Implement endpoints for: list items (`GET /items`), get item (`GET /items/{id}`), create item (`POST /items`), update item (`PUT /items/{id}`), delete item (`DELETE /items/{id}`)
- Use Pydantic models for request bodies and responses
- Return appropriate HTTP status codes (201 on create, 404 when item not found, etc.)
- Keep state in-memory (a Python dict) so the app runs without a database

### 🛠️ Task 2 — Optional Extensions (extra credit)

#### Description
Improve the API with one or more of the following enhancements.

#### Examples (pick any)

- Add query parameters for filtering and pagination
- Persist data to a simple JSON file or SQLite DB using `sqlmodel` or `sqlite3`
- Add simple token-based authentication for protected endpoints
- Add OpenAPI examples and response models for better docs

## 🧰 Starter files

- `main.py` — minimal FastAPI app (provided as starter code)

To run the starter app locally:

```bash
pip install fastapi uvicorn
uvicorn main:app --reload --port 8000
```

Open the interactive API docs at: http://localhost:8000/docs

## ✅ Submission

Place your final `.py` file(s) in the `assignments/building-rest-apis-fastapi/` folder. Include a short README describing any extra features you added and how to run the app.

## Help & Hints

- Use `from pydantic import BaseModel` to define request/response schemas
- Keep the core API logic in functions for easier testing
- Validate input and return clear error messages with proper status codes

```
