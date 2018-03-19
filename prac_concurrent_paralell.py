# https://qiita.com/castaneai/items/9cc33817419896667f34

# #####################
# #
# # Thread
# #
# #####################
# import time
# import threading
#
# def func1():
#     while True:
#         print("111111")
#         time.sleep(1)
#
#
# def func2():
#     while True:
#         print("2222222")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     thread_1 = threading.Thread(target=func1)
#     thread_2 = threading.Thread(target=func2)
#
#     thread_1.start()
#     thread_2.start()

# #####################
# #
# # concurrent.futures.ThreadPoolExecutor
# #
# #####################
# import time
# import concurrent.futures
#
#
# def func1():
#     while True:
#         print("111111")
#         time.sleep(1)
#
#
# def func2():
#     while True:
#         print("2222222")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
#     executor.submit(func1)
#     executor.submit(func2)


# #####################
# #
# # concurrent.futures.ProcessPoolExecutor
# #
# #####################
#
# import time
# import concurrent.futures
#
#
# def func1():
#     while True:
#         print("111111")
#         time.sleep(1)
#
#
# def func2():
#     while True:
#         print("2222222")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
#     executor.submit(func1)
#     executor.submit(func2)
#


#####################
#
# asyincio
#
#####################
import asyncio


@asyncio.coroutine
def func1():
    while True:
        print("111111")
        yield from asyncio.sleep(1)


@asyncio.coroutine
def func2():
    while True:
        print("2222222")
        yield from asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([func1(), func2()])
    loop.run_until_complete(tasks)
