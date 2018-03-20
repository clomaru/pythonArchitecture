# p.146
import time
import matplotlib.pyplot as plt

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1): # lowから0まで-1ずつ
        if a % i == 0 and b % i == 0:
            return i

numbers1    = [(1963309, 2265973)]
numbers2    = [(1963309, 2265973), (2030677, 3814172)]
numbers3    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620)]
numbers4    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086)]
numbers5    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256)]
numbers6    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755)]
numbers7    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175)]
numbers8    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175), (2897408, 3954239)]
numbers9    = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175), (2897408, 3954239), (2807038, 9397858)]
numbers10   = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175), (2897408, 3954239), (2807038, 9397858), (2302602, 2265934)]
# numbers20   = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175), (2897408, 3954239), (2807038, 9397858), (2302602, 2265934),
#                (1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2051429, 2022086), (2796292, 2355256), (1972029, 3050755), (2790710, 3103175), (2897408, 3954239), (2807038, 9397858), (2302602, 2265934)]
numbers = [numbers1,numbers2,numbers3,numbers4,numbers5,numbers6,numbers7,numbers8,numbers9,numbers10]



######################
# 普通にやる
######################
normal_result = []
print('==========================')
print('normal')
print('==========================')

for i in range(len(numbers)):
    start = time.time()
    results = list(map(gcd, numbers[i]))
    end = time.time()
    normal_result.append(end - start)
    print(f'{i+1}:took %.3f seconds' % (end - start))

# result
# 1:took 0.187 seconds
# 2:took 0.381 seconds
# 3:took 0.499 seconds
# 4:took 0.677 seconds
# 5:took 0.895 seconds
# 6:took 1.085 seconds
# 7:took 1.341 seconds
# 8:took 1.638 seconds
# 9:took 1.853 seconds
# 10:took 2.059 seconds



######################
# ThreadPoolExecutorを使う
######################
from concurrent.futures import ThreadPoolExecutor

the_list = []
print('==========================')
print('ThreadPoolExecutor')
print('==========================')

for i in range(len(numbers)):
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers[i])) # I/O?
    end = time.time()
    the_list.append(end - start)
    print(f'{i+1}:took %.3f seconds' % (end - start))

# result
# 1:took 0.163 seconds
# 2:took 0.356 seconds
# 3:took 0.484 seconds
# 4:took 0.682 seconds
# 5:took 0.865 seconds
# 6:took 1.045 seconds
# 7:took 1.308 seconds
# 8:took 1.554 seconds
# 9:took 1.789 seconds
# 10:took 2.011 seconds



######################
# ProcessPoolExecutorを使う
######################
from concurrent.futures import ProcessPoolExecutor

# max_workers = 2のとき
#=======================
ppe_list = []
print('==========================')
print('ProcessPoolExecutor max_workers=2')
print('==========================')

for i in range(len(numbers)):
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers[i]))
    end = time.time()
    ppe_list.append(end - start)
    print(f'{i+1}:took %.3f seconds' % (end - start))

# result
# 1:took 0.204 seconds
# 2:took 0.193 seconds
# 3:took 0.327 seconds
# 4:took 0.369 seconds
# 5:took 0.530 seconds
# 6:took 0.535 seconds
# 7:took 0.775 seconds
# 8:took 0.782 seconds
# 9:took 1.012 seconds
# 10:took 0.993 seconds



# max_workers = 4のとき
#=======================
ppe_list_4 = []
print('==========================')
print('ProcessPoolExecutor max_workers=4')
print('==========================')

for i in range(len(numbers)):
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=4)
    results = list(pool.map(gcd, numbers[i]))
    end = time.time()
    ppe_list_4.append(end - start)
    print(f'{i+1}:took %.3f seconds' % (end - start))

# result
# 1:took 0.210 seconds
# 2:took 0.200 seconds
# 3:took 0.276 seconds
# 4:took 0.381 seconds
# 5:took 0.580 seconds
# 6:took 0.574 seconds
# 7:took 0.752 seconds
# 8:took 0.878 seconds
# 9:took 1.058 seconds
# 10:took 1.128 seconds




######################
# 可視化
######################
plt.plot(normal_result, marker='o', color="black", label="normal")
plt.plot(the_list, marker='p', color="blue", label="ThreadPoolExecutor")
plt.plot(ppe_list, marker='*', color="red", label="ProcessPoolExecutor worker=2")
plt.plot(ppe_list_4, marker='8', color="green", label="ProcessPoolExecutor worker=4")
plt.legend(loc="upper left")
plt.xlabel('element_num')
plt.ylabel('time')
plt.show()
