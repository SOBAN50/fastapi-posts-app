# 📝 fastapi-posts-app

A production-ready REST API built with [FastAPI](https://fastapi.tiangolo.com/) for managing posts with full CRUD operations.  
This project demonstrates how to structure a modern Python backend using clean architecture principles, modular design, and type safety.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Status](https://img.shields.io/badge/status-Active-success)

---

## 📖 Project Overview

`fastapi-posts-app` is a lightweight and extensible API for creating and managing posts — similar to a minimal blogging or microblogging backend.  
It’s built on top of **FastAPI**, which makes it:
- ⚡ **Fast** — uses Python’s async capabilities.
- 🧹 **Clean** — easy-to-maintain modular structure.
- 🛡 **Reliable** — data validation with Pydantic.
- 🚀 **Production-ready** — easy to deploy using Uvicorn & Docker.

Typical use cases include:
- A backend API for a blogging platform.
- A learning template for FastAPI beginners.
- A starting point for more complex microservices.

---

## 🧰 Tech Stack & Why

| Technology                | Purpose                                      | Why It’s Used                                              |
|----------------------------|----------------------------------------------|------------------------------------------------------------|
| Python 3.10+               | Programming language                        | Modern syntax, async support                               |
| FastAPI                    | Web framework                               | Fast, type-hinted, auto-docs                               |
| Uvicorn                    | ASGI server                                 | Lightweight and fast server for async apps                 |
| Pydantic                   | Data validation                             | Ensures clean, strict input models                         |
| SQLite / PostgreSQL        | Database                                    | Simple local dev or production DB                          |
| Pytest                     | Testing                                     | Clean, fast testing framework                              |
| Docker (optional)          | Containerization                            | Simplifies deployment                                      |

---

## 🏗 Architecture & Folder Structure

```
fastapi-posts-app/
│
├── main.py                # App entry point
├── models/                # ORM models / database structure
├── routers/               # Route definitions for CRUD operations
├── schemas/               # Pydantic schemas for data validation
├── database.py            # DB connection and session management
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

### 🧭 Flow
1. **Request** hits a route in `routers/`.
2. Request data is validated with Pydantic `schemas`.
3. Database interaction happens through `models` and `database.py`.
4. Response is returned as a Pydantic model.
5. Interactive API docs are automatically generated at `/docs`.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SOBAN50/fastapi-posts-app.git
cd fastapi-posts-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file at the root if using a database like PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost:5432/fastapi_posts
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> 💡 For development, SQLite can be used without extra setup.

---

## 🧭 Running the Server

```bash
uvicorn main:app --reload
```

The server runs by default at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)  

API Docs:  
- Swagger UI 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Example API Endpoints

| Method | Endpoint         | Description              |
|--------|-------------------|---------------------------|
| GET    | `/posts`         | Get all posts            |
| GET    | `/posts/{id}`    | Get a specific post      |
| POST   | `/posts`         | Create a new post        |
| PUT    | `/posts/{id}`    | Update an existing post  |
| DELETE | `/posts/{id}`    | Delete a post            |

Sample `POST /posts` request body:
```json
{
  "title": "My First Post",
  "content": "This is an example post.",
  "published": true
}
```

---

## 🧪 Running Tests

This project supports automated tests with [pytest](https://docs.pytest.org/).

```bash
pytest
```

> Tests cover endpoint behavior, validation, and database interactions.

---

## 🐳 Docker Support

### Build and Run with Docker
```bash
docker build -t fastapi-posts-app .
docker run -d -p 8000:8000 fastapi-posts-app
```

### Environment Variables with Docker
Create a `.env` file and use `--env-file .env` with `docker run`.

---

## 🚀 Deployment

### Production Server Example with Uvicorn + Gunicorn
```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

For cloud deployment:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://www.heroku.com/)
- [Docker Hub](https://hub.docker.com/)

---

## 🛣 Roadmap / Future Improvements

- 🔐 Add authentication with JWT / OAuth2  
- 🧑‍🤝‍🧑 Add user accounts and roles  
- 📊 Add pagination & filtering  
- 🧠 Add caching layer (e.g., Redis)  
- 📬 Add background tasks  
- ☁️ CI/CD setup for auto-deployment

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make changes and commit (`git commit -m 'Add feature'`)  
4. Push the branch (`git push origin feature-name`)  
5. Open a Pull Request

### Code Style Guidelines
- Use [Black](https://black.readthedocs.io/en/stable/) for formatting.
- Use type hints and docstrings.
- Write tests for new features.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) for the framework  
- [Uvicorn](https://www.uvicorn.org/) for the server  
- [Pydantic](https://docs.pydantic.dev/) for data validation  
- Inspired by real-world backend structures and best practices.

---

⭐ **If you like this project, consider giving it a star on GitHub!**
