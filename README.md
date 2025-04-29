# Pricing Module Assignment

## 📌 Overview

This project is a configurable pricing module built using Django.

It calculates ride fare dynamically based on:
- ✅ Distance traveled
- ✅ Ride duration (in hours)
- ✅ Waiting time (in minutes)
- ✅ Day of the week

It mimics billing systems like Uber/Ola for evaluation purposes.

---

## ✅ Key Features

- 🔧 Manage pricing configurations via Django Admin
- 📅 Enable/Disable configs based on the day of the week
- 🧠 Time multipliers stored as a single JSON field
- 📝 Auto-log every config creation or update with timestamp + actor
- 📡 Expose a clean, documented API to calculate price

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pricing_module_assignment.git
cd pricing_module_assignment
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Panel Login)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🔐 Admin Panel Usage

- Visit: `http://127.0.0.1:8000/admin`
- Use superuser credentials to login.
- Manage:
  - **Pricing Configs** → Add/Edit JSON-based pricing rules
  - **Pricing Config Logs** → View logs of all config changes

### 🧾 Sample JSON for `time_multipliers` field:
```json
{
  "upto_1hr": 1.0,
  "1_to_2hr": 1.25,
  "2_to_3hr": 2.2
}
```

---

## 📡 API Usage

### ▶️ Endpoint

```http
POST http://127.0.0.1:8000/api/calculate-price/
```

### 🔻 Request Body (JSON)

```json
{
  "distance": 10,
  "time_hours": 1.5,
  "waiting_minutes": 5,
  "day_of_week": "Monday"
}
```

### 🔺 Response Body (JSON)

```json
{
  "distance_price": 170.0,
  "time_price": 1.5,
  "waiting_charge": 5.0,
  "total_price": 176.5
}
```

---

## 🛠 Technologies Used

- Python 3.10+
- Django 5.x
- SQLite (for local DB)
- Postman (for API testing)

---

## 📝 Notes

- `time_multipliers` is stored as a JSONField to allow flexibility.
- Only one config per `day_of_week` is marked active.
- All config changes are logged using Django signals with timestamp and action.

---

## 📄 License

This project is for educational and assignment evaluation purposes only.
