import csv
import random
zodiac = ("Rat Ox Tiger Rabbit Dr,a,gon Sn'a'ke "
          "Horse Goat Mo,nkey Rooster Dog Pig")

names = zodiac.lower().split()
rows = []
for _ in range(100):
    top3animals = random.choices(names, k = 3)
    jumble = list(random.choice(names))
    random.shuffle(jumble)
    jumble = "".join(jumble)
    row = top3animals + [jumble]
    print(row)
    rows.append(row)

# in order to creat a CSV file you need
# headers (1D list) I still need to make
# data (2D list) this is rows
headers = ['choice 1', 'choice 2', 'choice 3', 'jumble']

# now we are ready to write it out
with open('zodiacanimals.csv', 'wt', encoding='utf-8')  as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers) # singular! 1D list
    csvout.writerows(rows) # your 2d list

