#Ans
#Wed Aug  9 13:38:46 2023 - hello
#Wed Aug  9 13:38:47 2023 - world!
import asyncio
import time

async def print_after(message, delay):
    """Print a message after the specified dalay (seconds)"""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")

async def main():
    # Use asyncio.gather to run two coroutines concurrently:
    await asyncio.gather(
        print_after("world!", 2),
        print_after("hello", 1)
    )

asyncio.run(main())