## 3. Stack and Queue Using Type Hints and Dataclasses

### Aim

To develop a reusable Python implementation of Stack and Queue using
Type Hints and Dataclasses.

### Algorithm

#### Stack (LIFO)

1.  Create a stack using a dataclass.
2.  Add elements using `push()`.
3.  Remove the last element using `pop()`.
4.  Display the result.

#### Queue (FIFO)

1.  Create a queue using a dataclass.
2.  Add elements using `enqueue()`.
3.  Remove the first element using `dequeue()`.
4.  Display the result.

### Python Program

``` python
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


# Stack
s = Stack[int]([])
s.push(10)
s.push(20)
print("Stack pop:", s.pop())

# Queue
q = Queue[str]([])
q.enqueue("A")
q.enqueue("B")
print("Queue dequeue:", q.dequeue())
```

### Data (Input)

``` text
Stack elements: 10, 20
Queue elements: A, B
```

### Result (Output)

``` text
Stack pop: 20
Queue dequeue: A
```

### Inference

The reusable Stack and Queue classes successfully perform insertion and
deletion operations using Type Hints and Dataclasses.

### Analysis

  Operation       Time Complexity
  --------------- -----------------
  Stack push      O(1) amortized
  Stack pop       O(1)
  Queue enqueue   O(1) amortized
  Queue dequeue   O(n)

-   Space complexity: `O(n)` for storing `n` elements.
-   Type Hints improve code readability and support type checking.
-   Dataclasses reduce boilerplate code for storing data.
