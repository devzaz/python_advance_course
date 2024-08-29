import time
import multiprocessing


def cal_squre(numbers):
    print("calculating square of give numbers")
    for number in numbers:
        time.sleep(5)
        print("Squre: ", number*number)


def cal_cube(numbers):
    print("calculating cube of give numbers")
    for number in numbers:
        time.sleep(5)
        print("Cube: ", number*number*number)

if __name__ == '__main__':
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=cal_squre, args=(arr,))
    p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


    print("Done")

