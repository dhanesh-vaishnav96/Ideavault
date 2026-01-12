# 📝 IdeaVault — IdeasNotes Management System

IdeaVault is a full-stack web application built with **FastAPI, MongoDB, and Jinja2** that allows users to create, search, edit, and manage notes in a clean and responsive interface.

This project demonstrates a **real backend with database integration**, making it far more powerful than browser-only note apps.

---

## 🌐 Live Demo
🚀 Deployed on Render  
👉 https://ideavault-twtm.onrender.com

---

## ✨ Features

- 🧠 Create, read, update, and delete notes  
- 🔍 Search notes by title  
- ✏️ Edit saved notes  
- 🗑️ Soft delete (safe deletion)  
- 💾 MongoDB database storage  
- 📄 Server-side rendering with Jinja2  
- 🎨 Clean and responsive UI  
- ⚡ FastAPI backend  

---

## 🛠 Tech Stack

**Frontend**
- HTML  
- CSS  
- Jinja2 Templates  

**Backend**
- FastAPI  
- Python  

**Database**
- MongoDB Atlas  

**Deployment**
- Render  

---


## 📂 Project Structure
```text
project/
│── main.py
│── config/
│── models/
│── schema/
│── templates/
│── static/
│── requirements.txt

---

## ⚙️ How It Works

1. User submits a note from the browser  
2. FastAPI processes the request  
3. Data is stored in MongoDB  
4. Notes are fetched and rendered via Jinja2  
5. User can search, edit, or delete notes  

All data is stored permanently in the database.

---

## 🔐 Security

- Database credentials are stored in environment variables  
- No sensitive data is exposed in the code  
- MongoDB Atlas ensures secure and scalable storage  

---




