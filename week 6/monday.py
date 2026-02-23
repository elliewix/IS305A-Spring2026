import random
# rand = random.randint(0, 10)
random.seed(10)
run_count = 0
while True:
    rand = random.randint(0, 10)
    # print(rand, "I won't stop")
    run_count += 1
    if rand == 2:
        break
# print(run_count)

# a more traditional while loop

# word = "hello"
# i = 0
# vowel = False
# while i < len(word):
#     print(word[i])
#     i += 1

## what if we have vowels?

word = "coolio"
i = 0
vowel = False
while i < len(word):
    print(word[i])
    if not (word[i] in "aeiou"): # not vowels
        i += 1
    elif vowel:
        i += 1
        vowel = False
    else: # vowel condition
        # do nothing with i
        vowel = True

## a more traditional sentinel

text = "hello I am text for you"
# print(text.index('x'))
i = 0
searching = True
while i < len(text):
    character = text[i]
    if character == 'x':
        searching = False
        # print("found x at ", i)
    i += 1

i = 0
text = "no special character here"
searching = True
while searching and (i < len(text)):
    character = text[i]
    if character == 'x':
        searching = False
        print("found x at ", i)
    i += 1

## raffle simulator

# so we have a 3% chance of something happening
random.seed()
print(random.random())

def determine_wins(chance):
    # big win is 1/463
    # small win 1/32
    if chance <= (1/463):
        return 100
    elif chance <= (1/32):
        return 10
    else:
        return 0

num_plays_needed = []
for run_num in range(10000):
    bank = 0
    plays = 0
    while bank <= 0: # while in the red
        bank -= .5 # subtract our play cost
        prob = random.random()
        result = determine_wins(prob)
        bank += result # add any winnings
        plays += 1
        # print(bank, plays)
    num_plays_needed.append(plays)

print(sum(num_plays_needed) / len(num_plays_needed))