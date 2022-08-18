import random
import time

nums = []

def fill():
    for i in range(20):
        random_nums = random.randint(1, 30)
        nums.append(random_nums)
    # print(nums)

def how_many_times():
    fill()
    wook = {}
    for i in range(len(nums)):
        wook[nums[i]] = nums.count(nums[i])
    return wook

print(how_many_times())

time.sleep(3)