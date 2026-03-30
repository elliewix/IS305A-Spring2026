# let's just make a matrix

width, height = (20, 10) # 20 colums, 10 rows
matrix = []
for row_i in range(height):
    print(row_i)

# print([0] * 5)

for row_i in range(height):
    row = [0] * width
    matrix.append(row)

print(matrix)
import random
# my preferred style
for i in range(len(matrix)):
    col_choice = random.choice(range(width)) # col to change
    num_choice = random.randint(50, 100) # value to use
    matrix[i][col_choice] = num_choice

# an alternative way, not my fav

for row in matrix:
    col_choice = random.choice(range(width)) # col to change
    num_choice = random.randint(50, 100)
    row[col_choice] = num_choice
    print(id(row))
print(matrix)
print(id(matrix[2]))

twoith = matrix[2]
twoith[-1] = "HAVE A BUG"
print(matrix)
# so this can be a problem


# a quick review of some core syntax

# 1) setting list values

l = ['a', 'b', 'c', 'd']
# say we want to change 'c' to 'x'
l[2] = 'x'
print(l)

# 2) finding an index position in a list
d_pos = l.index('d') # find it
print(d_pos)
l[d_pos] = 'x' # use it to update
print(l)

# 3) finding unique values from a list
# use the set object type
print(set(l))
# uniques = set(l) # sets don't work like lists
uniques = list(set(l)) # so recast it
uniques[0] = 'y'
print(uniques)