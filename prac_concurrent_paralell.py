# https://qiita.com/castaneai/items/9cc33817419896667f34
import time
import threading
import concurrent.futures
import asyncio

def func1(epoch):
    for i in range(epoch):
        print(f"{i}:aaaaa")
        time.sleep(3)


def func2():
    for i in range(epoch):
        print(f"{i}:bbbbb")
        time.sleep(3)


#####################
#
# Thread
#
#####################

def myThread():

    print('===============')
    print('Thread')
    print('===============')
    start = time.time()

    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)

    thread_1.start()
    thread_2.start()



#####################
#
# concurrent.futures.ThreadPoolExecutor
#
#####################

def myThreadPool():

    print('===============')
    print('concurrent.futures.ThreadPoolExecutor')
    print('===============')
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    executor.submit(func1)
    executor.submit(func2)



#####################
#
# concurrent.futures.ProcessPoolExecutor
#
#####################

def myProcessPool():

    print('===============')
    print('concurrent.futures.ProcessPoolExecutor')
    print('===============')
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor.submit(func1)
    executor.submit(func2)




#####################
#
# asyincio
#
#####################

def myAsyncio():

    print('===============')
    print('asyncio')
    print('===============')

    @asyncio.coroutine
    def func1():
        for i in range(epoch):
            print(f"{i}:aaaaa")
            yield from asyncio.sleep(epoch)


    @asyncio.coroutine
    def func2():
        for i in range(epoch):
            print(f"{i}:bbbbb")
            yield from asyncio.sleep(epoch)

    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([func1(), func2()])
    loop.run_until_complete(tasks)




#####################
#
# 実行
#
#####################

epoch = 3

myThread()
# myThreadPool()
# myProcessPool()
# myAsyncio()



#####################
#
# 実行結果
#
#####################

# epoch = 3

# Thread
#===============
# real	0m9.231s
# user	0m0.150s
# sys	0m0.059s

# concurrent.futures.ThreadPoolExecutor
# ===============
# real	0m9.328s
# user	0m0.183s
# sys	0m0.077s

# concurrent.futures.ProcessPoolExecutor
# ===============
# real	0m9.245s
# user	0m0.167s
# sys	0m0.077s

# asyncio
# ===============
# real	0m9.229s
# user	0m0.150s
# sys	0m0.058s
