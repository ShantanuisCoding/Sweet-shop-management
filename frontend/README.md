# Sweet Shop Management System – Frontend

This directory contains the **frontend application** for the Sweet Shop Management System. The frontend is built as a modern **Single Page Application (SPA)** using **React + Vite** and is responsible for interacting with the backend APIs, handling authentication, and providing a clean user interface for managing sweets and inventory.

The frontend focuses on clarity, responsiveness, and correct integration with the backend rather than heavy UI complexity.

---

## 🎯 Objectives

The frontend aims to:

* Provide an intuitive UI for users to interact with backend APIs
* Support authentication and protected routes
* Display sweets and inventory information clearly
* Enable purchase and admin-only restock actions
* Follow a clean and maintainable folder structure

---

## 🚀 Tech Stack

* React (Vite)
* JavaScript (ES6+)
* Axios (API communication)
* HTML5 & CSS3

---

## 🧠 Core Features

### 🔐 Authentication

* User registration and login
* JWT token handling
* Protected routes using role-based access

### 🍬 Sweet Dashboard

* Display all available sweets
* Show name, category, price, and quantity
* Disable purchase button when stock is zero

### 📦 Inventory Actions

* Purchase sweets (authenticated users)
* Restock sweets (ADMIN users only)

---

## 📂 Project Structure

```
frontend/
├── public/
├── src/
│   ├── api/        # Axios instances and API calls
│   ├── assets/     # Static assets
│   ├── auth/       # Authentication logic and helpers
│   ├── pages/      # Page-level components
│   ├── routes/     # Route definitions and guards
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Navigate to Frontend Directory

```bash
cd frontend
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Start Development Server

```bash
npm run dev
```

The frontend will be available at:

```
http://localhost:5173
```

---

## 🔗 Backend Integration

The frontend communicates with the backend via REST APIs.

Ensure the backend is running at:

```
http://127.0.0.1:8000
```

The API base URL is configured inside the `src/api` layer.

---

## 🔐 Authorization Handling

* JWT tokens are stored in browser storage
* Tokens are attached to requests using Axios interceptors
* UI elements are conditionally rendered based on user role

---

## 🧪 Testing

Frontend testing is not implemented in this version and can be added as a future enhancement.

---

## 📌 Notes

* Business rules are strictly enforced by the backend
* Frontend focuses on usability and correct API interaction
* Any local database files (e.g. `test.db`) should not be committed

---

## ✨ Future Enhancements

* Improved UI styling
* Search and filter functionality
* Frontend testing
* Deployment configuration
