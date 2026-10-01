# ZipLink

A robust, fast, and beautifully designed URL shortener built as a modern, high-performance portfolio project.

## Features
- ⚡ **Lightning Fast Shortening**: Uses `nanoid` for highly unique, collision-resistant short codes.
- 🔗 **Instant Redirection**: Performs HTTP 302 redirects with minimal latency.
- 📊 **Statistics Tracking**: Automatically tracks the number of clicks for each shortened URL.
- 🎨 **Modern UI**: Clean, responsive frontend built with Tailwind CSS.
- 🛡️ **Robust Validation**: Enforces strict URL formatting checks.

## Tech Stack
- **Backend**: Python 3, Flask, SQLAlchemy (SQLite)
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS
- **Testing**: Pytest

## Quick Start Setup

1. **Clone the repository and enter the directory**:
   Navigate to the project root in your terminal.

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python run.py
   ```
   *The database (`urls.db`) will automatically initialize on the first run.*

5. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Running Tests
Run the test suite using `pytest`:
```bash
pytest
```
