from multiprocessing import cpu_count
from multiprocessing import Pool
import numpy as np
import sys
import time 

def f(a):
    x = np.arange(0, 1e7, 1) * a
    return x*x

if __name__ == '__main__':
    core = cpu_count()
    print("cores = %d"%core)
    # print("version ", sys.version)

    a = range(1, 8 + 1)
    print(len(a))

    ta1 = time.time()
    with Pool(1) as pool1:
        b = pool1.map(f,a)
    tb1 = time.time()


    ta2 = time.time()
    with Pool() as pool2:
        b = pool2.map(f,a)
    tb2 = time.time()

    print("One core costs %4.2fs"%(tb1 - ta1))
    print("Multi cores cost %4.2fs"%(tb2 - ta2))

    with open("cost.txt", 'w') as f:
        print("One core costs %4.2fs"%(tb1 - ta1), file = f)
        print("Multi cores cost %4.2fs"%(tb2 - ta2) , file = f)



