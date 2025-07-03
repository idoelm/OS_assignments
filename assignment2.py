import time
import os
import multiprocessing

def secondFunction(num :int):
    for index in range(num):
        print(str(index))
        time.sleep(5)
    print("The PID of secondFunction: " + str(os.getpid()) + " and the PID of main: " + str(os.getppid()))

def main():
    num = 5
    print("The PID of main: " + str(os.getpid()) + " and the PID of parent: " + str(os.getppid()))
    process = multiprocessing.Process(target = secondFunction, args = (num,))
    process.start()
    print("I take a break of 7 seconds. Thanks.")
    time.sleep(7)
    print("Okay, let's continue.")
    process.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total running: " + str(end_time - start_time))