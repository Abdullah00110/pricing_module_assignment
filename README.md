# Pricing Module Assignment

## Overview

This project is a **configurable pricing module** built using Django.  
It calculates the final ride price based on:
- Distance traveled
- Ride duration
- Waiting time
- Day of the week

Similar to billing systems like Uber/Ola.

---

## Features

- Add/Edit pricing configurations through Django Admin.
- Enable/Disable specific pricing configs.
- Auto-log all configuration changes with actor and timestamp.
- API to calculate ride price dynamically based on user input.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pricing_module_assignment.git
cd pricing_module_assignment

2. Create and Activate Virtual Environment
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create Superuser (for admin panel access)
python manage.py createsuperuser

6. Run the Development Server
python manage.py runserver
