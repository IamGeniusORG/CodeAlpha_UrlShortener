# System Architecture & Tech Stack

## System Topology
A monolithic web application comprising a backend REST API and a statically served single-page frontend.

## Exact Tech Stack
- **Backend Framework:** Python / Flask
- **Database:** SQLite
- **ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Frontend UI:** HTML5, Tailwind CSS (via CDN for simplicity), Vanilla JavaScript for API interactions.
- **Unique ID Generation:** `nanoid` (Python implementation) or custom Base62 encoding.

## Service Communication
- The Vanilla JS frontend communicates with the Flask backend asynchronously via the `fetch` API.
- The Flask backend queries and updates the SQLite database synchronously using SQLAlchemy models.

## Deployment Choices
- **Development:** Localhost with Flask's built-in server or Waitress/Gunicorn for local production-simulation.
- **Production (Target):** Containerized deployment (Docker) or a lightweight PaaS (e.g., Render, Railway) suitable for SQLite-backed Flask apps.
