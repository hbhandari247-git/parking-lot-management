# 🚗 Parking Lot Management System (Django REST API)

A backend-focused **Parking Lot Management System** built using **Django** and **Django REST Framework**.  
This project demonstrates clean architecture, service-layer design, and extensible fee calculation using strategy patterns.

It is designed to be **interview-ready**, **production-oriented**, and easy to extend.

---

## 📌 Features

- Vehicle entry and exit management
- Parking slot allocation and release
- Ticket lifecycle handling
- Hourly-based parking fee calculation
- Extensible pricing strategy (hourly, penalty, surcharge)
- RESTful APIs using Django REST Framework
- Clean separation of concerns (API → Service → Strategy)

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (development)
- Postman (API testing)

---

## 🏗 Project Structure

parking_lot/
├── api/
│   ├── views/
│   │   ├── entry.py
│   │   └── exit.py
│   ├── serializers/
│   ├── urls.py
│   └── exception_handler.py
│
├── core/
│   ├── models/
│   │   ├── ticket.py
│   │   ├── parking_slot.py
│   │   └── vehicle.py
│   ├── services/
│   │   ├── entry_gate_service.py
│   │   ├── exit_gate_service.py
│   │   └── payment_service.py
│   └── strategies/
│       └── calculate_fees/
│           ├── hourly_fee.py
│           ├── penalty.py
│           ├── surcharge.py
│           └── custom_fee.py
│
├── parking_lot/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### Clone the Repository
git clone https://github.com/your-username/parking-lot-management.git
cd parking-lot-management

### Create Virtual Environment
python -m venv venv
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Run Migrations
python manage.py migrate

### Start Server
python manage.py runserver

---

## 📡 API Endpoints

### Vehicle Entry
POST /api/entry/

Request:
{
  "vehicle_number": "DL01PM1234",
  "vehicle_type": "CAR"
}

### Vehicle Exit
POST /api/exit/

Request:
{
  "ticket_id": 1
}

---

## 🧠 Design Highlights

- Service layer architecture
- Strategy pattern for pricing
- Clean separation of concerns
- Extensible and testable codebase

---

## 👨‍💻 Author

Himanshu Bhandari  
Backend Developer | Python | Django

---

## 📄 License

MIT License
