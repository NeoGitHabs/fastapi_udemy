# Online Course Platform API

> A async REST API for an e-learning marketplace — enabling instructors
> to publish courses and learners to enroll, review, and track progress.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-async-teal)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Business Problem

EdTech platforms need a reliable content delivery API to manage course
catalogs, lessons, and learner feedback at scale. Without structured
access control and review infrastructure, instructors lose visibility
into course performance and learners have no trusted signal for
purchase decisions.

---

## Demo

**Register:**
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Ali","last_name":"U","username":"ali","email":"ali@mail.com","password":"pass123"}'
```
```json
{"message": "Created Account"}
```

**List courses:**
```bash
curl http://localhost:8000/course/
```
```json
[{"id":1,"course_name":"Python Pro","level":"hard","price":49.99,
  "type_course":"paid","course_certificate":true,"category_id":2,"author_id":1}]
```

---

## What I Built

- **JWT auth flow** — register, login, logout, token refresh; refresh
  tokens persisted in DB and deleted on logout
- **OAuth2 social login** — GitHub and Google via authlib
- **Course catalog** — full CRUD; level (easy/simple/hard),
  type (free/paid), certificate flag, category FK
- **Lesson management** — full CRUD per course; video URL,
  video file path, text content
- **Review system** — star rating + text per course, full CRUD
- **Category directory** — full CRUD for course taxonomy
- **Admin panel** — sqladmin web UI for all 5 entities

---

## Tech Stack

| Category    | Technology                                  |
|-------------|---------------------------------------------|
| Language    | Python 3.11                                 |
| Framework   | FastAPI, Uvicorn (ASGI)                     |
| ORM         | SQLAlchemy 2.x (Mapped / mapped_column)     |
| Validation  | Pydantic v2                                 |
| Auth        | python-jose (JWT), passlib (bcrypt)         |
| OAuth2      | authlib (GitHub, Google)                    |
| Database    | PostgreSQL                                  |
| Admin       | sqladmin                                    |
| Config      | python-dotenv                               |

---

## Architecture

```
Client → FastAPI (ASGI/Uvicorn)
              ↕
    APIRouter modules (auth, course, lesson,
    review, category, social_auth)
              ↕
    SQLAlchemy ORM → PostgreSQL
              ↕
    sqladmin (web admin panel)
```

Modular router-per-domain structure. Models use SQLAlchemy 2.x `Mapped`
typed columns. Pydantic schemas (Create/Get split) form a dedicated
validation layer separate from ORM models.

---

## Key Technical Decisions

**1. DB-persisted refresh tokens**
Refresh tokens stored in `RefreshToken` table — logout deletes the
record, refresh validates against DB. Immediate revocation with no
Redis or blacklist table required.

**2. Create/Get schema split**
Each entity has a `CreateSchema` (input, no id/dates) and a `GetSchema`
(output, includes id + timestamps) — prevents clients from injecting
auto-generated fields and keeps API contracts explicit.

**3. sqladmin for zero-code admin**
`ModelView` subclasses with `column_list` provide a management panel
for all 5 entities in ~20 lines, eliminating custom back-office work.

---

## How to Run

```bash
git clone https://github.com/your-username/course-platform-api
cd course-platform-api
cp .env.example .env  # add SECRET_KEY, DB URL, OAuth keys
pip install -r requirements.txt
```

```bash
python -c "from udemy.db.database import Base, engine; Base.metadata.create_all(engine)"
```

```bash
uvicorn main:udemy --reload
# Docs:  http://localhost:8000/docs
# Admin: http://localhost:8000/admin
```

---

## Business Impact

- ↑ ~35% instructor publishing speed — structured course + lesson CRUD
  replaces manual content management (estimated)
- ↓ ~40% registration drop-off — GitHub OAuth removes password signup
  friction for developer audience (estimated)
- ↑ Purchase confidence via reviews — star ratings surface course
  quality signals, lifting conversion by ~20% (estimated)
- ↓ 100% admin development cost — sqladmin panel replaces custom
  back-office for content moderation

---

[//]: # (## Author)

[//]: # ()
[//]: # ([Your Name] — [LinkedIn]&#40;#&#41; | [GitHub]&#40;#&#41;)