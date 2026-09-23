## 4. List-Based vs Generator-Based Processing

### Aim

To compare list-based processing and generator-based processing for a
large dataset in terms of execution time and memory usage.

### Algorithm

1.  Create a large dataset.
2.  Process the dataset using a list.
3.  Process the same dataset using a generator.
4.  Measure execution time and memory usage.
5.  Compare the results.

### Python Program

``` python
import time
import tracemalloc

n = 1000000

# List-based processing
tracemalloc.start()
start = time.time()

data = [i * 2 for i in range(n)]
list_sum = sum(data)

list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


# Generator-based processing
tracemalloc.start()
start = time.time()

data = (i * 2 for i in range(n))
generator_sum = sum(data)

generator_time = time.time() - start
generator_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()


print("List sum:", list_sum)
print("Generator sum:", generator_sum)

print("List time:", list_time)
print("Generator time:", generator_time)

print("List memory:", list_memory)
print("Generator memory:", generator_memory)
```

### Data (Input)

``` text
Dataset size: 1,000,000 numbers
Operation: Multiply each number by 2 and calculate the sum
Methods: List and Generator
```

### Result (Output)

The exact execution time and memory usage depend on the computer.

Example format:

``` text
List sum: 999999000000
Generator sum: 999999000000

List time: [measured value]
Generator time: [measured value]

List memory: [measured value]
Generator memory: [measured value]
```

### Inference

Generators process data one element at a time and generally use less
additional memory than lists.

### Analysis

  Method      Memory Usage   Processing
  ----------- -------------- ----------------------------------
  List        Higher         Stores all elements
  Generator   Lower          Processes elements one at a time

-   List additional memory: `O(n)`.
-   Generator additional memory: `O(1)` for the generator itself.
-   Time complexity: `O(n)` for both methods.
-   Actual execution time should be measured on the target system.
