"""Pytest configuration and shared fixtures for TodoMVC E2E tests."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from playwright.sync_api import Page

# Allow `from pages...` when running pytest from repo root or this package root.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from pages.todo_page import TODOMVC_URL, TodoPage


@pytest.fixture(scope="session")
def base_url() -> str:
    """Default URL for pytest-base-url (relative ``page.goto`` paths if used later)."""
    return TODOMVC_URL


@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    """TodoMVC home with a page object bound to the Playwright ``page``."""
    page.goto(TODOMVC_URL)
    return TodoPage(page)
