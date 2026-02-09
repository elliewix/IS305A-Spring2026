list_a = ["a", "b", "c", "d"]
list_b = [1, 2, 3, 4]

# what might we do to combine these?

for letter in list_a:
    print(letter)

for num in list_b:
    print(num)

# nope, just vertically concats them
# let's try again
# lets nest the loops

for letter in list_a:
    for num in list_b:
        print(letter, num)

# nope, that made the cross product

# let's try the mutual index pattern
print(list(range(len(list_a))))
print(list(range(5))) # just to see the content

# i is fine to use when used for index pos
for i in range(len(list_a)):
    print(i, list_a[i], list_b[i])

# you can use this with enumerate
print(enumerate("cats")) # you'll see an enumerate object
print(list(enumerate("cats"))) # recast to see content

# produces tuple pairs, 0th is index and 1th is content

for pair in enumerate(list_a):
    print(pair)
# use multi value assignment to be more specific
for i, letter in enumerate(list_a):
    print(i, letter, list_b[i])

# DON'T USE THIS WE CAN DO BETTER
i = 0
while i < len(list_a):
    print(i, list_a[i], list_b[i])
    i +=1

# we could also use zip

print(zip(list_a, list_b))# makes a zip object
print(list(zip(list_a, list_b)))# recast to see
# note: you only need to recast if you want print
# all the resuls out at once
# don't need to recast if you're looping overit

for lett, num in zip(list_a, list_b):
    print(lett, num, lett * num)

# fun facts
for lett1, lett2 in zip(list_a, list_a[::-1]):
    print(lett1, lett2)

## reviewing python function syntax

"""
1. know the name
2. know the parameters
3. know the business to do
4. know what to return
"""

# make greeting function

def make_greeting(name, fact):
    # presume that name, fact are strings
    greeting = "hello " + name + " I like that you " + fact
    return greeting

print(make_greeting("phillip", "am cat"))
