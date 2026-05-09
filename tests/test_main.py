import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    """Test that the home page returns HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_name_in_response(client):
    """Test that the student's name is present on the page."""
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "John Raymond" in data
    assert "Alba" in data


def test_course_in_response(client):
    """Test that the course name is present on the page."""
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Bachelor of Science in Computer Science" in data


def test_school_in_response(client):
    """Test that the school name is present on the page."""
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Camarines Sur Polytechnic Colleges" in data


def test_year_level_in_response(client):
    """Test that the year level is mentioned on the page."""
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "3rd Year" in data or "3rd year" in data


def test_subject_in_response(client):
    """Test that Software Engineering 2 is mentioned on the page."""
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Software Engineering 2" in data


def test_content_type(client):
    """Test that the response content type is HTML."""
    response = client.get("/")
    assert "text/html" in response.content_type
