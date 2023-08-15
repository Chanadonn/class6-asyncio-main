#Ans
#Wed Aug  9 13:20:37 2023 - world!
#Wed Aug  9 13:20:38 2023 - hello
#This program not asynchronous program because corutine function not task
# When do coroutines start running?
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified dalay (seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = print_after("world!", 2)
    second_awaitable = print_after("hello", 1)
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())