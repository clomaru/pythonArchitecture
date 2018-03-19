import time

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]

start = time.time()
results = list(map(gcd, numbers))
end = time.time()
print('took %.3f seconds' % (end - start))

# start = time.time()
# pool = ThreadPoolExecutor(max_workers=2)
# results = list(pool.map(gcd, numbers))
# end = time()
# print('took %.3f seconds' % (end - start))

# start = time.time()
# pool = ProcessPoolExecutor(max_workers=2)
# results = list(pool.map(gcd, numbers))
# end = time()
# print('took %.3f seconds' % (end - start))


# ハイパフォーマンスpython p.185
# http://ningning.today/2017/02/05/python/high-performance-python/
# import asyncio
# import aiohttp
# import random
# import string
#
#
# def generate_urls(base_url, num_urls):
#     for i in range(num_urls):
#         yield base_url + "".join(random.sample(string.ascii_lowercase, 10))
#
#
# def chunked_http_client(num_chunks):
#     semaphore = asyncio.Semaphore(num_chunks)
#
#     @asyncio.coroutine
#     def http_get(url):
#         nonlocal semaphore
#         with (yield from semaphore):
#             response = yield from aiohttp.request('GET', url)
#             body = yield from response.content.read()
#             yield from response.wait_for_close()
#         return body
#     return http_get
#
#
# def run_experiment(base_url, num_iter=500):
#     urls = generate_urls(base_url, num_iter)
#     http_client = chunked_http_client(100)
#     tasks = [http_client(url) for url in urls]
#     responses_sum = 0
#     for future in asyncio.as_completed(tasks):
#         data = yield from future
#         responses_sum += len(data)
#     return responses_sum
#
# if __name__ == "__main__":
#     import time
#     loop = asyncio.get_event_loop()
#     delay = 100
#     num_iter = 500
#
#     start = time.time()
#     result = loop.run_until_complete(
#         run_experiment(
#             "http://127.0.0.1:8080/add?name=asyncio&delay={}&".format(delay),
#             num_iter))
#     end = time.time()
#     print("{} {}".format(result, end - start))
