from dataclasses import dataclass
from typing import Generic, TypeVar
T = TypeVar("T")
@dataclass
class Stack(Generic[T]):
    items: list[T]
    def push(self, item: T) -> None:
        self.items.append(item)
    def pop(self) -> T:
        return self.items.pop()
@dataclass
class Queue(Generic[T]):
    items: list[T]
    def enqueue(self, item: T) -> None:
        self.items.append(item)
    def dequeue(self) -> T:
        return self.items.pop(0)
s = Stack[int]([])
s.push(10)
s.push(20)
print("Stack pop:", s.pop())
q = Queue[str]([])
q.enqueue("A")
q.enqueue("B")
print("Queue dequeue:", q.dequeue())

