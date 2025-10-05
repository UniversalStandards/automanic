# Python Web Application Template

<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: web-app
LANGUAGE: python
FRAMEWORK: fastapi
BUILD_SYSTEM: pip
DATABASE: postgresql
DEPLOYMENT: docker
CI_CD: github-actions
TESTING: pytest
LICENSE_TYPE: mit
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->

# FastAPI Web Application

A modern, fast (high-performance) web API with Python 3.8+ based on standard Python type hints.

## Features

- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic)
- **Fast to code**: Increase the speed to develop features by about 200% to 300%
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors
- **Intuitive**: Great editor support with autocompletion everywhere
- **Easy**: Designed to be easy to use and learn
- **Short**: Minimize code duplication
- **Robust**: Get production-ready code with automatic interactive documentation

## Requirements

- Python 3.8+
- PostgreSQL (for database)
- Docker (for deployment)

## Quick Start

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up database: `createdb myapp`
4. Run the application: `uvicorn src.main:app --reload`
5. Open http://localhost:8000/docs for interactive API documentation

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

## Database

This application uses PostgreSQL with SQLAlchemy ORM and Alembic for migrations.

## Testing

Run tests with: `pytest`

## Deployment

Deploy using Docker:
```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.