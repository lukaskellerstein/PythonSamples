# FastAPI Sample Server

A simple FastAPI server with sample endpoints demonstrating GET, POST, PUT, PATCH, and DELETE operations.

## Installation

```bash
pip install fastapi uvicorn
```

## Running the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

## Testing with cURL

### Basic Endpoints

```bash
# Root endpoint
curl -X GET http://localhost:8000/

# Health check
curl -X GET http://localhost:8000/health
```

### Items Endpoints

```bash
# Get all items
curl -X GET http://localhost:8000/items

# Get specific item
curl -X GET http://localhost:8000/items/1

# Create new item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tablet",
    "description": "Android tablet",
    "price": 300.0
  }'

# Update entire item (PUT)
curl -X PUT http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gaming Laptop Updated",
    "description": "High-end gaming laptop",
    "price": 1500.0
  }'

# Partial update item (PATCH)
curl -X PATCH http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1400.0
  }'

# Delete item
curl -X DELETE http://localhost:8000/items/1
```

### Users Endpoints

```bash
# Get all users
curl -X GET http://localhost:8000/users

# Create new user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bob Wilson",
    "email": "bob@example.com"
  }'
```

## Running Tests

```bash
python test_server.py
```
