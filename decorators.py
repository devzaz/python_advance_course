import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "sec")
        return result

    return wrapper

@time_it
def cal_sqr(numbers):
    result = [i*i for i in numbers]
    return result

@time_it
def cal_cube(numbers):
    result = [i*i*i for i in numbers]
    return result


array = range(1, 100000)
out_sqr = cal_sqr(array)
out_cube = cal_cube(array)


