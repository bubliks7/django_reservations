# 🚗 Django Reservations

A simple car reservation system built with Django. The application allows users to browse vehicles, rent them for selected dates, and manage their reservations.

---

## 📌 Features

### 👤 Users
* registration and login (Django forms – `forms.py`)
* simple user profile
* access to personal reservations

---

### 🚘 Cars
* list of all available cars
* detailed car pages
* ability to add reviews
* view reviews from other users

---

### 📅 Reservations
* rent cars for selected date ranges
* prevention of booking already reserved cars
* reservation statuses (e.g. pending, approved, canceled)
* ability to cancel reservations (depending on status)

---

### 📊 Views and Organization
* page with all cars
* user panel with reservations:
  * upcoming
  * canceled (displayed at the bottom)
* reservations sorted by activity/status

---

### 🛠️ Admin Panel
* built-in Django admin panel with improved UI
* management of:
  * cars
  * reservations
  * reviews
  * users

---

## 🛠️ Technologies

* Python
* Django
* PostgreSQL
* HTML / CSS
* media files stored in `media/` directory

---

## ⚙️ Installation and Setup

### 1. Clone the repository
git clone <link-to-repo>
cd django_rezerwations

### 2. Create virtual environment
python -m venv venv

source venv/bin/activate  # Linux / Mac  
venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure database
Set up PostgreSQL in `settings.py`

### 5. Apply migrations
python manage.py migrate

### 6. Run the server
python manage.py runserver

### 7. Open in browser
http://127.0.0.1:8000/

---

## 👤 Admin Panel

### Create superuser
python manage.py createsuperuser

### Login
http://127.0.0.1:8000/admin/

---

## 📂 Project Structure

* `models.py` – models (cars, reservations, reviews, users)
* `views.py` – application logic
* `forms.py` – forms
* `templates/` – HTML templates
* `static/` – CSS / JS
* `media/` – images (e.g. cars)

---

## 📄 Project Status

* project completed
* all core functionalities are working properly

---

## 💡 Possible Improvements

* online payments
* email notifications
* API (Django REST Framework)
* extended user profile

---

## 🤝 Author

Project created for educational purposes.
