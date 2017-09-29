import asyncio

async def coroutine():
    print('in coroutine')
    return "OK"


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    value = event_loop.run_until_complete(coro)
    print(value)
finally:
    print('closing event loop')
    event_loop.close()
