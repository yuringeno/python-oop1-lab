#!/usr/bin/env python3

#!/usr/bin/env python3
"""Coffee model.

Defines a `Coffee` class with a validated `size` and a `price`.
Includes a `tip()` method that prints a message and increases the price.
"""

from typing import Optional, Any


class Coffee:
    """Representation of a coffee order.

    Attributes:
        size (str): One of "Small", "Medium", "Large".
        price (float): Numeric price of the coffee.
    """
    def __init__(self, size: str, price: float) -> None:
        self._size: Optional[str] = None
        self.size = size
        self.price: float = price

    @property
    def size(self) -> Optional[str]:
        return self._size

    @size.setter
    def size(self, value: Any) -> None:
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
            return
        self._size = value

    def tip(self) -> None:
        """Print a tipping message and add 1 to `price`."""
        print("This coffee is great, here’s a tip!")
        try:
            self.price = self.price + 1
        except Exception:
            self.price = 1