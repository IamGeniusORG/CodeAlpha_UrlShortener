# Codebase Guardrails & Rules

## Coding Conventions
- **Python:** Strict adherence to PEP 8 guidelines. Use type hints for all function signatures.
- **Flask:** Keep routes lightweight. Offload complex generation or database logic to dedicated helper modules/services.
- **Frontend:** Use semantic HTML. Keep Tailwind classes organized. No heavy frontend frameworks (React/Vue)—stick to Vanilla JS.

## Preferred Directory Structure
Keep the project modular. Do not dump everything in `app.py`.
```text
CodeAlpha_UrlShortener/
├── app/
│   ├── __init__.py      # App factory & DB initialization
│   ├── models.py        # SQLAlchemy database schemas
│   ├── routes.py        # API and view routes
│   ├── utils.py         # Base62/nanoid generation logic
│   ├── static/          # CSS, JS, Images
│   └── templates/       # HTML files (index.html)
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── run.py               # Application entry point
```

## Security & Validation Rules

* **Input Validation:** All submitted URLs must be verified using a regex or a library like `urllib.parse` before processing. Reject malformed URLs with a `400 Bad Request`.
* **SQL Injection:** Absolutely no raw SQL strings. All database interactions must happen through SQLAlchemy ORM.
* **Rate Limiting:** (Optional but recommended) Implement basic Flask-Limiter on the generation endpoint to prevent spam.

## Testing Requirements

* Use `pytest` for backend testing.
* Must include tests for: URL validation logic, short code collision prevention, and basic route status codes (200, 302, 400, 404).
