"""
conftest.py
---

Fixtures for pytest.
"""
from datetime import date
from pathlib import Path
from unittest.mock import patch

import pytest
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
from starlette.testclient import TestClient

from globoticket.api import app, get_session
from globoticket.models import Base, DBCategory, DBEvent

test_db = sqlalchemy.create_engine(
    "sqlite+pysqlite:///:memory:",
    connect_args={"check_same_thread": False},
    echo=True,
)

test_sessionmaker = sessionmaker(bind=test_db)


def setup_test_db():
    """Create tables and test data in test db."""
    Base.metadata.create_all(bind=test_db)
    session = Session(test_db)
    cat = DBCategory(name="t")
    ev = DBEvent(product_code="123456", price=5.50, date=date(2024, 1, 1), category=cat)
    session.add(cat)
    session.add(ev)
    session.commit()


def get_test_session():
    """Create a db session for a single test.
    After the test: close the session and drop all tables."""
    setup_test_db()
    session = test_sessionmaker()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_db)


@pytest.fixture()
def client():
    """Create a TestClient that uses the test database."""

    # See: https://fastapi.tiangolo.com/advanced/testing-database/
    app.dependency_overrides[get_session] = get_test_session
    yield TestClient(app)
    del app.dependency_overrides[get_session]


@pytest.fixture(autouse=True, scope="session")
def test_frontmatter():
    """Override the location of frontmatter files."""
    with patch(
        "globoticket.frontmatter.FRONTMATTER_DIRECTORY",
        new=Path(__file__).parent / "product_info",
    ):
        yield
