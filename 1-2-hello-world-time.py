#Ans
#Wed Aug  9 13:28:57 2023 - start of : Frist call
#Wed Aug  9 13:28:58 2023 - end of : Frist call
#Wed Aug  9 13:28:58 2023 - start of : Second call
#Wed Aug  9 13:28:59 2023 - end of : Second call
#Define the corutine object is't asynchronous cause no task
import asyncio
import time

async def example(message):
    print (f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print (f"{time.ctime()} - end of :", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = example("Frist call")
    second_awaitable = example("Second call")
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())