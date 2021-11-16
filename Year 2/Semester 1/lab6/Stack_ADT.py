# Implementation of the Stack ADT using a Python list.
from typing import Any, MutableSequence


class Stack:
    # Creates an empty stack.
    def __init__(self, values: MutableSequence = None) -> None:
        if values is None:
            values = []
        self.items = [v for v in values]

    def __str__(self):
        s = ""
        for i in range(len(self)):
            if self.items[(len(self) - 1) - i] == self.peek():
                s += str(self.items[(len(self) - 1) - i]) + " <--top" + "\n"
            else:
                s += str(self.items[(len(self) - 1) - i]) + "\n"
        return s

    def __iter__(self) -> Any:
        return iter(self.items)

    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self) -> bool:
        return len(self) == 0

    # Returns the number of items in the stack.
    def __len__(self) -> int:
        return len(self.items)

    # Returns the top item on the stack without removing it.
    def peek(self) -> Any:
        if self.isEmpty():
            raise ValueError("Cannot peek at an empty stack")
        else:
            return self.items[-1]

    # Removes and returns the top item on the stack.
    def pop(self) -> Any:
        if self.isEmpty():
            raise ValueError("Cannot pop from an empty stack")
        else:
            return self.items.pop()

    def replace(self, value: Any, index: int = 0) -> None:
        self.items[index] = value

    # Push an item onto the top of the stack.
    def push(self, item: Any) -> None:
        self.items.append(item)
