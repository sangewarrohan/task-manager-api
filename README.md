# 🚀 Task Manager API

A production-ready backend REST API built with **FastAPI** and **PostgreSQL**. This project is being developed as part of my backend engineering learning journey, following industry-standard architecture and best practices.

---

## 📖 About the Project

Task Manager API is designed to help users organize and manage their daily tasks efficiently.

The project focuses on building a scalable backend by implementing RESTful APIs, database relationships, authentication, validation, pagination, filtering, and other production-level backend concepts.

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python 3.14
- Uvicorn

### Database
- PostgreSQL

### ORM
- SQLAlchemy 2.0

### Database Migration
- Alembic

### Validation
- Pydantic

### Development Tools
- VS Code
- Postman
- Git
- GitHub

---

## 📂 Project Structure

```text
task-manager-api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   ├── main.py
│   └── __init__.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ✨ Planned Features

- User Management
- Task Management
- Category Management
- CRUD Operations
- Request Validation
- Error Handling
- Pagination
- Filtering
- Sorting
- JWT Authentication
- Password Hashing
- Database Migrations
- API Documentation (Swagger)
- Docker Support
- Unit Testing
- CI/CD Pipeline

---

## 📡 API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/sangewarrohan/task-manager-api.git
```

### Navigate to the project

```bash
cd task-manager-api
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📈 Development Roadmap

- [x] Project Setup
- [x] FastAPI Configuration
- [x] Git & GitHub Setup
- [ ] PostgreSQL Connection
- [ ] SQLAlchemy Models
- [ ] CRUD APIs
- [ ] Authentication
- [ ] Pagination & Filtering
- [ ] Docker
- [ ] Testing
- [ ] Deployment

---

## 🎯 Learning Goals

This project is being developed to strengthen my backend engineering skills by learning:

- REST API Design
- Database Design
- SQLAlchemy ORM
- PostgreSQL
- Authentication & Authorization
- Clean Architecture
- Dependency Injection
- Docker
- Production Deployment
- Backend Best Practices

---

## 👨‍💻 Author

**Rohan Sangewar**

GitHub: https://github.com/sangewarrohan