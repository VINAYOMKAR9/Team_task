# 🌐 Ferilion Portal

**Ferilion Portal** is a web-based internal platform Developed using **Python Flask**. It enables OTP-based authentication, trainee management, and role-specific dashboards for a smooth internal operation workflow.

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
│ ├── config.py # Configurations (Dev, prod, test)
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


### 1. Git Workflow Guide

## 📂 Branch Strategy

- `main` → stays empty or protected (no code pushed here)
- `Dev` → central integration branch
- `features/<name>` → individual Developer branches


## 👨‍💻 Developer Workflow

### 🔹 Step 1: Work on Your Feature Branch

git checkout features/Astick
# ... make your code changes ...

### 🔹 Step 2: Stage and Commit Your Changes

git add .
git commit -m "Completed: Video upload functionality"
git push origin features/Vinay ( Please use your branch name for push your code ) 


### 🔹 Step 3: Switch to `Dev` and Pull the Latest Code

git checkout Dev
git pull origin Dev

### 🔹 Step 4: Merge Your Feature Branch into `Dev`

git merge features/Vinay ( Please use your branch name for merge your code ) 


### ⚠️ If Merge Conflicts Occur

# Resolve conflicts manually, then:
git add .
git commit -m "Resolved conflicts while merging features/Astick into Dev"

### 🔹 Step 5: Push the Updated `Dev` Branch to GitHub

git push origin Dev

✅ Your changes are now available to the whole team in the `Dev` branch.

## ✅ Best Practices

- Always pull the latest `Dev` before merging
- Test thoroughly before pushing
- Communicate with your team on major changes
