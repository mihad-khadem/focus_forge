# 🚀 FocusForge Backend

FocusForge is a productivity backend built with Python FastAPI and MongoDB, designed to track tasks, habits, focus sessions, and real coding activity via WakaTime API integration.

---

## 🧰 Tech Stack

- **Python:** 3.11+
- **Framework:** FastAPI
- **Database:** MongoDB (Motor or MongoEngine)
- **Authentication:** JWT, bcrypt (Passlib)
- **Scheduler:** APScheduler or AsyncIO tasks
- **External API:** WakaTime for coding activity data
- **Testing:** Pytest (recommended)
- **Deployment:** Docker-compatible

---

## 📂 Project Structure

```
app/
├── api/ # FastAPI route handlers
├── core/ # Config, security utils, scheduler setup
├── db/ # MongoDB models and connection
├── services/ # Business logic and external API interactions
├── utils.py # Helpers and utility functions
├── main.py # FastAPI app entrypoint
tests/ # Unit and integration tests
Dockerfile # Container configuration
requirements.txt # Python dependencies
.env.example # Sample environment variables
README.md # This file

```

---

## ✨ Features

- JWT-based secure user authentication
- CRUD APIs for tasks, habits, and focus sessions
- Pomodoro-style focus session tracking
- Integration with WakaTime API to fetch real coding stats
- Scheduled background jobs to sync coding data periodically
- Clean, modular architecture for scalability
- Unit and integration tests for reliability

---

## ⚙️ API Endpoints Overview (Summary)

| Method | Endpoint             | Description                         |
| ------ | -------------------- | ----------------------------------- |
| POST   | `/auth/register`     | Register new user                   |
| POST   | `/auth/login`        | User login and JWT token generation |
| CRUD   | `/tasks`             | Manage user tasks                   |
| CRUD   | `/habits`            | Manage habits and streaks           |
| CRUD   | `/focus_sessions`    | Track Pomodoro focus sessions       |
| POST   | `/wakastats/connect` | Connect WakaTime account            |
| GET    | `/wakastats`         | Get latest coding statistics        |
| POST   | `/wakastats/fetch`   | Trigger manual coding data fetch    |

---

## 🚀 Getting Started

1. Clone the repo and navigate to the project root
2. Create a `.env` file based on `.env.example` with your config
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python main.py
   ```

---

## 🛠 Challenges & Solutions

- OAuth & API key management for secure WakaTime integration

- Rate limiting on WakaTime API handled with caching & scheduled fetches

- Data synchronization ensuring no duplicates and consistent updates

- Robust error handling in background jobs and API routes

## 🔮 Future Backend Enhancements

- Full OAuth2 with refresh tokens for WakaTime

- Real-time WebSocket API for live focus & coding stats

- AI-powered backend productivity suggestions and analytics

- Multi-user and team support with role-based access control

- API integrations with calendars and other productivity tools

- Offline data sync and conflict resolution
