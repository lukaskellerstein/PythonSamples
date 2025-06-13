import httpx
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Sample Server"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_all_items():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_get_specific_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "price" in data


def test_get_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_create_item():
    new_item = {"name": "Test Item", "description": "Test description", "price": 99.99}
    response = client.post("/items", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == new_item["name"]
    assert data["price"] == new_item["price"]
    assert "id" in data


def test_update_item_put():
    updated_item = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 199.99,
    }
    response = client.put("/items/1", json=updated_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_item["name"]
    assert data["price"] == updated_item["price"]
    assert data["id"] == 1


def test_update_nonexistent_item_put():
    updated_item = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 199.99,
    }
    response = client.put("/items/999", json=updated_item)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_partial_update_item_patch():
    partial_update = {"price": 299.99}
    response = client.patch("/items/1", json=partial_update)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == partial_update["price"]
    assert data["id"] == 1


def test_partial_update_nonexistent_item_patch():
    partial_update = {"price": 299.99}
    response = client.patch("/items/999", json=partial_update)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_create_user():
    new_user = {"name": "Test User", "email": "test@example.com"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == new_user["name"]
    assert data["email"] == new_user["email"]
    assert "id" in data


def test_delete_item():
    new_item = {
        "name": "Item to Delete",
        "description": "Will be deleted",
        "price": 50.0,
    }
    create_response = client.post("/items", json=new_item)
    created_item = create_response.json()
    item_id = created_item["id"]

    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    assert "message" in delete_data
    assert "deleted_item" in delete_data


def test_delete_nonexistent_item():
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


if __name__ == "__main__":
    print("Running FastAPI server tests...")

    print("✓ Testing root endpoint...")
    test_root_endpoint()

    print("✓ Testing health check...")
    test_health_check()

    print("✓ Testing get all items...")
    test_get_all_items()

    print("✓ Testing get specific item...")
    test_get_specific_item()

    print("✓ Testing get nonexistent item...")
    test_get_nonexistent_item()

    print("✓ Testing create item...")
    test_create_item()

    print("✓ Testing update item (PUT)...")
    test_update_item_put()

    print("✓ Testing update nonexistent item (PUT)...")
    test_update_nonexistent_item_put()

    print("✓ Testing partial update item (PATCH)...")
    test_partial_update_item_patch()

    print("✓ Testing partial update nonexistent item (PATCH)...")
    test_partial_update_nonexistent_item_patch()

    print("✓ Testing get all users...")
    test_get_all_users()

    print("✓ Testing create user...")
    test_create_user()

    print("✓ Testing delete item...")
    test_delete_item()

    print("✓ Testing delete nonexistent item...")
    test_delete_nonexistent_item()

    print("\n✅ All tests passed!")
