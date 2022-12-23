"Stack structure implementation"


class Stack:
    "Stack structure implementation"

    def __init__(self) -> None:
        self._stack = []
        return None

    def push(self, item):
        "Push item to stack"
        self._stack.append(item)

    def pop(self):
        "Pop item from stack"
        return self._stack.pop()

    def is_empty(self):
        "Check if stack is empty"
        return not self._stack

    def peek(self):
        "Return top item from stack"
        return self._stack[-1]

    def get_string(self):
        "Return string representation of stack"
        string_stack = ""
        for i in self._stack:
            string_stack += i
        return string_stack

    def __len__(self):
        "Return length of stack"
        return len(self._stack)

    def __str__(self):
        "Return string representation of stack"
        return str(self._stack)

    def __repr__(self):
        "Return string representation of stack"
        return str(self._stack)
