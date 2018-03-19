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
            # これでも本来はeopch秒かかるはずなので自動的に並列的にコマンドが実行されている
            proc.communicate()

    end = time.time()

    latency = end - start

    if param == 0:
        proc_list.append(latency)
    elif param == 1:
        proc_com_list.append(latency)

    name = lambda param: "proc            " if param == 0 else "proc.communicate"
    print('{} : finished in {} seconds'.format(name(param), latency))

for i in range(1, 50):
    test(0, i * 10)
    test(1, i * 10)

# test(0, 504)

plt.plot(proc_list, marker='o', color="blue", label="proc")
plt.plot(proc_com_list, marker='p', color="red", label="proc.communicate")
plt.legend(loc="upper left")
plt.xlabel('epoch')
plt.ylabel('time')
plt.show()
