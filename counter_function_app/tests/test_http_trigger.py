import json
import pytest
from unittest.mock import patch, MagicMock
import azure.functions as func
import main  # adjust if your file name is different


@pytest.fixture
def mock_req_get():
    """Mock GET request."""
    return func.HttpRequest(
        method='GET',
        url='/api/http_trigger',
        body=None,
    )


@pytest.fixture
def mock_req_post():
    """Mock POST request."""
    return func.HttpRequest(
        method='POST',
        url='/api/http_trigger',
        body=None,
    )


def make_mock_container(count=1):
    """Create a mocked Cosmos container."""
    mock_container = MagicMock()
    mock_container.read_item.return_value = {"id": "1", "count": count}
    return mock_container


@patch("counter_function_app.main.CosmosClient")
def test_get_request_returns_count(mock_cosmos, mock_req_get):
    """Test GET request returns count from mocked Cosmos DB."""
    mock_client = MagicMock()
    mock_container = make_mock_container(5)

    # Mock Cosmos DB structure
    mock_db = MagicMock()
    mock_db.get_container_client.return_value = mock_container
    mock_client.get_database_client.return_value = mock_db
    mock_cosmos.return_value = mock_client

    # Run function
    response = main.http_trigger(mock_req_get)

    # Validate
    assert response.status_code == 200
    data = json.loads(response.get_body())
    assert data["count"] == 5


@patch("counter_function_app.main.CosmosClient")
def test_post_request_increments_count(mock_cosmos, mock_req_post):
    """Test POST request increments visitor count."""
    mock_client = MagicMock()
    mock_container = make_mock_container(2)

    mock_db = MagicMock()
    mock_db.get_container_client.return_value = mock_container
    mock_client.get_database_client.return_value = mock_db
    mock_cosmos.return_value = mock_client

    response = main.http_trigger(mock_req_post)

    # Assertions
    assert response.status_code == 200
    data = json.loads(response.get_body())
    assert data["new_count"] == 3
    mock_container.replace_item.assert_called_once()


@patch("counter_function_app.main.CosmosClient")
def test_missing_env_vars_returns_500(mock_cosmos, mock_req_get, monkeypatch):
    """Test when environment variables are missing."""
    monkeypatch.delenv("COSMOS_DB_URL", raising=False)
    monkeypatch.delenv("COSMOS_DB_KEY", raising=False)

    response = main.http_trigger(mock_req_get)
    assert response.status_code == 500
    data = json.loads(response.get_body())
    assert "Missing Cosmos DB URL or key" in data["error"]
