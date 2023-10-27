from unittest.mock import patch

import pytest
from fastapi import HTTPException

from globoticket.api import get_event
from globoticket.models import DBEvent


@patch("globoticket.api.get_dbevent", return_value=DBEvent(product_code="Test"))
def test_get_event(mock_get_dbevent):
    """Return the event found in the database."""
    assert get_event(id=25, db="Fake db") is mock_get_dbevent.return_value
    mock_get_dbevent.assert_called_with(25, "Fake db")


@patch("globoticket.api.get_dbevent", return_value=None)
def test_get_event_404(_):
    """Raise HTTPException when no event is found."""
    with pytest.raises(HTTPException):
        get_event(id=0, db=None)


def test_client_get_event_1(client):
    """Call get_event using the client, retrieving event 1"""
    response = client.get("/event/1")
    assert response.status_code == 200
    assert response.json() == {
        "date": "2024-01-01",
        "id": 1,
        "price": "5.5000000000",
        "artist": "Bob Marley",
        "content": "Love the life you live. Live the life you love.",
        "image": "whalers.jpg",
        "name": "Live at the Rainbow",
    }


def test_client_get_event_404(client):
    """Call get_event using the client, with a non-existing id"""
    response = client.get("/event/100")
    assert response.status_code == 404
