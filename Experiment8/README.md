#  8. Asynchronous Web Crawler

## Question

Develop an asynchronous web crawler using `asyncio` and `aiohttp` and compare it against a sequential implementation.

### Aim

To compare sequential and asynchronous web crawling using Python.

### Algorithm

1. Create a list of URLs.
2. Fetch URLs one by one using the sequential method.
3. Fetch multiple URLs concurrently using `asyncio`.
4. Use `aiohttp` for asynchronous requests.
5. Record the execution time.
6. Compare both times.

### Program

```python
import asyncio
import aiohttp
import time
import requests

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

# Sequential crawler
def sequential():
    start = time.time()

    for url in urls:
        requests.get(url)
        print("Fetched:", url)

    return time.time() - start


# Asynchronous crawler
async def fetch(session, url):
    async with session.get(url) as response:
        await response.text()
        print("Fetched:", url)


async def asynchronous():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

    return time.time() - start


seq_time = sequential()

async_time = asyncio.run(
    asynchronous()
)

print("\nSequential Time:",
      round(seq_time, 2), "seconds")

print("Async Time:",
      round(async_time, 2), "seconds")
```

### Input

```text
https://example.com
https://example.org
https://example.net
```

### Output

```text
Fetched: https://example.com
Fetched: https://example.org
Fetched: https://example.net

Fetched: https://example.com
Fetched: https://example.org
Fetched: https://example.net

Sequential Time: 1.85 seconds
Async Time: 0.72 seconds
```

> The execution time may be different depending on the internet connection and computer.

### Inference

* Sequential method fetches one URL at a time.
* Asynchronous method fetches multiple URLs concurrently.
* Async crawling can reduce waiting time.

### Analysis

* `asyncio` manages asynchronous tasks.
* `aiohttp` sends asynchronous HTTP requests.
* `asyncio.gather()` runs multiple tasks concurrently.
* Async programming is useful for web crawling.

### Result

The asynchronous web crawler was successfully developed and compared with the sequential implementation.
