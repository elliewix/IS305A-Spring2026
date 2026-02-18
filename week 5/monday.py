import csv

with open('hw2data.csv', 'rt', encoding='utf-8') as infile:
    csvin = csv.reader(infile)
    # print(csvin)
    headers = next(csvin)
    print(headers)
    data = [r for r in csvin]
    # print(data)

# that's kind of long, let's do it shorter

with open('hw2data.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(headers)
print(len(data))

# let's explore this * more

## you may have seen for loops like this

for _ in range(5):
    print("I did a thing")

# _ can let us make a throwaway variable name

words = ["horse", 'snake', 'dragon', 'bunny', 'rat']
current, *rest = words
print(current)
print(rest)

first, *data, last = words
print(first, last)
first, *_, last = words
print(first, last)

## you may see this in function defs

## where we might have

def dostuff(x, y, z):
    print(x)
    print(y)
    print(z)
dostuff(8,9, 10)

def dostuff(x, y, z):
    nums = [x, y, z]
    for n in nums:
        print(n)

def dostuff(*nums):
    for n in nums:
        print(n)
dostuff(1,9,8,7,6,6,5,9)

def dothat(multiply, *nums):
    for n in nums:
        print(n * multiply)
dothat(5,9,7,6,5,4,4,7,9,9,8,6)

### now let's actually read this in and work with content
with open('hw2data.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# asking for row in 2D lists
print(data[5]) # relatively easy
# asking for columns of data, not so much

## do it as a list accumulator
pokedexnums = []
for row in data:
    dex = row[0]
    # print(dex) # confirmed we've got what we want
    pokedexnums.append(dex)
print(pokedexnums)
# pro: I can mess with the content easily
# con: super long

# we don't need to mess the content, so a list comp
# is a pretty good choice here
pokedexnums = [ row[0] for row in data]
print(len(pokedexnums))
# pro: generally understandable, short
# con: don't really have access to the content to mess with

# use whichever style you are comfortable with
# don't go crazy with comprehensions

# let's look at our program together
with open('hw2data.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

pokedexnums = [r[0] for r in data]
pokemonnames = [r[1] for r in data]
for name in pokemonnames:
    # print(name, name.isalnum())
    if name.isalnum() == False:
        print(name)