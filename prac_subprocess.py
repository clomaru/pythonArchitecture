# # effective python p.118
# http://myenigma.hatenablog.com/entry/2016/04/09/184215
#########
#
# subprocess
#
#########
import subprocess
import time
from time import sleep
import matplotlib.pyplot as plt

proc_list = []
proc_com_list = []
def test(param, epoch):
    start = time.time()
    procs = []
    for _ in range(epoch):
        # subprocessを使うことで、コマンドラインツールを複数並列実行させることができる
        # つまり、subprocessによって複数の子プロセスを起動することができ、それらの子プロセスは並列に実行される
        proc = subprocess.Popen(['sleep', str(1)])
        procs.append(proc)

    for proc in procs:

        if param == 0:
            # またない 非同期 速い
            proc
        elif param == 1:
            # まつ 同期 遅い
            # これでも本来は10秒かかるはずなので自動的に並列的にコマンドが実行されている
            proc.communicate()

    end = time.time()

    latency = end - start

    if param == 0:
        proc_list.append(latency)
    elif param == 1:
        proc_com_list.append(latency)

    name = lambda param: "proc            " if param == 0 else "proc.communicate"
    print('{} : finished in {} seconds'.format(name(param), latency))

# for i in range(1, 10):
#     test(0, i * 10)
#     test(1, i * 10)

test(0, 506)


# plt.plot(proc_list, 'o-', label="proc")
# plt.plot(proc_com_list, 'k-', label="proc.communicate")
# plt.legend(loc="upper left")
# plt.xlabel('epoch')
# plt.ylabel('time')
# plt.show()

# #########
# #
# # concurrent.futures
# #
# #########
# import concurrent.futures
# import time
#p
# def Calc(number):
#     #何か重い処理
#     time.sleep(1)
#
# numbers=[14,60,900,30,30]
# start = time.time()
#
# #multi process
# '''
# 並列処理させる
# max_workersは同時並行に処理するプロセスの数
# このモジュールはマルチプロセスで処理をしたあと、それぞれのプロセスのデータをプロセス間通信で、データのやり取りをする
# なので、処理のオーバーヘッドが多く、あまりワーカーを増やしすぎても処理性能はあまり上がらないことも多い
# '''
# pool=concurrent.futures.ProcessPoolExecutor(max_workers=2)
# result=list(pool.map(Calc,numbers))
#
# # single process
# # result=list(map(Calc,numbers))
#
# end = time.time()
# print('%.3f' %(end-start))

# #########
# #
# # Queue
# #
# #########
# # マルチプロセスで別々に処理し、処理とその次の処理にプロセス間でデータを送ることができる
# # effective python p.132
# import time
# import multiprocessing
#
# q12 = multiprocessing.Queue()
# q23 = multiprocessing.Queue()
#
# def Calc1(number):
#     time.sleep(1)
#     q12.put(number) # putでデータを追加
#
# def Calc2(number):
#     data=q12.get() # getでデータを受信
#     time.sleep(2)
#     q23.put(data)
#
# def Calc3(number):
#     data=q23.get()
#     time.sleep(1)
#     print("result"+str(data))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(10):
#         p1 = multiprocessing.Process(target=Calc1, args=(i,))
#         p1.start()
#         p2 = multiprocessing.Process(target=Calc2, args=(1,))
#         p2.start()
#         p3 = multiprocessing.Process(target=Calc3, args=(1,))
#         p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     end = time.time()
#     print('%.3f' %(end-start))
