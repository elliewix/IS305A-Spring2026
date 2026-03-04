import random

random.seed(64)

outer_data = []
for _ in range(20):
    row = [random.randint(0,10) for _ in range(10)]
    outer_data.append(row)
print(outer_data)

# we've got 2d data
# ## let's loop over it
# for row in outer_data:
#     print(row)
#     for num in row:
#         print(num)

changethese = [1, 2, 9, 14]
# for hw3 you'll ALSO be looping over clusters
for row_index in changethese:
    print(outer_data[row_index]) # these are the rows
    # looking up a value
    changethis = outer_data[row_index][0]
    # setting values
    outer_data[row_index][2] = 9999
    outer_data[row_index][0] = changethis * 3
    print(outer_data[row_index])

print(outer_data)