
import asyncio

async def main():
    print("1")

    await test()

    print("2")

    # await result

async def test():
    print("A")
    await asyncio.sleep(1)
    print("B")

asyncio.run(main())