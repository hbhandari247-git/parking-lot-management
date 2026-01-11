# Parking Lot Management System

A Django REST API–based Parking Lot Management System that handles vehicle entry, exit, slot allocation, and dynamic fee calculation using extensible pricing strategies.

---

## 🚀 Features

- Vehicle entry and exit APIs
- Automatic parking slot allocation
- Hourly parking fee calculation
- Strategy-based fee calculation (hourly, penalty, surcharge)
- Clean service-layer architecture
- RESTful API design

---

## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (for development)

---

## 🏗️ Project Architecture

```text
parking_lot/
│
├── api/                # API layer (views, serializers, URLs)
├── core/               # Business logic
│   ├── services/       # Service layer (Entry, Exit, Payment)
│   └── strategies/     # Fee calculation strategies
│
├── parking_lot/        # Django project settings
├── manage.py
└── db.sqlite3
