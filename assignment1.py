import os
import multiprocessing

def secondFunction(num :int):
    for index in range(num):
        print(str(index))
    print("The PID of secondFunction: " + str(os.getpid()) + "and the PID of main: " + str(os.getppid()))

def main():
    num = 10
    print("The PID of main: " + str(os.getpid()) + "and the PID of parent: " + str(os.getppid()))
    process = multiprocessing.Process(target = secondFunction, args = (num,))
    process.start()
    process.join()

if __name__ == "__main__":
    main()