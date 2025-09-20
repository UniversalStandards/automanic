# Go API Service Template

<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: api
LANGUAGE: go
FRAMEWORK: gin
BUILD_SYSTEM: go
DATABASE: postgresql
DEPLOYMENT: kubernetes
CI_CD: github-actions
TESTING: go-test
LICENSE_TYPE: apache-2.0
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->

# Go API Service

A high-performance REST API service built with Go and Gin framework.

## Features

- **High Performance**: Built with Go for excellent performance and concurrency
- **RESTful API**: Clean, well-structured REST endpoints
- **Database Integration**: PostgreSQL with GORM ORM
- **Authentication**: JWT-based authentication
- **Middleware**: Logging, CORS, rate limiting, and more
- **Testing**: Comprehensive test coverage
- **Documentation**: OpenAPI/Swagger documentation
- **Containerized**: Docker support for easy deployment
- **Kubernetes Ready**: Includes K8s manifests

## Architecture

```
cmd/
├── server/          # Application entrypoint
internal/
├── api/            # HTTP handlers and routes
├── auth/           # Authentication logic
├── config/         # Configuration management
├── database/       # Database connection and migrations
├── middleware/     # HTTP middleware
├── models/         # Data models
└── services/       # Business logic
pkg/
└── utils/          # Shared utilities
```

## Requirements

- Go 1.21+
- PostgreSQL 13+
- Docker (optional)
- Kubernetes cluster (for deployment)

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd go-api-service
   ```

2. Install dependencies:
   ```bash
   go mod tidy
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start PostgreSQL (using Docker):
   ```bash
   docker-compose up postgres -d
   ```

5. Run migrations:
   ```bash
   go run cmd/migrate/main.go
   ```

6. Start the server:
   ```bash
   go run cmd/server/main.go
   ```

The API will be available at `http://localhost:8080`

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login user
- `POST /auth/refresh` - Refresh JWT token

### Users
- `GET /users` - List users (authenticated)
- `GET /users/:id` - Get user by ID
- `PUT /users/:id` - Update user
- `DELETE /users/:id` - Delete user

### Health
- `GET /health` - Health check endpoint

## Configuration

Environment variables:

```env
# Server
PORT=8080
GIN_MODE=release

# Database
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=api_service

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRY=24h

# Redis (for rate limiting)
REDIS_URL=redis://localhost:6379/0
```

## Testing

```bash
# Run all tests
go test ./...

# Run tests with coverage
go test -cover ./...

# Run tests with detailed coverage
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

## Building

```bash
# Build for current platform
go build -o bin/server cmd/server/main.go

# Build for Linux
GOOS=linux GOARCH=amd64 go build -o bin/server-linux cmd/server/main.go

# Build Docker image
docker build -t api-service .
```

## Deployment

### Docker
```bash
docker-compose up -d
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

## API Documentation

Swagger documentation is available at `http://localhost:8080/docs` when the server is running.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.