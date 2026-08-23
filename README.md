# 🏨 Smart Hostel Management System

A full-stack **Hostel Management System** built with **Django and MySQL** to simplify hostel administration, student management, room allocation, and day-to-day hostel operations.

## 📌 Overview

Smart Hostel Management System is a web-based application designed to digitize hostel management workflows. It provides an organized platform for administrators to manage students, rooms, and hostel-related information through a secure and responsive interface.

The project was developed using **Django** for backend development, **MySQL** for database management, and **HTML, CSS, and JavaScript** for the frontend.

## ✨ Features

* 🔐 **Admin Authentication**

  * Secure admin login
  * Protected administrative functionality

* 👨‍🎓 **Student Management**

  * Add and manage student records
  * Store and update student information
  * Centralized student data management

* 🏠 **Room Management**

  * Manage hostel rooms
  * Track room allocation
  * Assign rooms to students

* 📊 **Admin Dashboard**

  * Overview of hostel information
  * Centralized management interface
  * Easy access to student and room data

* 📱 **Responsive UI**

  * User-friendly interface
  * Responsive frontend for different screen sizes

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django

### Database

* MySQL

### Tools

* Git
* GitHub

## 🏗️ Project Architecture

```text
Smart Hostel Management System
│
├── Frontend
│   ├── HTML
│   ├── CSS
│   └── JavaScript
│
├── Backend
│   └── Django
│
└── Database
    └── MySQL
```

## ⚙️ How It Works

```text
User
  │
  ▼
Frontend (HTML/CSS/JavaScript)
  │
  ▼
Django Backend
  │
  ▼
MySQL Database
```

The frontend collects user input and communicates with the Django backend. Django handles application logic, authentication, and database operations, while MySQL stores student and hostel-related information.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* Django
* MySQL
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/shivanshtholia/Smart_hostel.git
```

```bash
cd Smart_hostel
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database and update the database configuration in Django's `settings.py` according to your local MySQL credentials.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smart_hostel',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin Account

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 📂 Main Modules

| Module             | Description                    |
| ------------------ | ------------------------------ |
| Authentication     | Admin login and access control |
| Student Management | Manage student records         |
| Room Management    | Manage rooms and allocations   |
| Dashboard          | Centralized hostel information |
| Database           | MySQL-based data storage       |

## 🔒 Security

The project uses Django's authentication and backend architecture to restrict administrative functionality and manage application access.

> For production deployment, environment variables should be used for sensitive credentials such as database passwords and secret keys.

## 🎯 Project Objectives

* Digitize hostel administration
* Reduce manual record management
* Simplify student and room management
* Centralize hostel information
* Provide an easy-to-use administrative interface

## 🔮 Future Improvements

* Student login and dashboard
* Online hostel fee management
* Complaint and maintenance tracking
* Leave/outpass management
* Email notifications
* Advanced hostel analytics
* Cloud deployment

## 👨‍💻 Author

**Shivansh**

B.Tech Computer Science Engineering Student

* GitHub: https://github.com/shivanshtholia
* Project: https://github.com/shivanshtholia/Smart_hostel

---

⭐ If you find this project useful, consider giving the repository a star!
