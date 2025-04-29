
# 📚 Online Book Store

An online bookstore web application built using **Django**, allowing users to browse books, add them to a cart, place orders, and manage profiles. It also includes admin capabilities for managing books, orders, and users.

---

## 🧰 Technologies Used

- **Backend**: Python 3, Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django DB)
- **Others**: Django Admin, Template Language, Static Files Handling

---

## 🎯 Features

### 🛍️ User Side
- User registration, login, and logout
- Profile update and order history
- Browse books by category or name
- Book detail pages with highlights
- Add/remove items from cart
- Checkout and place orders

### 🧑‍💼 Admin Side
- Django admin dashboard for managing:
  - Books
  - Orders
  - Users
  - Reviews
  - Categories

### ✨ Other Features
- Book rating and reviews
- Customer care messaging
- Fully responsive UI using Bootstrap

---

## 📁 Project Structure

```
OnlineBookStore-main/
├── accounts/               # Handles user authentication, profiles, and customer care
├── books/                  # Core bookstore logic: models, cart, orders, reviews
├── ecom_project/           # Django settings, URLs, and WSGI
├── static/                 # CSS, JS, Images
├── templates/              # HTML templates
├── db.sqlite3              # Default database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies (you can generate this)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/OnlineBookStore.git
cd OnlineBookStore-main
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, run `pip freeze > requirements.txt` after installing Django.

### 4. Change settings.py

Make changes in settings.py for Email, EmailHostPassword and SecretKey.

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Admin Panel

Access the admin panel at:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Log in using the superuser credentials you created.

---

## 📝 Notes

- Static and media files may need additional setup if deploying.
- Default database is SQLite — for production, switch to PostgreSQL or MySQL.
- For payments, integrate Razorpay, Stripe, or PayPal.
- Improve SEO and security before deploying.

---

## 🚀 Deployment

You can deploy this Django app using:

- **Heroku** (using Gunicorn and WhiteNoise)
- **PythonAnywhere**
- **AWS / GCP / Azure**
- **Docker**


-----------------------
## Author
- [R Pavani](https://www.linkedin.com/in/r-pavani/)
- [GitHub](https://github.com/pavani-1510/)

---

© 2025 R Pavani. All rights reserved.

---
