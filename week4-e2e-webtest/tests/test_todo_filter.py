"""
Filter-focused E2E scenarios (extends Journey 3).
"""

from __future__ import annotations

from playwright.sync_api import expect

from pages.todo_page import TodoPage


def test_filter_all_shows_active_and_completed(todo_page: TodoPage) -> None:
    """All lists every task after visiting other filters."""
    todo_page.add_task("Open")
    todo_page.add_task("Shut")
    todo_page.toggle_task_by_title("Shut")

    todo_page.filter_completed()
    expect(todo_page.page).to_have_url("#/completed")
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_title_label("Shut")).to_have_text("Shut")
    expect(todo_page.completed_todo_items.get_by_test_id("todo-title")).to_have_text(["Shut"])

    todo_page.filter_all()
    expect(todo_page.page).to_have_url("#/")
    expect(todo_page.todo_items).to_have_count(2)
    expect(todo_page.todo_items.get_by_test_id("todo-title")).to_have_text(["Open", "Shut"])


def test_filter_active_hides_completed_tasks(todo_page: TodoPage) -> None:
    """Active filter hides completed rows."""
    todo_page.add_task("Still going")
    todo_page.add_task("Already done")
    todo_page.toggle_task_by_title("Already done")

    todo_page.filter_active()
    expect(todo_page.page).to_have_url("#/active")
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_title_label("Still going")).to_have_text("Still going")
    expect(todo_page.todo_count).to_have_text("1 item left")


def test_filter_completed_hides_active_tasks(todo_page: TodoPage) -> None:
    """Completed filter hides active rows."""
    todo_page.add_task("In progress")
    todo_page.add_task("Shipped")
    todo_page.toggle_task_by_title("Shipped")

    todo_page.filter_completed()
    expect(todo_page.page).to_have_url("#/completed")
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_title_label("Shipped")).to_have_text("Shipped")
    expect(todo_page.todo_count).to_have_text("1 item left")
