# 🌐 Ferilion Portal

**Ferilion Portal** is a web-based internal platform developed using **Python Flask**. It enables OTP-based authentication, trainee management, and role-specific dashboards for a smooth internal operation workflow.

---

## 🚀 Features

- 🔐 OTP-based user login and verification
- 👨‍🎓 Trainee dashboard to access video learning content
- 🧑‍💼 Management portal for internal operations
- 📁 Video file upload and secure access
- 📊 Role-based user experience (Trainee, Management)
- 🛠 Modular MVC-like structure using Blueprints

---

## 🏗️ Project Structure

ferilion_portal/
├── fer_app/
│ ├── init.py # App factory function
│ ├── config.py # Configurations (dev, prod, test)
│ ├── models.py # SQLAlchemy models for User, Trainee, etc.
│ ├── controllers/ # Business logic layer
│ │ ├── auth_controller.py
│ │ ├── trainee_controller.py
│ │ └── management_controller.py
│ ├── views/ # Flask route handlers (Blueprints)
│ │ ├── auth.py
│ │ ├── trainee.py
│ │ └── management.py
│ ├── templates/ # HTML files using Jinja2 templating
│ │ ├── login.html
│ │ ├── otp.html
│ │ └── dashboard.html, ...
│ ├── static/ # Static assets (CSS, JS, images)
├── videos/ # Directory to store uploaded training videos
├── run.py # App entry point
├── requirements.txt # All required Python packages
├── .gitignore # Git ignore rules
├── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/VINAYOMKAR9/Team_task.git
cd Team_task