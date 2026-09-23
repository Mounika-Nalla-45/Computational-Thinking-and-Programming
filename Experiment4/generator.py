import time
import tracemalloc
n = 1000000
tracemalloc.start()
start = time.time()
data = [i * 2 for i in range(n)]
list_sum = sum(data)
list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
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