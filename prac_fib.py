# https://qiita.com/castaneai/items/9cc33817419896667f34
import time
import threading
from multiprocessing import Process
import concurrent.futures
import asyncio
from queue import Queue


input_list = [33,34,35]

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)



#####################
#
# normal
#
#####################
def myNormal():
    print('===============\n Normal \n===============')

    print(list(map(fib, input_list)))



#####################
#
# Thread
#
#####################
# https://docs.python.jp/3/library/threading.html#threading.Thread

def myThread():

    print('===============\n Thread \n===============')

    thread_1 = threading.Thread(target=fib, args=(33,))
    thread_2 = threading.Thread(target=fib, args=(34,))
    thread_3 = threading.Thread(target=fib, args=(35,))

    thread_1.start()
    thread_2.start()
    thread_3.start()

#####################
#
# multiprocessing
#
#####################
def myMultiProcessing():

    print('===============\n multiprocessing \n===============')

    process_1 = Process(target=fib, args=(33,))
    process_2 = Process(target=fib, args=(34,))
    process_3 = Process(target=fib, args=(35,))

    process_1.start()
    process_2.start()
    process_3.start()



#####################
#
# concurrent.futures.ThreadPoolExecutor
#
#####################

def myThreadPool():

    print('===============\n concurrent.futures.ThreadPoolExecutor \n===============')
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    executor.submit(fib, 33)
    executor.submit(fib, 34)
    executor.submit(fib, 35)



#####################
#
# concurrent.futures.ProcessPoolExecutor
#
#####################

def myProcessPool():

    print('===============\n concurrent.futures.ProcessPoolExecutor \n===============')
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    executor.submit(fib, 33)
    executor.submit(fib, 34)
    executor.submit(fib, 35)




#####################
#
# 実行
#
#####################

epoch = 10
sleep_time = 2

# myNormal()
# myThread()
# myMultiProcessing()
# myThreadPool()
myProcessPool()
