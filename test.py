import time

# start = time.monotonic()
# time.sleep(1.111)
# stop  = time.monotonic()

# print(start < stop)
# print(stop - start)
# print(start)
# print(stop)

my_list = [1, 2, None, 4, 5]
result = filter(lambda x: x == None, my_list)
print(type(result))
print(len(list(filter(lambda x: x == None, my_list))))

for object in result:
    print(object)





