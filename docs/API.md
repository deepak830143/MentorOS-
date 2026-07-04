# MentorOS API Documentation

Version 1.0

---

# Base URL

Development

http://127.0.0.1:8000

Production

https://api.mentoros.in

---

# Authentication APIs

## Register

POST

/api/v1/auth/register

Request

```json
{
    "name":"Deepak",
    "email":"deepak@gmail.com",
    "password":"password123"
}
```

Response

```json
{
    "id":1,
    "name":"Deepak",
    "email":"deepak@gmail.com"
}
```

---

## Login

POST

/api/v1/auth/login

Response

```json
{
    "access_token":"JWT_TOKEN",
    "token_type":"bearer"
}
```

---

# User APIs

## Current User

GET

/api/v1/users/me

---

# Notification APIs

## Get Notifications

GET

/api/v1/notifications

---

## Get Notification

GET

/api/v1/notifications/{id}

---

## Create Notification

POST

/api/v1/notifications

---

## Delete Notification

DELETE

/api/v1/notifications/{id}

---

# Current Affairs APIs

(Upcoming)

GET

/api/v1/current-affairs

GET

/api/v1/current-affairs/{id}

---

# Books APIs

(Upcoming)

GET

/api/v1/books

GET

/api/v1/books/{id}

POST

/api/v1/books/bookmark

---

# AI APIs

(Upcoming)

POST

/api/v1/ai/chat

POST

/api/v1/ai/mcq

POST

/api/v1/ai/study-plan

---

# Study Planner APIs

(Upcoming)

GET

/api/v1/planner

POST

/api/v1/planner

PUT

/api/v1/planner/{id}

DELETE

/api/v1/planner/{id}

---

# Mental Health APIs

(Upcoming)

POST

/api/v1/mental-health/log

GET

/api/v1/mental-health/report

---

# Admin APIs

(Upcoming)

GET

/api/v1/admin/users

GET

/api/v1/admin/statistics

POST

/api/v1/admin/notifications

DELETE

/api/v1/admin/users/{id}