import asyncio


@asyncio.coroutine
def test(i):
    print("test_1", i)
    r = yield from asyncio.sleep(1)
    print("test_2", i)

loop = asyncio.get_event_loop()
tasks = [test(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# for 3.4
# @asyncio.coroutine把一个generator标记为coroutine类型，把这个coroutine扔到EventLoop中执行。
# test()会首先打印出test_1，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，
# 在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。


import asyncio


async def test(i):
    print("test_1", i)
    await asyncio.sleep(1)
    print("test_2", i)

loop = asyncio.get_event_loop()
tasks = [test(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close


# for 3.5