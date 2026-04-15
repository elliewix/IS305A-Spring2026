from  lxml import etree

with open('hamlet-tei.xml', 'rb') as infile:
    xml = infile.read()

tree = etree.fromstring(xml)
print(tree)

for each in tree:
    print("child elem", each)

# when you see you have a namespace
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# search for all titles
# titles = tree.xpath('//title')
# oops for alias stmt
# titles = tree.xpath('', namespaces = ns)
titles = tree.xpath('//tei:title', namespaces = ns)

# print(titles)
# for t in titles:
#     print(t.xpath('text()'))

# let's be more specific

titles = tree.xpath('//tei:titleStmt/tei:title[@type = "statement"]/text()', namespaces = ns)

print(titles)

# what if we wanted to see all the types of titles?

titletypes = tree.xpath('//tei:title/@type', namespaces = ns)
print(titletypes)

# all the person standard names

names = tree.xpath('//tei:persName[@type = "standard"]/text()', namespaces = ns)
print(names)

