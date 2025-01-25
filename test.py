import time

# start = time.monotonic()
# print(start)
# time.sleep(1.111)
# stop  = time.monotonic()
# print(stop)

# print(start < stop)
# print(stop - start)
# print(start)
# print(stop)

# my_list = [1, 2, None, 4, 5]
# result = filter(lambda x: x == None, my_list)
# print(type(result))
# print(len(list(filter(lambda x: x == None, my_list))))

# for object in result:
#     print(object)

#################
movement = [
    {"paths": [1, 2, 3]},
    {"paths": [4, 5, 6]},
]

idx_mov = 0  # First dictionary in the list
idx_dir = 1  # Second element in the "paths" list

del movement[idx_mov]["paths"][idx_dir]

print(movement)



