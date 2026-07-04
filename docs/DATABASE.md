# MentorOS Database Design

Version: 1.0

---

# Overview

MentorOS uses PostgreSQL as its primary database.

The database is designed to support:

- User Management
- Government Notifications
- Current Affairs
- Digital Library
- AI Mentor
- Study Planner
- Mental Health
- Analytics

---

# Database Tables

## 1. users

Stores user accounts.

| Column | Type |
|---------|------|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role | String |
| created_at | DateTime |
| updated_at | DateTime |

---

## 2. exam_notifications

Stores government notifications.

| Column | Type |
|---------|------|
| id | Integer |
| source | String |
| organization | String |
| exam_name | String |
| notification_no | String |
| title | String |
| category | String |
| state | String |
| department | String |
| vacancies | Integer |
| qualification | String |
| age_limit | String |
| fee | String |
| salary | String |
| application_start | Date |
| application_end | Date |
| exam_date | Date |
| pdf_url | String |
| apply_url | String |
| official_url | String |
| status | String |
| notification_hash | String |
| created_at | DateTime |
| updated_at | DateTime |

---

## 3. current_affairs

Stores daily current affairs.

| Column | Type |
|---------|------|
| id | Integer |
| source | String |
| category | String |
| title | String |
| content | Text |
| summary | Text |
| keywords | Text |
| exam_relevance | String |
| created_at | DateTime |

---

## 4. books

Stores digital library information.

| Column | Type |
|---------|------|
| id | Integer |
| title | String |
| author | String |
| category | String |
| exam | String |
| file_url | String |
| cover_image | String |
| created_at | DateTime |

---

## 5. bookmarks

Stores bookmarked books.

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| book_id | Integer |
| page_number | Integer |
| created_at | DateTime |

---

## 6. study_plans

Stores study schedules.

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| title | String |
| start_date | Date |
| end_date | Date |
| status | String |

---

## 7. study_sessions

Tracks daily study.

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| duration | Integer |
| subject | String |
| completed | Boolean |
| created_at | DateTime |

---

## 8. mental_health_logs

Stores wellness information.

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| focus_score | Integer |
| stress_score | Integer |
| sleep_hours | Float |
| water_intake | Float |
| created_at | DateTime |

---

## 9. ai_chat_history

Stores AI conversations.

| Column | Type |
|---------|------|
| id | Integer |
| user_id | Integer |
| prompt | Text |
| response | Text |
| created_at | DateTime |

---

# Relationships

users
├── study_plans
├── study_sessions
├── bookmarks
├── mental_health_logs
└── ai_chat_history

books
└── bookmarks

exam_notifications
(Currently independent)

current_affairs
(Currently independent)

---

# Future Tables

- notification_logs
- revision_logs
- user_progress
- daily_statistics
- current_affair_sources
- book_categories
- ai_generated_mcqs
- exam_preferences