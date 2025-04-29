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
