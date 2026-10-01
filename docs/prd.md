# Product Requirements Document (PRD)
**Project:** CodeAlpha_UrlShortener
**Author:** Tanmay Dey
**Objective:** Build a simple, robust URL shortener backend with a clean frontend for a CodeAlpha Backend Development Internship task.

## Core Business Logic
- Accept long URLs from users and generate highly unique, collision-resistant short codes using Base62 encoding or nanoid.
- Persist the mapping between the short code and the destination URL in a local database.
- Intercept requests to the short code and issue an HTTP 302/301 redirect to the original destination.
- Track usage metrics by incrementing a click counter every time a short link is accessed.

## Target User Personas
- **End Users:** People looking to quickly condense long, unwieldy links into easily shareable short URLs.
- **Code Assessors:** Internship reviewers evaluating clean code, RESTful design, and database management.

## Must-Have Features (MVP)
- REST API endpoint for URL submission and short code generation.
- SQLite database integration to store URLs, short codes, creation timestamps, and click counts.
- Redirection route (`GET /<short_code>`).
- Responsive, single-page frontend UI with a form to generate links.
- One-click "Copy to Clipboard" functionality for generated short links.
- Dashboard/section displaying recent link statistics (original URL, short URL, click count).
- Strict validation for URL formats and appropriate error handling (404 for missing codes, 400 for invalid URLs).
