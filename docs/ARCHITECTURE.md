# MentorOS System Architecture

Version: 1.0

---

# Overview

MentorOS follows a modular, scalable architecture based on Clean Architecture principles.

The system is divided into independent modules that communicate through APIs and shared services.

---

# High Level Architecture

                    Flutter Mobile App
                            │
                    REST API (FastAPI)
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
 Authentication     Notification Engine     AI Engine
        │                   │                   │
 Current Affairs      Digital Library     Study Planner
        │                   │                   │
  Mental Health      Analytics Engine     Admin Module
                            │
                     PostgreSQL Database
                            │
                      APScheduler Jobs

---

# Backend Layers

Client (Flutter)
        │
API Routes
        │
Services
        │
Repositories
        │
Models
        │
PostgreSQL

---

# Folder Structure

MentorOS/

backend/

docs/

mobile/

assets/

README.md

LICENSE

---

# Backend Structure

backend/

app/

api/

collectors/

core/

db/

dependencies/

dto/

middleware/

models/

registry/

repositories/

scheduler/

schemas/

services/

tasks/

utils/

---

# Notification Engine

Official Websites

↓

Collectors

↓

Parser

↓

Duplicate Detection

↓

Notification Service

↓

Repository

↓

Database

↓

REST API

↓

Flutter

Supported Sources

- APPSC
- SSC
- RRB
- UPSC
- Defence
- Banking
- ISRO
- DRDO
- BEL

---

# Current Affairs Engine

Sources

- PIB
- PRS
- RBI
- NITI Aayog
- Government Ministries
- ISRO

Flow

Collector

↓

Parser

↓

AI Summary

↓

Category

↓

Database

↓

Flutter

---

# Digital Library

Books

↓

Metadata

↓

Search

↓

Bookmarks

↓

Continue Reading

↓

Flutter

---

# AI Engine

User Question

↓

OpenAI

↓

Prompt Processing

↓

Response

↓

History

↓

Analytics

---

# Study Planner

User

↓

Planner

↓

Scheduler

↓

Reminder

↓

Progress Tracking

---

# Mental Health Module

Study Hours

↓

Burnout Detection

↓

Focus Score

↓

Recommendations

↓

Dashboard

---

# Scheduler

Every Hour

Government Notifications

6 AM

Current Affairs

10 PM

Mental Wellness Report

Sunday

Weekly Analytics

---

# Authentication Flow

Register

↓

Login

↓

JWT Token

↓

Protected APIs

↓

Role Validation

---

# Future Deployment

Flutter App

↓

FastAPI

↓

Nginx

↓

PostgreSQL

↓

Cloud Storage

↓

Redis (Future)

---

# Design Principles

- Modular
- Scalable
- Clean Architecture
- RESTful APIs
- Separation of Concerns
- Reusable Components
- AI Ready

---

# Future Expansion

- Web Dashboard
- Desktop App
- AI Voice Assistant
- Offline Mode
- Multi-language Support
- AI Interview Coach