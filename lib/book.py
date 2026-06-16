#!/usr/bin/env python3

"""Book model.

Defines a `Book` class with a title and a validated `page_count`.
Includes a `turn_page()` convenience method that prints a short message.
"""

from typing import Optional, Any


class Book:
    """Representation of a book.

    Attributes:
        title (str): The book title provided at initialization.
        page_count (Optional[int]): The number of pages; must be an integer.
    """
    def __init__(self, title: str, page_count: int) -> None:
        self.title: str = title
        self._page_count: Optional[int] = None
        self.page_count = page_count

    @property
    def page_count(self) -> Optional[int]:
        return self._page_count

    @page_count.setter
    def page_count(self, value: Any) -> None:
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self) -> None:
        """Simulate turning a page by printing a short message."""
        print("Flipping the page...wow, you read fast!")