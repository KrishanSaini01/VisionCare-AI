# 🩺 VisionCare AI – Intelligent Medical Image Analysis Platform

> **An AI-powered healthcare platform that combines Deep Learning and Generative AI to analyze medical images, explain predictions, and generate intelligent medical reports.**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-orange)
![Gemini](https://img.shields.io/badge/Generative%20AI-Gemini-blueviolet)
![MYSQL](https://img.shields.io/badge/MYSQL-Database-blue)
![HTML](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-green)

---

# 📌 Overview

VisionCare AI is a next-generation **Medical Image Analysis Platform** developed as a **Final Year Computer Science Engineering Project**.

The platform combines **Deep Learning (CNN)**, **Generative AI**, and a **Relational Database** to assist users in analyzing medical images and understanding AI predictions.

Users can upload medical images (such as Chest X-rays, Brain MRI, CT Scans, or Skin Lesion images), and the CNN model predicts the possible disease. After prediction, Generative AI explains the results in easy-to-understand language, generates medical summaries, answers follow-up questions, and creates downloadable PDF reports.

The system securely stores users, uploaded images, prediction history, reports, and conversations in a relational database.

> **Disclaimer:** This project is intended for educational and research purposes only. It is **not** a substitute for professional medical diagnosis or treatment.

---

# 🎯 Objectives

- Detect diseases using a Convolutional Neural Network (CNN).
- Provide AI-powered explanations using Generative AI.
- Generate downloadable medical reports.
- Maintain prediction history.
- Create an intelligent healthcare assistant.
- Demonstrate the integration of Deep Learning, Generative AI, and Database technologies.

---

# 🚀 Key Features

## 👤 User Management

- User Registration
- Login Authentication
- Password Encryption
- User Profile

---

## 🩻 Medical Image Upload

Supports medical images such as:

- Chest X-rays

- Brain MRI Images

---

## 🧠 Deep Learning Module

Uses a CNN model for:

- Image Classification
- Disease Prediction
- Confidence Score Calculation
- Feature Extraction

---

## 🤖 Generative AI Module

Powered by Gemini API.

Capabilities:

- Explain prediction results
- Simplify medical terminology
- Answer user questions
- Generate medical summaries
- Provide general precautions
- Generate PDF medical reports

---

## 📊 Dashboard

Displays

- Uploaded Images
- Prediction History
- Confidence Scores
- AI Reports
- Chat History

---

## 💬 AI Medical Assistant

Users can ask questions like:

- What is Pneumonia?
- Explain my MRI result.
- What precautions should I take?
- What causes this disease?
- How is it generally treated?

---

## 📄 PDF Report Generation

Automatically generates reports containing

- Patient Information
- Uploaded Image
- Prediction
- Confidence Score
- AI Explanation
- General Precautions
- Report Timestamp

---

## 🗄 Database Management

Stores

- Users
- Uploaded Images
- Predictions
- Reports
- Chat History

---

# 🏗 System Architecture

```
                    User
                      │
                      ▼
            HTML + CSS + JavaScript
                      │
                      ▼
                Flask Backend
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 CNN Deep Learning   MYSQL     Gemini API
      │               │                │
      └───────────────┼────────────────┘
                      ▼
              PDF Report Generator
```

---

# 🔄 Workflow

```
User Login
      │
Upload Medical Image
      │
Image Preprocessing
      │
CNN Model Prediction
      │
Confidence Score
      │
Store Prediction in Database
      │
Send Result to Gemini
      │
Generate Explanation
      │
AI Chat Support
      │
Generate PDF Report
      │
Save Report
```

---

# 🧠 Deep Learning

## Model

Convolutional Neural Network (CNN)

Responsibilities

- Image preprocessing
- Feature extraction
- Disease classification
- Confidence prediction

Libraries

- TensorFlow
- Keras
- OpenCV
- NumPy

---

# 🤖 Generative AI

Uses

- Google Gemini API

Functions

- Explain disease prediction
- Answer medical questions
- Generate summaries
- Produce readable reports
- Simplify technical terminology

---

# 🗄 Database Schema

## Users

- user_id
- name
- email
- password_hash
- created_at

---

## Medical_Images

- image_id
- user_id
- image_path
- image_type
- upload_date

---

## Predictions

- prediction_id
- image_id
- disease_name
- confidence_score
- prediction_date

---

## Reports

- report_id
- prediction_id
- ai_summary
- precautions
- pdf_path

---

## Chat_History

- chat_id
- user_id
- question
- answer
- timestamp

---

# 💻 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap / Tailwind CSS

## Backend

- Flask

## Deep Learning

- TensorFlow
- Keras
- OpenCV

## Generative AI

- Gemini API

## Database

- MYSQL

## ORM

- SQLAlchemy

## PDF

- ReportLab

---

# 📂 Project Structure

```
VisionCare-AI/

│── app.py
│── requirements.txt
│── config.py
│── README.md

├── static/
│     ├── css/
│     ├── js/
│     ├── images/
│
├── templates/
│     ├── index.html
│     ├── login.html
│     ├── register.html
│     ├── dashboard.html
│     ├── upload.html
│     ├── prediction.html
│     ├── report.html
│     ├── chat.html
│
├── model/
│     ├── cnn_model.h5
│     ├── predict.py
│
├── database/
│     ├── models.py
│     ├── database.py
│
├── ai/
│     ├── gemini.py
│     ├── prompt.py
│
├── reports/
│
├── uploads/
│
└── utils/
```

---

# 🔒 Security Features

- Password Hashing
- Secure File Upload
- Input Validation
- SQL Injection Protection
- Session Management

---

# 🌟 Future Enhancements

- Multi-disease support
- Explainable AI (Grad-CAM heatmaps)
- Doctor Dashboard
- Hospital Integration
- Mobile Application
- Cloud Deployment
- Multi-language Support
- Medical History Analytics

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Deep Learning
- CNN Architecture
- Medical Image Processing
- Generative AI
- Prompt Engineering
- Flask Development
- PostgreSQL Database
- REST API Development
- Authentication System
- PDF Report Generation
- Full Stack Development

---

# 👨‍💻 Developed By

**Krishan Kumar Saini**
Bachelor of Technology (Computer Science Engineering)

Final Year Project

---

## ⭐ If you find this project helpful, consider giving it a star on GitHub!