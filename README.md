# ⚡ AI-Powered Developer Collaboration Platform

A real-time collaborative coding environment designed to enhance remote pair programming, technical interviews, and open-source teamwork — powered by AI and GitHub OAuth.

## 🚀 Features

- 👥 **Live Code Sync** — Collaborate in real-time like Google Docs, but for code
- 🤖 **AI Code Review** — Instant feedback on your code with OpenAI integration
- 🔐 **Secure GitHub Login** — OAuth-based authentication for a seamless developer experience
- ☁️ **Scalable Cloud Architecture** — Dockerized microservices ready for AWS deployment

## 🛠 Tech Stack

### Frontend
- React + TypeScript
- Tailwind CSS

### Backend
- Flask (Python) — for AI & auth services
- Node.js + Socket.io — for real-time collaboration
- PostgreSQL — for user and session data

### DevOps
- Docker + Docker Compose
- Environment variables via `.env`
- AWS-ready deployment

## 📦 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai-dev-collab.git
   cd ai-dev-collab

2. **Add your environment variables**

   Create a .env file in the backend and frontend directories. Example:

   ```env
   # .env
   GITHUB_CLIENT_ID=your_client_id
   GITHUB_CLIENT_SECRET=your_client_secret
   FLASK_SECRET_KEY=your_flask_secret
   FRONTEND_URL=http://localhost:5173
   DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@db:5432/postgres
   ```

3. **Start with Docker Compose**

   ```bash
   docker-compose up --build
   ```

4. **Visit the app**

   * Frontend: [http://localhost:5173](http://localhost:5173)
   * Backend: [http://localhost:5000](http://localhost:5000)
