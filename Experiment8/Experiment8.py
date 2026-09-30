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