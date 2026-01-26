---
page_type: sample
languages:
- azdeveloper
- python
- bicep
- html
products:
- azure
- azure-app-service
- azure-database-postgresql
urlFragment: cosmos-voyage
name: CosmosVoyage - FastAPI Space Travel Platform with PostgreSQL
description: A modern space travel booking platform built with FastAPI, PostgreSQL, and Azure. Features REST API, booking system, and destination management.
---

<div align="center">

# 🚀 CosmosVoyage

### *Your Gateway to Galactic Adventures*

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Azure](https://img.shields.io/badge/Azure-Ready-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/ChelseaVadlapati/CosmosVoyage?style=for-the-badge)](https://github.com/ChelseaVadlapati/CosmosVoyage/stargazers)
[![Issues](https://img.shields.io/github/issues/ChelseaVadlapati/CosmosVoyage?style=for-the-badge)](https://github.com/ChelseaVadlapati/CosmosVoyage/issues)

**A production-ready, full-stack space travel booking platform built with modern Python technologies**

[Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-documentation) • [Deployment](#️-deployment-to-azure) • [Contributing](#-contributing)

---

</div>

## 📖 About

**CosmosVoyage** is a full-stack web application designed for a futuristic space travel agency. Built with **FastAPI** and **PostgreSQL**, it showcases modern web development practices including:

- 🎨 Beautiful, responsive web interface for browsing space destinations and cruises
- ⚡ High-performance REST API with automatic OpenAPI documentation
- 🗄️ Robust database design with SQLModel ORM
- ☁️ Cloud-native architecture ready for Azure deployment
- 🧪 Comprehensive testing with Playwright
- 🔒 Production-grade security and error handling

Whether you're learning modern Python web development or building a real-world application, CosmosVoyage demonstrates industry best practices and patterns.

## ✨ Features

<table>
<tr>
<td width="50%">

### 🌐 Web Application
- **Responsive UI** - Beautiful interface that works on all devices
- **Space Destinations** - Browse exotic locations across the galaxy
- **Cruise Booking** - View and request information about space cruises
- **Interactive Forms** - Submit travel inquiries with ease

</td>
<td width="50%">

### 🔌 REST API
- **OpenAPI 3.0** - Automatic Swagger UI documentation
- **RESTful Endpoints** - Standard CRUD operations
- **JSON Responses** - Easy integration with any client
- **Health Checks** - Monitor application status

</td>
</tr>
<tr>
<td width="50%">

### 🗄️ Database
- **PostgreSQL 16** - Reliable, ACID-compliant storage
- **SQLModel ORM** - Type-safe database operations
- **Migrations** - Easy schema management
- **Seed Data** - Pre-populated sample data

</td>
<td width="50%">

### ☁️ Cloud Native
- **Azure Ready** - Optimized for Azure App Service
- **Infrastructure as Code** - Bicep templates included
- **CI/CD** - GitHub Actions workflows
- **Monitoring** - Azure Application Insights integration

</td>
</tr>
</table>

### 🎯 Key Highlights

- ✅ **Production-Ready** - Error handling, logging, and monitoring
- ✅ **Developer-Friendly** - Dev container support, hot reload
- ✅ **Well-Tested** - Playwright integration tests
- ✅ **Documented** - Comprehensive API and setup documentation
- ✅ **Type-Safe** - Full Python type hints with Pydantic models
- ✅ **Secure** - Environment-based configuration, no hardcoded secrets

## 🚀 Quick Start

> **💡 Tip:** See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions and troubleshooting!

### Prerequisites

- 🐍 Python 3.13 or higher
- 🐘 PostgreSQL 16
- 💻 VS Code (recommended)

### Installation (macOS/Linux)

```bash
# 1️⃣ Install and start PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# 2️⃣ Create database
/opt/homebrew/opt/postgresql@16/bin/createdb fastapi_app

# 3️⃣ Clone and navigate to project
git clone https://github.com/ChelseaVadlapati/CosmosVoyage.git
cd CosmosVoyage

# 4️⃣ Setup environment variables
cp .env.example .env
# Edit .env with your database credentials

# 5️⃣ Create virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e src

# 6️⃣ Initialize database with sample data
python src/fastapi_app/seed_data.py

# 7️⃣ Run the application
python -m uvicorn fastapi_app:app --reload --port=8000
```

### 🎉 Access the Application

- **Main Website**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/api/docs
- **Alternative API Docs**: http://localhost:8000/api/redoc
- **Health Check**: http://localhost:8000/api/health

### 🐳 Using Dev Container (Alternative)

If you have Docker and VS Code with Dev Containers extension:

```bash
# Simply open the project in VS Code
code .
# Click "Reopen in Container" when prompted
```

Everything will be configured automatically!

## 📚 API Documentation

CosmosVoyage provides a comprehensive REST API with automatic documentation:

### Available Endpoints

#### 🌍 Destinations
```http
GET  /api/destinations          # List all space destinations
GET  /api/destination/{id}      # Get specific destination details
```

#### 🚢 Cruises
```http
GET  /api/cruises               # List all available cruises
GET  /api/cruise/{id}           # Get specific cruise details
```

#### 🏥 Health & Monitoring
```http
GET  /api/health                # Application health check
```

### Interactive Documentation

Once your application is running, explore the API using:

- **Swagger UI** (http://localhost:8000/api/docs) - Interactive API testing interface
- **ReDoc** (http://localhost:8000/api/redoc) - Clean, searchable API documentation

### Example API Request

```bash
# Get all destinations
curl http://localhost:8000/api/destinations

# Get specific destination
curl http://localhost:8000/api/destination/1

# Health check
curl http://localhost:8000/api/health
```

### Example Response

```json
{
  "id": 1,
  "name": "Mars Colony Alpha",
  "description": "Experience life on the Red Planet",
  "cruises": [
    {
      "id": 1,
      "name": "Mars Express"
    }
  ]
}
```

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="25%">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="80" alt="FastAPI"/><br/>
<b>FastAPI</b><br/>
Modern Python web framework
</td>
<td align="center" width="25%">
<img src="https://www.postgresql.org/media/img/about/press/elephant.png" width="80" alt="PostgreSQL"/><br/>
<b>PostgreSQL 16</b><br/>
Reliable database
</td>
<td align="center" width="25%">
<img src="https://sqlmodel.tiangolo.com/img/logo-margin/logo-margin-vector.svg" width="80" alt="SQLModel"/><br/>
<b>SQLModel</b><br/>
Type-safe ORM
</td>
<td align="center" width="25%">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="100" alt="Python"/><br/>
<b>Python 3.13</b><br/>
Core language
</td>
</tr>
</table>

### Frontend & Templates
- **Jinja2** - Server-side templating
- **Bootstrap** - Responsive CSS framework
- **Custom SCSS** - Styled components

### Cloud & DevOps
- **Azure App Service** - Application hosting
- **Azure Database for PostgreSQL** - Managed database
- **Azure Application Insights** - Monitoring & analytics
- **GitHub Actions** - CI/CD pipelines
- **Azure Developer CLI (azd)** - Deployment automation

### Development Tools
- **Uvicorn** - ASGI server with hot reload
- **Playwright** - End-to-end testing
- **pytest** - Unit testing framework
- **Ruff** - Fast Python linter
- **Docker** - Dev container support

## 📁 Project Structure

```
CosmosVoyage/
│
├── 📂 src/                          # Source code
│   ├── 📂 fastapi_app/              # Main application package
│   │   ├── 📄 __init__.py           # Package initialization
│   │   ├── 📄 app.py                # FastAPI routes & endpoints
│   │   ├── 📄 models.py             # SQLModel database models
│   │   └── 📄 seed_data.py          # Database seeding script
│   │
│   ├── 📂 templates/                # Jinja2 HTML templates
│   │   ├── 📄 base.html             # Base template
│   │   ├── 📄 index.html            # Homepage
│   │   ├── 📄 destinations.html    # Destinations listing
│   │   └── 📄 ...                   # Other templates
│   │
│   ├── 📂 static/                   # Static assets
│   │   ├── 📂 res/css/              # Stylesheets
│   │   ├── 📂 res/img/              # Images
│   │   └── 📂 res/scss/             # SCSS source files
│   │
│   ├── 📂 tests/                    # Test suites
│   │   ├── 📂 local/                # Local development tests
│   │   └── 📂 smoke/                # Smoke tests
│   │
│   ├── 📄 requirements.txt          # Production dependencies
│   └── 📄 pyproject.toml            # Package configuration
│
├── 📂 infra/                        # Azure infrastructure (Bicep)
│   ├── 📄 main.bicep                # Main infrastructure template
│   ├── 📄 db.bicep                  # Database configuration
│   ├── 📄 web.bicep                 # Web app configuration
│   └── 📂 core/                     # Reusable Bicep modules
│
├── 📂 .devcontainer/                # Dev container configuration
│   ├── 📄 devcontainer.json         # Container settings
│   └── 📄 docker-compose_dev.yml    # Docker compose for dev
│
├── 📂 .github/workflows/            # GitHub Actions CI/CD
│   ├── 📄 azure-dev.yml             # Azure deployment workflow
│   ├── 📄 tests.yml                 # Test automation
│   └── 📄 ...                       # Other workflows
│
├── 📄 .env.example                  # Environment template
├── 📄 README.md                     # This file
├── 📄 QUICKSTART.md                 # Quick start guide
├── 📄 azure.yaml                    # Azure Developer CLI config
└── 📄 requirements-dev.txt          # Development dependencies
```

## 🧪 Running Tests

CosmosVoyage includes comprehensive test coverage with Playwright for end-to-end testing.

### Setup Testing Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install Playwright browsers
python -m playwright install chromium --with-deps
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/fastapi_app --cov-report=html

# Run specific test file
pytest src/tests/local/test_playwright.py

# Run with verbose output
pytest -v
```

### Test Structure

- **Unit Tests** - Test individual functions and models
- **Integration Tests** - Test API endpoints and database operations
- **E2E Tests** - Test complete user workflows with Playwright

### Continuous Integration

Tests run automatically on every push and pull request via GitHub Actions. See `.github/workflows/tests.yml` for configuration.

## ☁️ Deployment to Azure

CosmosVoyage is optimized for Azure deployment using the Azure Developer CLI (azd).

### Prerequisites

- Azure account ([Create free account](https://azure.microsoft.com/free/))
- Azure Developer CLI ([Installation guide](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd))

### Deploy to Azure

```bash
# 1️⃣ Login to Azure
azd auth login

# 2️⃣ Initialize and deploy (first time)
azd up
```

This single command will:
- ✅ Provision all Azure resources (App Service, PostgreSQL, etc.)
- ✅ Deploy your application code
- ✅ Configure environment variables
- ✅ Set up monitoring and logging

### Update Deployment

After making changes to your code:

```bash
# Deploy updated code
azd deploy
```

### Environment Configuration

The deployment will prompt you for:
- **Environment name** - e.g., "prod", "staging" (lowercase, alphanumeric)
- **Azure subscription** - Select from your available subscriptions
- **Region** - e.g., "eastus", "westus2"

### CI/CD with GitHub Actions

Automate deployments on every push to main:

```bash
# Configure GitHub Actions
azd pipeline config
```

This will:
- Create necessary Azure service principal
- Configure GitHub secrets
- Enable automatic deployments

### Monitoring

Once deployed, monitor your application:
- **Azure Portal** - View metrics, logs, and diagnostics
- **Application Insights** - Detailed performance monitoring
- **Health Endpoint** - `https://your-app.azurewebsites.net/api/health`

### Cost Estimation

Resources deployed (approximate monthly cost):
- **App Service (Basic)**: ~$13-55/month
- **PostgreSQL Flexible Server**: ~$15-200/month
- **Application Insights**: Pay-as-you-go (free tier available)

💡 **Tip**: Use `azd down` to delete all resources when done testing.

## 🤝 Contributing

We love contributions! Whether it's bug fixes, new features, or documentation improvements, your help is welcome.

### How to Contribute

1. **Fork the repository**
   ```bash
   # Click "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CosmosVoyage.git
   cd CosmosVoyage
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow existing code style (Ruff for linting)
   - Add tests for new features
   - Update documentation as needed

5. **Test your changes**
   ```bash
   pytest
   ruff check .
   ```

6. **Commit and push**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Describe your changes

### Development Guidelines

- 📝 Write clear commit messages
- ✅ Ensure all tests pass
- 📚 Update documentation for new features
- 🎨 Follow Python PEP 8 style guidelines
- 🔒 Never commit sensitive data or credentials

### Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

### Need Help?

- 💬 Open an [issue](https://github.com/ChelseaVadlapati/CosmosVoyage/issues) for bugs or questions
- 💡 Start a [discussion](https://github.com/ChelseaVadlapati/CosmosVoyage/discussions) for ideas
- 📧 Contact the maintainers

## � Troubleshooting

### Common Issues

<details>
<summary><b>Database connection errors</b></summary>

```bash
# Check if PostgreSQL is running
brew services list

# Restart PostgreSQL
brew services restart postgresql@16

# Verify database exists
psql -l | grep fastapi_app
```
</details>

<details>
<summary><b>Port 8000 already in use</b></summary>

```bash
# Find process using port 8000
lsof -ti:8000

# Kill the process
lsof -ti:8000 | xargs kill

# Or use a different port
python -m uvicorn fastapi_app:app --reload --port=8001
```
</details>

<details>
<summary><b>Import errors</b></summary>

```bash
# Ensure package is installed in editable mode
pip install -e src

# Verify PYTHONPATH includes src directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```
</details>

<details>
<summary><b>Environment variables not loading</b></summary>

```bash
# Ensure .env file exists
cp .env.example .env

# Edit .env with your settings
nano .env

# Verify variables are set
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('POSTGRES_HOST'))"
```
</details>

For more help, see [QUICKSTART.md](QUICKSTART.md) or [open an issue](https://github.com/ChelseaVadlapati/CosmosVoyage/issues).

---

## 📊 Project Stats

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/ChelseaVadlapati/CosmosVoyage?style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/ChelseaVadlapati/CosmosVoyage?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ChelseaVadlapati/CosmosVoyage?style=flat-square)

</div>

---

## �📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - You are free to:
✅ Use commercially
✅ Modify
✅ Distribute
✅ Private use
```

---

## 🌟 Acknowledgments

Built with love using these amazing technologies:

- [FastAPI](https://fastapi.tiangolo.com/) - The modern Python web framework
- [PostgreSQL](https://www.postgresql.org/) - The world's most advanced open source database
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQL databases in Python with type safety
- [Azure](https://azure.microsoft.com/) - Cloud computing platform
- [Playwright](https://playwright.dev/) - Reliable end-to-end testing

Special thanks to all [contributors](https://github.com/ChelseaVadlapati/CosmosVoyage/graphs/contributors) who help make this project better!

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ for space travel enthusiasts and Python developers**

[Report Bug](https://github.com/ChelseaVadlapati/CosmosVoyage/issues) • [Request Feature](https://github.com/ChelseaVadlapati/CosmosVoyage/issues) • [Documentation](QUICKSTART.md)

</div>

## Opening the project

This project has [Dev Container support](https://code.visualstudio.com/docs/devcontainers/containers), so it will be setup automatically if you open it in Github Codespaces or in local VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

If you're *not* using one of those options for opening the project, then you'll need to:

1. Start up a local PostgreSQL server, create a database for the app, and set the following environment variables according to your database configuration.

```shell
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_DATABASE=<YOUR DATABASE>
export POSTGRES_USERNAME=<YOUR USERNAME>
export POSTGRES_PASSWORD=<YOUR PASSWORD>
```

    Alternatively, copy `.env.example` to `.env` and fill in the values so VS Code can load them automatically.

1. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it.

1. Install production requirements:

    ```sh
    python3 -m pip install -r src/requirements.txt
    ```


1. Install the app as an editable package:

    ```sh
    python3 -m pip install -e src
    ```


1. Apply database migrations and seed initial data:

    ```sh
    python3 src/fastapi_app/seed_data.py
    ```

## Running locally

If you're running the app inside VS Code or GitHub Codespaces, you can use the "Run and Debug" button to start the app.

```sh
python3 -m uvicorn fastapi_app:app --reload --port=8000
```


## Running tests

1. Install the development requirements:

    ```sh
    python3 -m pip install -r requirements-dev.txt
    python3 -m playwright install chromium --with-deps
    ```

2. Run the tests:

    ```sh
    python3 -m pytest
    ```

## Deployment

This repo is set up for deployment on Azure via Azure App Service.

Steps for deployment:

1. Sign up for a [free Azure account](https://azure.microsoft.com/free/) and create an Azure Subscription.
2. Install the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). (If you open this repository in Codespaces or with the VS Code Dev Containers extension, that part will be done for you.)
3. Login to Azure:

    ```shell
    azd auth login
    ```

4. Provision and deploy all the resources:

    ```shell
    azd up
    ```

    It will prompt you to provide an `azd` environment name (like "myapp"), select a subscription from your Azure account, and select a location (like "eastus"). Then it will provision the resources in your account and deploy the latest code. If you get an error with deployment, changing the location can help, as there may be availability constraints for some of the resources.

5. When `azd` has finished deploying, you'll see an endpoint URI in the command output. Visit that URI, and you should see the front page of the app! 🎉

6. When you've made any changes to the app code, you can just run:

    ```shell
    azd deploy
    ```

### CI/CD pipeline

This project includes a Github workflow for deploying the resources to Azure
on every push to main. That workflow requires several Azure-related authentication secrets
to be stored as Github action secrets. To set that up, run:

```shell
azd pipeline config
```
