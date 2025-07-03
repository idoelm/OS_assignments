import multiprocessing.queues
import time
import os
import multiprocessing

def secondFunction(num :int, queue_to_process: multiprocessing.Queue):
    sum = 0
    for index in range(num):
        print(str(index))
        sum += index
        time.sleep(5)
    print("The PID of secondFunction: " + str(os.getpid()) + " and the PID of main: " + str(os.getppid()))
    queue_to_process.put(sum)

def main():
    queue_to_process = multiprocessing.Queue()
    num = 5
    print("The PID of main: " + str(os.getpid()) + " and the PID of parent: " + str(os.getppid()))
    process = multiprocessing.Process(target = secondFunction, args = (num, queue_to_process))
    process.start()
    print("I take a break of 7 seconds. Thanks.")
    time.sleep(7)
    print("Okay, let's continue.")
    process.join()
    print("The sum: " + str(queue_to_process.get()))

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total running: " + str(end_time - start_time))