# https://qiita.com/castaneai/items/9cc33817419896667f34
import time
import threading
import concurrent.futures
import asyncio

def func1():
    for i in range(epoch):
        print(f"{i}:aaaaa")
        time.sleep(sleep_time)


def func2():
    for i in range(epoch):
        print(f"{i}:bbbbb")
        time.sleep(sleep_time)


def func3():
    for i in range(epoch):
        print(f"{i}:ccccc")
        time.sleep(sleep_time)


def func4():
    for i in range(epoch):
        print(f"{i}:ddddd")
        time.sleep(sleep_time)


def func5():
    for i in range(epoch):
        print(f"{i}:eeeee")
        time.sleep(sleep_time)


#####################
#
# normal
#
#####################
def myNormal():
    print('===============')
    print('Normal')
    print('===============')

    func1()
    func2()
    func3()
    func4()
    func5()



#####################
#
# Thread
#
#####################

def myThread():

    print('===============')
    print('Thread')
    print('===============')

    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)
    thread_3 = threading.Thread(target=func3)
    thread_4 = threading.Thread(target=func4)
    thread_5 = threading.Thread(target=func5)

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()



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
    executor.submit(func3)
    executor.submit(func4)
    executor.submit(func5)



#####################
#
# concurrent.futures.ProcessPoolExecutor
#
#####################

def myProcessPool():

    print('===============')
    print('concurrent.futures.ProcessPoolExecutor')
    print('===============')
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    executor.submit(func1)
    executor.submit(func2)
    executor.submit(func3)
    executor.submit(func4)
    executor.submit(func5)




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
            yield from asyncio.sleep(sleep_time)


    @asyncio.coroutine
    def func2():
        for i in range(epoch):
            print(f"{i}:bbbbb")
            yield from asyncio.sleep(sleep_time)


    @asyncio.coroutine
    def func3():
        for i in range(epoch):
            print(f"{i}:ccccc")
            yield from asyncio.sleep(sleep_time)


    @asyncio.coroutine
    def func4():
        for i in range(epoch):
            print(f"{i}:ddddd")
            yield from asyncio.sleep(sleep_time)


    @asyncio.coroutine
    def func5():
        for i in range(epoch):
            print(f"{i}:eeeee")
            yield from asyncio.sleep(sleep_time)


    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([func1(), func2(), func3(), func4(), func5()])
    loop.run_until_complete(tasks)




#####################
#
# 実行
#
#####################

epoch = 10
sleep_time = 2

# myNormal()
# myThread()
# myThreadPool()
# myProcessPool()
myAsyncio()



#####################
#
# 実行結果
#
#####################

# epoch = 10


# Normal
# ============
# real	1m40.345s
# user	0m0.157s
# sys	0m0.061s

# Thread
#===============
# real	0m20.341s
# user	0m0.179s
# sys	0m0.087s
# Normalのfunc数倍速くなっている

# concurrent.futures.ThreadPoolExecutor
# ===============
# real	0m20.338s
# user	0m0.184s
# sys	0m0.087s

# concurrent.futures.ProcessPoolExecutor
# ===============
# max_workers=2のとき
# real	1m0.345s
# user	0m0.189s
# sys	0m0.096s

# max_workers=4のとき
# abcd*20s + e*20s
# real	0m40.444s
# user	0m0.217s
# sys	0m0.121s

# max_workers=5のとき
# abcde * 20s
# real	0m20.298s
# user	0m0.196s
# sys	0m0.136s

# asyncio
# ===============
# real	0m20.287s
# user	0m0.183s
# sys	0m0.062s
