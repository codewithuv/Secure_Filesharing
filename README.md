# 🔐 Secure File Sharing System (Python/Django)

A secure REST API-based file-sharing platform built using **Django** and **Django REST Framework**, supporting two types of users — **Operation Users** and **Client Users** — with secure file upload, encrypted download URLs, and email verification.

---

## 🚀 Features

### 👨‍💼 Operation User
- Login (JWT Authentication)
- Upload files (`.pptx`, `.docx`, `.xlsx` only)

### 👤 Client User
- Sign Up (returns encrypted email verification link)
- Email Verification
- Login
- List all uploaded files
- Download files via encrypted, one-time secure URLs

### 🔐 Security
- JWT-based authentication
- Role-based access control (`ops` and `client`)
- Encrypted tokens for download links using `itsdangerous`
- Email verification for client sign-up

---

## 🛠️ Tech Stack

| Layer              | Technology                  |
|-------------------|-----------------------------|
| Backend            | Django + Django REST Framework |
| Auth               | JWT (`djangorestframework-simplejwt`) |
| Email              | Django Email Backend (SMTP) |
| Database           | SQLite / PostgreSQL         |
| File Storage       | Django File System          |
| Secure Tokens      | `itsdangerous` (for email/download links) |

---

## 📁 Project Structure

SecureFileShare/
├── api/
│ ├── models.py # Custom User and File models
│ ├── views.py # API endpoints
│ ├── serializers.py # Request/Response validation
│ ├── permissions.py # Role-based access control
│ └── urls.py # App-specific routes
├── SecureFileShare/
│ ├── settings.py # Django settings and configurations
├── media/ # Uploaded file storage
├── manage.py
└── requirements.txt




