x = input('number_1: ')
y = input('number_2: ')

try:
    z = int(x) / int(y)
except Exception as e:
    z = None
    print("exception :", e)

print("result {}".format(z))
