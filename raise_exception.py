# try:
#     raise MemoryError('Memory error')

# except MemoryError as e:
#     print(e)


# own class for exception

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception:", self.msg)

    def handle(self):
        print("Accident occured so take detour")


try:
    raise Accident('Crash between two cars')

except Accident as e:
    e.handle()
