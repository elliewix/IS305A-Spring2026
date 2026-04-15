import json
import requests

r = requests.get('https://api.github.com/users/hadley/orgs')

# print(r.content)
with open('mydata.json', 'wt') as outfile:
    parsed = json.loads(r.text)
    print(parsed)
    json.dump(parsed, outfile, indent = 4)
    # outfile.write(r.json())

r.close()

years = ['2015', '2019', '2022']
for y in years:
    url = "https://whatever.com/" + y
    print(url)
    # requests stuff
    # write json file
    # close response
    # time sleep