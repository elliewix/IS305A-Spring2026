print("hello from monday")

# quick review

## logic
print(True == True) ## == for equality
print(5 > 10) # false
### equality vs identity
print(5 == 5) # True
print("cat" == "cat") # True
# print("cat" is "cat") # True
print([] == []) # True
print([] is []) # False
print(id("cat"), id("cat"))

### things get weird with mutable objects
print([] == []) # True
print([] is []) # False
# print(id([]), id([]))
list_a = []
list_b = list_a # no, caution!
print(list_a, list_b)
list_a.append("cat")
print(list_a, list_b)
#### this is we don't use is

# assert statements
## allow you to put some boolean in
## and let it kill the program if it fails

example_list = [0,89,0,0,8]
# assert boolean, message
assert len(example_list) == 5
# if True: passes through
print("we're good here")
# assert len(example_list) > 5
# assert len(example_list) > 5, "length not greater than 5"
# assert len(example_list) > 5, (
#         "length was " + str(len(example_list)) + " not > 5")

# checking for data types
print(type(example_list))
print(type(print))
print(type(example_list) == list)
print(isinstance(example_list, list))

# isinstance allows multiple options
print(isinstance(5, (int, float)))
print(isinstance(5.5545, (int, float)))

# truthiness
if example_list:
    print(True, "from truthiness")
else:
    print(False)

print(example_list == True)

empty_list = []
if empty_list:
    print("True from truthiness")
else:
    print("falsy")