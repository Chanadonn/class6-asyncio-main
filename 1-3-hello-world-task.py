#Ans
#Wed Aug  9 13:33:15 2023 - Hello
#Wed Aug  9 13:33:16 2023 - world!
#This one have async task and delayable to be asynchronous
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified dalay (in seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = asyncio.create_task(print_after("world!", 2))
    second_awaitable = asyncio.create_task(print_after("Hello", 1))
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())