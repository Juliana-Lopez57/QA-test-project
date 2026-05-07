"""
P0 critical user journeys (see ai-workflow/prompt1-scenarios.md).
"""

from __future__ import annotations

from playwright.sync_api import expect

from pages.todo_page import TodoPage


def test_journey_01_core_task_creation_and_default_state(todo_page: TodoPage) -> None:
    """Journey 1: add a new task; empty submit is ignored; list and footer update."""
    expect(todo_page.main_section).not_to_be_visible()
    expect(todo_page.app_footer).not_to_be_visible()
    expect(todo_page.todo_items).to_have_count(0)

    todo_page.submit_empty_task()
    expect(todo_page.todo_items).to_have_count(0)
    expect(todo_page.main_section).not_to_be_visible()

    title = "Buy milk"
    todo_page.add_task(title)

    expect(todo_page.main_section).to_be_visible()
    expect(todo_page.app_footer).to_be_visible()
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_title_label(title)).to_have_text(title)
    expect(todo_page.todo_count).to_have_text("1 item left")

    row = todo_page.todo_items.first
    expect(row).not_to_have_class("completed")


def test_journey_02_task_completion_and_counter_accuracy(todo_page: TodoPage) -> None:
    """Journey 2: completing tasks updates styling and the items-left counter."""
    todo_page.add_task("Alpha")
    todo_page.add_task("Bravo")
    expect(todo_page.todo_count).to_have_text("2 items left")

    todo_page.toggle_task_by_title("Alpha")
    expect(todo_page.todo_item_for("Alpha")).to_have_class("completed")
    expect(todo_page.todo_count).to_have_text("1 item left")

    todo_page.toggle_task_by_title("Alpha")
    expect(todo_page.todo_item_for("Alpha")).not_to_have_class("completed")
    expect(todo_page.todo_count).to_have_text("2 items left")


def test_journey_03_routing_and_filtering(todo_page: TodoPage) -> None:
    """Journey 3: Completed / Active / All filters show the correct task subsets.

    Go through ``#/completed`` and ``#/`` before ``#/active`` so the list DOM
    always matches the hash (visiting Active first drops completed nodes).
    """
    todo_page.add_task("Task A")
    todo_page.add_task("Task B")
    todo_page.toggle_task_by_title("Task B")

    todo_page.filter_completed()
    expect(todo_page.page).to_have_url("#/completed")
    expect(todo_page.completed_todo_items.get_by_test_id("todo-title")).to_have_text(["Task B"])

    todo_page.filter_all()
    expect(todo_page.page).to_have_url("#/")
    expect(todo_page.todo_items).to_have_count(2)
    expect(todo_page.todo_items.get_by_test_id("todo-title")).to_have_text(["Task A", "Task B"])

    todo_page.filter_active()
    expect(todo_page.page).to_have_url("#/active")
    expect(todo_page.active_todo_items.get_by_test_id("todo-title")).to_have_text(["Task A"])

    todo_page.filter_all()
    expect(todo_page.page).to_have_url("#/")
    expect(todo_page.todo_items).to_have_count(2)
    expect(todo_page.todo_items.get_by_test_id("todo-title")).to_have_text(["Task A", "Task B"])


def test_journey_04_clear_completed_destructive_action(todo_page: TodoPage) -> None:
    """Journey 4: Clear completed removes completed rows and leaves actives."""
    todo_page.add_task("Keep me")
    todo_page.add_task("Remove me")
    todo_page.toggle_task_by_title("Remove me")

    expect(todo_page.clear_completed_button()).to_be_visible()
    expect(todo_page.todo_count).to_have_text("1 item left")

    todo_page.clear_completed()

    expect(todo_page.clear_completed_button()).not_to_be_visible()
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_title_label("Keep me")).to_have_text("Keep me")
    expect(todo_page.todo_count).to_have_text("1 item left")


def test_journey_05_cannot_add_whitespace_task(todo_page: TodoPage) -> None:
    """Journey 5: whitespace-only input must not create a task; counter stays absent (empty state)."""
    expect(todo_page.todo_items).to_have_count(0)
    expect(todo_page.main_section).not_to_be_visible()
    expect(todo_page.app_footer).not_to_be_visible()

    todo_page.submit_whitespace_only_task()

    expect(todo_page.todo_items).to_have_count(0)
    expect(todo_page.main_section).not_to_be_visible()
    expect(todo_page.app_footer).not_to_be_visible()
    expect(todo_page.page.get_by_test_id("todo-count")).to_have_count(0)
