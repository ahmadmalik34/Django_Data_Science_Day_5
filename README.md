# 🔐 User Authentication System

<div align="center">

**Complete Auth System with Blog CRUD**

[![Django](https://img.shields.io/badge/Django-5.0%2B-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=flat-square&logo=sqlite)](https://www.sqlite.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-quick-start)

</div>

---

## 🎯 Overview

Build a complete user authentication system with registration, login, logout, profiles, and user-specific blog post creation/editing.

**Production-grade authentication powered by Django's built-in auth system.**

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 👤 **User Registration** | Sign up with email validation |
| 🔓 **Login/Logout** | Session-based authentication |
| 📝 **User Profile** | View user bio and posts |
| ✍️ **Create Posts** | Authenticated users can write blogs |
| ✏️ **Edit Posts** | Users can edit their own posts |
| 🗑️ **Delete Posts** | Users can delete their posts |
| 🔒 **Protected Routes** | @login_required on sensitive views |
| 🎨 **Dark Theme** | Synthwave Sunset theme |

---

## 📦 Tech Stack

- **Framework:** Django 5.0+
- **Database:** SQLite3
- **Auth:** Django's built-in authentication system
- **Frontend:** HTML5 + CSS3 (Dark theme)
- **Language:** Python 3.8+

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install django python-decouple

# Apply migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### Run Locally

```bash
python manage.py runserver
```

Access:
- **Blog:** `http://127.0.0.1:8000/`
- **Register:** `http://127.0.0.1:8000/accounts/register/`
- **Login:** `http://127.0.0.1:8000/accounts/login/`
- **Admin:** `http://127.0.0.1:8000/admin/`

---

## 🔑 Key Features

### User Registration

```python
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
```

### Protected Routes

```python
@login_required(login_url='login')
def create_post(request):
    # Only authenticated users can create posts
    ...
```

### User-Specific Content

```python
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    # Ensure user owns the post
    if post.author.user != request.user:
        return HttpResponseForbidden()
    ...
```

---

## 📄 Views & Forms

### Views
- `register` — User signup
- `login_view` — User login
- `logout_view` — User logout
- `profile` — User profile page
- `create_post` — New post creation
- `edit_post` — Modify existing post
- `delete_post` — Remove post

### Forms
- `RegisterForm` — Custom user creation with email
- `PostForm` — ModelForm for blog posts

---

## 🎨 UI Features

### Dark Theme (Synthwave Sunset)
- Deep indigo background (#1a1a2e)
- Dark slate surfaces (#2a2a4e)
- Vibrant magenta accents (#ff00ff)
- Bright cyan accents (#00ffff)

### Responsive Design
- Mobile-first approach
- Works on all device sizes
- Glassmorphism effects

---

## 📂 Project Structure

```
Day_05_User_Auth/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   ├── register.html
│   │   ├── login.html
│   │   └── profile.html
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── create_post.html
│   │   ├── edit_post.html
│   │   └── delete_post.html
└── static/
    └── css/
        └── style.css
```

---

## 🔐 Security Features

✅ **Password Hashing** — Django's PBKDF2 algorithm  
✅ **CSRF Protection** — {% csrf_token %} on all forms  
✅ **Session Security** — HTTP-only cookies  
✅ **Permission Checks** — Users can only modify their own posts  
✅ **Login Requirements** — @login_required decorators  

---

## 📖 What You'll Learn

✅ Django's built-in authentication system  
✅ Custom user registration forms  
✅ Session-based login/logout  
✅ @login_required decorator  
✅ Form validation and error handling  
✅ CSRF protection  
✅ User permissions and ownership checks  
✅ ModelForm for database operations  
✅ Dynamic templates based on authentication  

---

## 🔄 Next Steps

- **Day 6:** NumPy for data science
- **Day 7:** Pandas exploratory data analysis

---

<div align="center">

**Day 5 of 50 — Django × Data Science Challenge**

Complete user authentication and blog CRUD system.

</div>

