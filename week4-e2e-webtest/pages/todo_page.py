"""Page Object Model for Playwright TodoMVC demo (sync API)."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

TODOMVC_URL = "https://demo.playwright.dev/todomvc/"

# Centralized list selectors (hash route + completion class)
TODO_ITEM = '[data-testid="todo-item"]'
TODO_ITEM_ACTIVE = f'{TODO_ITEM}:not(.completed)'
TODO_ITEM_COMPLETED = f"{TODO_ITEM}.completed"


class TodoPage:
    """Encapsulates locators and user actions for https://demo.playwright.dev/todomvc/."""

    def __init__(self, page: Page) -> None:
        self._page = page

    @property
    def page(self) -> Page:
        return self._page

    def _new_todo_input(self) -> Locator:
        return self._page.get_by_placeholder("What needs to be done?")

    def _todo_row(self, title: str) -> Locator:
        return self._page.get_by_test_id("todo-item").filter(
            has=self._page.get_by_test_id("todo-title").get_by_text(title, exact=True)
        )

    def todo_item_for(self, title: str) -> Locator:
        """The list row ``<li>`` that displays the given task title."""
        return self._todo_row(title)

    def todo_title_label(self, title: str) -> Locator:
        """Visible title label inside the row for ``title`` (scoped, stable for assertions)."""
        return self.todo_item_for(title).get_by_test_id("todo-title")

    @property
    def active_todo_items(self) -> Locator:
        """Todo rows that are not completed (DOM may reflect ``#/active`` or ``#/``)."""
        return self._page.locator(TODO_ITEM_ACTIVE)

    @property
    def completed_todo_items(self) -> Locator:
        """Todo rows marked completed (DOM may reflect ``#/completed`` or ``#/``)."""
        return self._page.locator(TODO_ITEM_COMPLETED)

    # --- Navigation / lifecycle ---

    def open(self) -> None:
        """Open the TodoMVC app."""
        self._page.goto(TODOMVC_URL)

    # --- Task input ---

    def add_task(self, title: str) -> None:
        """Submit a new task from the main input (Enter)."""
        entry = self._new_todo_input()
        entry.fill(title)
        entry.press("Enter")

    def submit_empty_task(self) -> None:
        """Submit the new-todo field with no title (should not create a row)."""
        entry = self._new_todo_input()
        entry.fill("")
        entry.press("Enter")

    def submit_whitespace_only_task(self, whitespace: str = "   \t  ") -> None:
        """Submit the new-todo field with only whitespace (trimmed to empty by the app)."""
        entry = self._new_todo_input()
        entry.fill(whitespace)
        entry.press("Enter")

    # --- List interactions ---

    def toggle_task_by_title(self, title: str) -> None:
        """Toggle completion for the task whose visible label matches ``title``."""
        self.todo_item_for(title).get_by_role("checkbox", name="Toggle Todo").click()

    def delete_task_by_title(self, title: str) -> None:
        """Remove a task using its destroy control (requires hover to reveal)."""
        row = self.todo_item_for(title)
        row.hover()
        row.get_by_role("button", name="Delete").click()

    def edit_task_title(self, old_title: str, new_title: str) -> None:
        """Enter edit mode, change text, commit with Enter."""
        row = self.todo_item_for(old_title)
        row.get_by_test_id("todo-title").dblclick()
        editor = row.locator("input.edit")
        editor.wait_for(state="visible")
        editor.fill(new_title)
        editor.press("Enter")

    # --- Footer: filters ---

    def filter_all(self) -> None:
        """Select the All filter."""
        self._page.get_by_role("link", name="All").click()

    def filter_active(self) -> None:
        """Select the Active filter."""
        self._page.get_by_role("link", name="Active").click()

    def filter_completed(self) -> None:
        """Select the Completed filter."""
        self._page.get_by_role("link", name="Completed").click()

    # --- Footer: bulk actions ---

    def clear_completed(self) -> None:
        """Click Clear completed when present."""
        self._page.get_by_role("button", name="Clear completed").click()

    # --- Read helpers ---

    def items_left_count(self) -> int:
        """Parse the numeric value from the 'N item(s) left' counter."""
        raw = self._page.get_by_test_id("todo-count").locator("strong").inner_text()
        return int(raw.strip())

    def list_titles(self) -> list[str]:
        """Return task titles for the current hash route.

        On ``#/active`` the app drops completed rows from the DOM; on
        ``#/completed`` it drops active rows. On ``#/`` every row is present.
        """
        url = self._page.url
        if "#/active" in url:
            return self.active_todo_items.get_by_test_id("todo-title").all_inner_texts()
        if "#/completed" in url:
            return self.completed_todo_items.get_by_test_id("todo-title").all_inner_texts()
        return self._page.get_by_test_id("todo-title").all_inner_texts()

    # --- Locators for assertions ---

    @property
    def todo_items(self) -> Locator:
        return self._page.get_by_test_id("todo-item")

    @property
    def main_section(self) -> Locator:
        return self._page.locator("section.main")

    @property
    def app_footer(self) -> Locator:
        return self._page.locator("footer.footer")

    @property
    def todo_count(self) -> Locator:
        return self._page.get_by_test_id("todo-count")

    def clear_completed_button(self) -> Locator:
        return self._page.get_by_role("button", name="Clear completed")
