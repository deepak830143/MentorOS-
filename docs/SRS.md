# Software Requirements Specification (SRS)

# MentorOS

Version: 1.0

---

# 1. Introduction

## 1.1 Project Name

MentorOS – AI Powered Government Exam Preparation Platform

---

## 1.2 Purpose

MentorOS is an intelligent platform designed to help government exam aspirants prepare efficiently by combining official notifications, current affairs, AI learning assistance, digital library, study planning, and mental wellness into a single application.

---

# 2. Problem Statement

Government exam aspirants currently use multiple applications for:

- Notifications
- Current Affairs
- Books
- Mock Tests
- Study Planning
- Revision

This wastes time and reduces productivity.

MentorOS solves this by providing one unified platform.

---

# 3. Objectives

- Reduce preparation time
- Provide official notifications automatically
- Deliver AI-powered current affairs
- Improve learning efficiency
- Support multiple government exams
- Track study progress
- Reduce student burnout

---

# 4. Target Users

Students preparing for:

- UPSC
- APPSC
- SSC
- RRB
- Defence
- Banking
- State PSCs

---

# 5. User Roles

## Student

- Register
- Login
- View notifications
- Read current affairs
- Access books
- Use AI Mentor
- Track progress

---

## Admin

- Manage notifications
- Manage books
- Manage current affairs
- Review reports

---

## Super Admin

- Manage users
- Manage admins
- Configure AI
- Configure schedulers
- View analytics

---

# 6. Functional Requirements

## Authentication

- Register
- Login
- JWT Authentication

---

## Government Notification Engine

- Automatic notification collection
- Duplicate detection
- Category filtering
- Search

---

## Current Affairs

- Daily updates
- AI summaries
- MCQs
- Revision notes

---

## Digital Library

- Books
- PDFs
- Search
- Bookmark
- Continue Reading

---

## Study Planner

- Daily planner
- Revision planner
- Focus Mode
- Reminder system

---

## Mental Wellness

- Burnout detection
- Water reminder
- Sleep reminder
- Break reminder

---

## AI Mentor

- Doubt solving
- Study planning
- MCQ generation
- Topic explanation

---

# 7. Non-Functional Requirements

- Secure Authentication
- High Availability
- Fast Response Time
- Scalable Architecture
- Responsive UI
- Modular Backend

---

# 8. Technology Stack

Backend

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy

Frontend

- Flutter

AI

- OpenAI API

Scheduler

- APScheduler

---

# 9. Future Scope

- Voice Assistant
- AI Interview Coach
- Offline Reading
- Smart Revision
- Adaptive Learning
- Personalized AI Mentor

---

# 10. Conclusion

MentorOS aims to become an intelligent ecosystem for government exam preparation by integrating learning, planning, AI assistance, and mental wellness into one unified platform.