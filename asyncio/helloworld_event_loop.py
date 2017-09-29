import asyncio


@asyncio.coroutine
def say(what, when):
    yield from asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()
loop.run_until_complete(say('hello world', 1))
loop.close()