# Design Specs

## API Contracts

**1. Shorten URL**
- **Endpoint:** `POST /api/shorten`
- **Request Body:** `{ "original_url": "https://example.com/very/long/path" }`
- **Success Response (201):** 
  `{ "short_code": "aB3k9", "short_url": "http://localhost:5000/aB3k9", "original_url": "..." }`
- **Error Response (400):** `{ "error": "Invalid URL format provided." }`

**2. Redirect**
- **Endpoint:** `GET /<short_code>`
- **Behavior:** Increments click count in DB. Returns HTTP 302 redirect to `original_url`.
- **Error Response (404):** Renders a friendly "Link not found" HTML page or JSON error.

**3. Get Stats**
- **Endpoint:** `GET /api/stats`
- **Success Response (200):** 
  `[ { "short_code": "aB3k9", "original_url": "...", "clicks": 5, "created_at": "..." } ]`

## Database Schema (SQLAlchemy)
**Table:** `urls`
- `id`: Integer, Primary Key
- `original_url`: String(2048), Nullable=False
- `short_code`: String(10), Unique=True, Nullable=False, Index=True
- `clicks`: Integer, Default=0
- `created_at`: DateTime, Default=UTC Now

## UI/UX Design Language
- **Theme:** Clean, modern, minimalist SaaS aesthetic.
- **Color Palette:** Slate/Gray backgrounds (`bg-slate-50`), crisp white cards, primary interactive elements in Tailwind Indigo (`bg-indigo-600`).
- **Typography:** Inter or system default sans-serif.
- **Components:** Centered main card containing a large input field, a prominent "Shorten" button, and a hidden-until-active success banner for the generated link.
