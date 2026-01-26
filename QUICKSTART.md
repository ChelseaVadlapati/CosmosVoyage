# 🚀 Quick Start Guide

## Prerequisites
- Python 3.13+
- PostgreSQL 16
- VS Code (recommended)

## ⚡ Quick Setup

### 1. Install PostgreSQL (if not installed)
```bash
brew install postgresql@16
brew services start postgresql@16
```

### 2. Create Database
```bash
/opt/homebrew/opt/postgresql@16/bin/createdb fastapi_app
```

### 3. Configure Environment
Copy `.env.example` to `.env` and update with your settings:
```bash
cp .env.example .env
```

Update `POSTGRES_USERNAME` in `.env` to match your system username.

### 4. Install Dependencies
The Python environment should be automatically configured by VS Code. If not:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e src
```

### 5. Initialize Database
```bash
python src/fastapi_app/seed_data.py
```

### 6. Run the Application
```bash
python -m uvicorn fastapi_app:app --reload --port=8000
```

Or use VS Code's "Run and Debug" feature (F5).

## 🌐 Access the Application

- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **Health Check**: http://localhost:8000/api/health

## 🔧 New Features Added

### REST API Endpoints
- `GET /api/destinations` - List all destinations
- `GET /api/destination/{id}` - Get specific destination
- `GET /api/cruises` - List all cruises
- `GET /api/cruise/{id}` - Get specific cruise
- `GET /api/health` - Health check endpoint

### Improvements
- ✅ Enhanced error handling with custom exception handlers
- ✅ 404 error handling for missing resources
- ✅ API documentation with Swagger UI
- ✅ Health check endpoint for monitoring
- ✅ Better logging and monitoring support
- ✅ Fixed PostgreSQL connection to allow empty passwords for local dev

## 🧪 Running Tests
```bash
pip install -r requirements-dev.txt
python -m playwright install chromium --with-deps
pytest
```

## 📦 Project Structure
```
src/
├── fastapi_app/
│   ├── app.py          # Main application with routes
│   ├── models.py       # Database models
│   └── seed_data.py    # Database seeding script
├── templates/          # HTML templates
└── static/            # Static files (CSS, JS, images)
```

## 🐛 Troubleshooting

### Database Connection Issues
- Ensure PostgreSQL is running: `brew services list`
- Check your `.env` file has correct credentials
- Verify database exists: `psql -l`

### Import Errors
- Make sure you installed the package: `pip install -e src`
- Check your PYTHONPATH includes the src directory

### Port Already in Use
- Change the port in the command: `--port=8001`
- Or kill the process using port 8000: `lsof -ti:8000 | xargs kill`
