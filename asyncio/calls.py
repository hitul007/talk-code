import asyncio

def success(msg):
    print("Success - %s" % msg)

async def callback_example(loop):
    print('registering callbacks')
    loop.call_soon(success, "Call soon")

    loop.call_later(2, success, "Call later 2 sec")
    loop.call_later(3, success, "Call later 3 sec")

    loop.call_at(1506541660, success, "Network connect")
    loop.time()

    await asyncio.sleep(3)


loop = asyncio.get_event_loop()
loop.run_until_complete(callback_example(loop))
loop.close()
