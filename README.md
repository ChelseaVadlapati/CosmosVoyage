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

# CosmosVoyage 🚀

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A Modern Space Travel Booking Platform**

CosmosVoyage is a full-stack web application for a space travel agency built with FastAPI and PostgreSQL. The application features a beautiful web interface for browsing destinations and cruises, plus a comprehensive REST API for programmatic access.

## ✨ Features

- 🌐 **Web Interface** - Beautiful, responsive UI for browsing space destinations and cruises
- 🔌 **REST API** - Comprehensive API with automatic Swagger/OpenAPI documentation
- 🗄️ **PostgreSQL Database** - Reliable data storage with SQLModel ORM
- ☁️ **Azure Ready** - Configured for easy deployment to Azure App Service
- 🐳 **Dev Container** - Instant development environment setup
- 🧪 **Testing** - Includes Playwright tests for UI testing
- 📊 **Monitoring** - Health check endpoints and Azure Monitor integration

## 🚀 Quick Start

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions!

**TL;DR:**
```bash
# Install PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# Create database
/opt/homebrew/opt/postgresql@16/bin/createdb fastapi_app

# Setup environment
cp .env.example .env
# (Edit .env with your settings)

# Install and run
pip install -e src
python src/fastapi_app/seed_data.py
python -m uvicorn fastapi_app:app --reload --port=8000
```

Visit http://localhost:8000 🎉

## 📚 API Documentation

Once running, access:
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **Health Check**: http://localhost:8000/api/health

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.13
- **Database**: PostgreSQL 16, SQLModel
- **Frontend**: Jinja2 Templates, Bootstrap
- **Cloud**: Azure App Service, Azure Database for PostgreSQL
- **DevOps**: GitHub Actions, Azure Developer CLI (azd)

## 📁 Project Structure

```
CosmosVoyage/
├── src/
│   ├── fastapi_app/        # Main application
│   │   ├── app.py          # FastAPI routes and endpoints
│   │   ├── models.py       # Database models
│   │   └── seed_data.py    # Database seeding script
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, images
│   └── tests/              # Test suites
├── infra/                  # Azure infrastructure (Bicep)
└── .devcontainer/          # Dev container configuration
```

## 🧪 Running Tests

```bash
pip install -r requirements-dev.txt
python -m playwright install chromium --with-deps
pytest
```

## ☁️ Deployment to Azure

This project is configured for deployment with the Azure Developer CLI (azd):

```bash
azd auth login
azd up
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

Built with FastAPI, PostgreSQL, and Azure technologies.

---

**Made with ❤️ for space travel enthusiasts**

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
