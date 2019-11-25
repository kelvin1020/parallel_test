from multiprocessing import cpu_count
from multiprocessing import Pool
import numpy as np
import sys
import time 

def f(x):
    return x*x

if __name__ == '__main__':
    core = cpu_count()
    print("cores = %d"%core)
    # print("version ", sys.version)

    a = np.arange(0, 5e6, 1)
    print(a)

    ta = time.time()
    with Pool(1) as pool:
        b = pool.map(f,a)
    tb = time.time()
    print("One core costs %4.2fs"%(tb - ta))


    ta = time.time()
    with Pool() as pool:
        b = pool.map(f,a)
    tb = time.time()
    print("Multi cores cost %4.2fs"%(tb - ta))



