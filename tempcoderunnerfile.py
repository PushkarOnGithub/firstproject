import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping(args):
    i, j = args
    subprocess.run(f'ping 172.20.{i}.{j} -n 1 -w 100', shell=True, stdout=f, text=True)
    # print(i, j)
pool = ThreadPoolExecutor(max_workers=100)

with open("output.txt", 'w') as f:
    for i in range(1,256):
        for j in range(1, 256):
            print(pool.submit(ping, (i, j)).result())