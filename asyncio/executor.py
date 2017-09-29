import asyncio
from concurrent.futures import ThreadPoolExecutor

print('running async test')


def say_boo():
    for i in range(10):
        print(i)


def say_baa():
    for i in range(10):
        print(i)


if __name__ == "__main__":
    executor = ThreadPoolExecutor(2)
    loop = asyncio.get_event_loop()
    boo = asyncio.ensure_future(loop.run_in_executor(executor, say_boo))
    baa = asyncio.ensure_future(loop.run_in_executor(executor, say_baa))

    loop.run_forever()