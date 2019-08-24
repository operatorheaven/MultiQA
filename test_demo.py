import os
import time
import random
import multiprocessing as mp

TOTAL_JOB_AMOUNT = 9
# Which would run child process of parent...
def run_child(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))
    time_start = time.time()
    # Waiting...
    time.sleep(random.random()*3.0)
    time_delta = time.time() - time_start
    print("Task %s run cost %0.2f seconds." % (name, time_delta))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    """ 
    p = mp.Process(target=run_child, args=('test',))
    print("Child process will start...")
    p.start()
    p.join()
    print("Child process end.") 
    """
    # Total 5 sub-processes: (0, 1, 2, 3, 4)
    p = mp.Pool(TOTAL_JOB_AMOUNT-1)
    for i in range(TOTAL_JOB_AMOUNT):
        p.apply_async(run_child, args=(str(i),))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')





    
    