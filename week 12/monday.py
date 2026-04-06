import sqlite3

# create the connection object
conn = sqlite3.connect('pettigrew.db')

# create the cursor
c = conn.cursor()

# let's see the table structure
results = c.execute('SELECT name FROM '
                    'sqlite_master WHERE '
                    'type = "table";')
# gives us a readout of all the tables in the db
print(results.fetchall())

# so let's the data from that table
results = c.execute('SELECT * FROM letters;')
# print(results.fetchall())

# preview limited results

# print(results.fetchone())
# print(results.fetchmany(5))
box3 = c.execute('SELECT * FROM letters '
                 'WHERE BoxNumber = 3;')
box3letters = box3.fetchall()
print(box3letters)

headers = ['BoxNumber', 'FolderNumber',
           'Contents', 'Date']
import csv
with open('box3.csv', 'wt', encoding='utf-8',
          newline="") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(box3letters)

## let's read in a csv and load it into the db

# read in the csv

with open('box3.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(data)
c.execute('CREATE TABLE IF NOT EXISTS box3 (box text, folder text, '
          'content text, date text);')

# use executemany if you have 2D data
c.executemany('INSERT INTO box3 VALUES (?, ?, ?, ?);', data)

conn.commit()

updated = c.execute('SELECT name FROM '
                    'sqlite_master WHERE '
                    'type = "table";')

print(updated.fetchall())

print(c.execute('SELECT * FROM box3;').fetchall())
