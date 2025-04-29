# Pricing Module Assignment

## Overview

This project is a configurable pricing module built using Django.
It calculates the final ride price based on:
- Distance traveled
- Ride duration
- Waiting time
- Day of the week

Similar to billing systems like Uber/Ola.

## Features

- Add/Edit pricing configurations through Django Admin.
- Enable/Disable specific pricing configs.
- Auto-log all configuration changes with actor and timestamp.
- API to calculate ride price dynamically based on user input.

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/pricing_module_assignment.git
cd pricing_module_assignment

### 2. Create and Activate Virtual Environment
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Apply Migrations
python manage.py migrate

### 5. Create Superuser (for admin panel access)
python manage.py createsuperuser

### 6. Run the Development Server
python manage.py runserver

## Admin Panel Usage

- Open http://127.0.0.1:8000/admin
- Login with your superuser credentials.
- Manage Pricing Configs:
    - Add new pricing configurations.
    - Edit existing configurations.
    - Enable/Disable pricing as needed.
- Pricing Config Logs:
    - Every create/update automatically creates a log entry with action and timestamp.

## API Usage

### Endpoint
POST http://127.0.0.1:8000/api/calculate-price/

### Request Body (JSON)
{
  "distance": 10,
  "time_hours": 1.5,
  "waiting_minutes": 5,
  "day_of_week": "Monday"
}

### Response (JSON)
{
  "distance_price": 170.0,
  "time_price": 1.5,
  "waiting_charge": 5.0,
  "total_price": 176.5
}

## Technologies Used

- Python 3
- Django 5
- SQLite3 (default database)

## Notes

- The API accepts only POST method.
- Pricing Config is selected dynamically based on the provided day_of_week.
- Logs are created automatically when a Pricing Config is created or updated.

## License

This project is for educational and assignment evaluation purposes only.
