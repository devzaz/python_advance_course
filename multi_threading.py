import time
import threading

def cal_squre(numbers):
    print("calculating square of give numbers")
    for number in numbers:
        time.sleep(0.2)
        print("Squre: ", number*number)


def cal_cube(numbers):
    print("calculating cube of give numbers")
    for number in numbers:
        time.sleep(0.2)
        print("Cube: ", number*number*number)

arr = [2,4,8,9]

t = time.time()
# cal_squre(arr)
# cal_cube(arr)

t1 = threading.Thread(target=cal_squre, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in ",time.time()-t)

