data = list(range(3, 30))
print(len(data))
print(data)

# count = 1
# for num in data:
#     if count == 3:
#         print(count, num, "collect")
#         count = 0
#     else:
#         count += 1
#         print(count)

# well that didn't work well

# count = 0
# for num in data:
#     count += 1
#     if count % 3 == 0:
#         print(count, num)

#

all_groups = []
scratch = []

for i, num in enumerate(data, start=1):
    # print(i, num)
    scratch.append(num)
    if i % 3 == 0: # if div by 3
        print("collect")
        all_groups.append(scratch) # collection
        scratch = [] # and reset

# print(scratch)
# print(all_groups)

import random
random.seed(64)
data = [random.randint(0, 10) for _ in range(30)]
print(data)
# collect and reset on the 0
# but don't get an error

groups = []
scratch = []
for i, num in enumerate(data):
    if num != 0:
        scratch.append(num)
    if (i + 1) != len(data):
        current = num
        upcoming = data[i + 1]
        print(current, "next", upcoming)
        if upcoming == 0: # collect and reset
            groups.append(scratch)
            scratch = []
    else:
        print("here's our last one!", num)
        groups.append(scratch)

print(groups)