# FastAPI App Backend

This repository contains the backend of a web application built using **FastAPI**, a modern and high-performance web framework for building APIs with Python.

## 🚀 Features

- ⚡ **FastAPI**: High-performance and easy-to-use API development.
- 🔄 **Asynchronous Support**: Efficient async/await-based operations.
- 🧱 **Modular Project Structure**: Cleanly organized files (routes, models, schemas, config).
- 🗃️ **SQLAlchemy ORM**: Integrates with relational databases.
- 🔄 **Alembic Migrations**: Handles database schema changes and versioning.
- 📄 **Auto-generated Docs**: Swagger UI and ReDoc out of the box.
- 🔒 **Authentication/Authorization**: JWT, OAuth2, or other security features.

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/saumyashah0510/fastAPI-app-backend.git
cd fastAPI-app-backend
```
### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Set up the Database

Create a .env file or update settings in core/config.py to point to your database URL.

### 5. Start the application

```bash
fastapi dev app/main.py
```

## 🧪 API Documentation

Once the server is running, you can access the interactive documentation:

- 📘 **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📕 **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

