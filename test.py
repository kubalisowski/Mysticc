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
# class Test():
#     def __init__(self, prop1, prop2, prop3):
#         self.prop1 = prop1
#         self.prop2 = prop2
#         self.prop3 = prop3

# test = Test(123, "value", 3.14)

# from database._db import session
# # from database.model.world_object import WorldObject
# from service.util_service import *
# import _config

# props = get_props(_config)
# for k,v in props.items():
#     print(type(props))
from apscheduler.schedulers.background import BackgroundScheduler
from test2 import *
movement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def output():
    print(movement)


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(move_objects, 'interval', args=[movement], seconds=1, id="move_objects")
scheduler.add_job(output, 'interval', seconds=1, id="output")
scheduler.start()

while True:
    pass



