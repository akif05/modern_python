>>> from collections import defaultdict
>>> d = defaultdict(list)
>>> d['tom'].append('red')
>>> d['rachel'].append('blue')
>>> d['mettew'].append('yellow')
>>> from pprint import pprint
>>> pprint(d)
defaultdict(<class 'list'>,
            {'mettew': ['yellow'],
             'rachel': ['blue'],
             'tom': ['red']})
>>> d['raymond'].append('mac')
>>> d['rachel'].append('pc')
>>> d['raymond'].del('mac')
  File "<stdin>", line 1
    d['raymond'].del('mac')
                   ^
SyntaxError: invalid syntax
>>> del d['raymond']
>>> d['tom'].append('linux')
>>> pprint(d)
defaultdict(<class 'list'>,
            {'mettew': ['yellow'],
             'rachel': ['blue', 'pc'],
             'tom': ['red', 'linux']})
>>> d['mattew'].append('mac')
>>> pprint(d)
defaultdict(<class 'list'>,
            {'mattew': ['mac'],
             'mettew': ['yellow'],
             'rachel': ['blue', 'pc'],
             'tom': ['red', 'linux']})
>>> del d['mettew']
>>> d['mattew'].append('yellow')
>>> pprint(d)
defaultdict(<class 'list'>,
            {'mattew': ['mac', 'yellow'],
             'rachel': ['blue', 'pc'],
             'tom': ['red', 'linux']})
>>> del d['mattew']
>>> d['mattew'].append('yellow')
>>> d['mattew'].append('mac')
>>> pprint(d)
defaultdict(<class 'list'>,
            {'mattew': ['yellow', 'mac'],
             'rachel': ['blue', 'pc'],
             'tom': ['red', 'linux']})
>>> pprint(dict(d))
{'mattew': ['yellow', 'mac'], 'rachel': ['blue', 'pc'], 'tom': ['red', 'linux']}
>>> # Defalutdict can be used for groupin or for accumilation
... # or invert 1 to many mapping
... # Model one-to-many: dict(one, list_of_many)
... 
>>> e2s {
...     'one': ['uno'],
...     'two': ['dos'],
...     'three': ['tres'],
...     'free': ['libre', 'gratis'],
... }
... 
... 
>>> pprint(e2s)
{'free': ['libre', 'gratis'], 'one': ['uno'], 'three': ['tres'], 'two': ['dos']}
>>> pprint(e2s, width=40)
{'free': ['libre', 'gratis'],
 'one': ['uno'],
 'three': ['tres'],
 'two': ['dos']}

>>> s2e = defaultdict(list)
>>> for eng, spanwords in e2s.items():
...     for span in spanwords:
...             s2e[span].append(eng)
... 
>>> pprint(s2e)
defaultdict(<class 'list'>,
            {'dos': ['two'],
             'gratis': ['free'],
             'libre': ['free'],
             'tres': ['three'],
             'uno': ['one']})
>>> pprint(s2e, width=10)
defaultdict(<class 'list'>,
            {'dos': ['two'],
             'gratis': ['free'],
             'libre': ['free'],
             'tres': ['three'],
             'uno': ['one']})


>>> # Using dictionary comprehancion
... 
>>> e2s = dict(one='uno', two='dos', three='tres')
>>> {span: eng for eng, span in e2s.items()}
{'uno': 'one', 'dos': 'two', 'tres': 'three'}


>>> # Using glob module. means global wildcard expansion
>>> with open('sites.csv', encoding='utf-8') as f:
...     print(f.read())


>>> # Parsing data
... # use csv module, it is very fast running module 
... import csv
>>> with open('sites.csv', encoding='utf-8') as f:
...     for row in csv.reader(f):
...             print(row)


>>> # Tuple packing and unpacking
... t = ('Raym', 'Hitting', 54, 'python@adfa.com')
>>> type(t)
<class 'tuple'>
>>> len(t)
4
>>> fname, lname, age, email = t
>>> fname
'Raym'
>>> lname
'Hitting'
>>> email
'python@adfa.com'
>>> 
>>> names = 'raymond rachel mattew'.split()
>>> colors = 'red blue yellow'.split()
>>> cities = 'austin dalls ausetin houston chicago dallas autsitn'.split()
>>> for i in name(len(names)):
...     print(names[i].upper())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> for i in range(len(names)):
...     print(names[i].upper())
... 
RAYMOND
RACHEL
MATTEW
>>> # more elegant way is
... for name in names:
...     print(name.upper())
... 
RAYMOND
RACHEL
MATTEW
>>> # Enumerating
... 
>>> # Old stile
... for i in range(len(names)):
...     print(i+1, names[i])
... 
1 raymond
2 rachel
3 mattew
>>> 
>>> # or 
... for i, name in enumerate(names, start=1):
...     print(i, name)
... 
1 raymond
2 rachel
3 mattew
>>> colors
['red', 'blue', 'yellow']

>>> for i in range(len(colors) -1, -1, -1):
...     print(colors[i])
... 
yellow
blue
red
>>> # Bether way is 
... for color in reversed(colors):
...     print(color)
... 
yellow
blue
red
>>> names
['raymond', 'rachel', 'mattew']
>>> colors
['red', 'blue', 'yellow']
>>> n = min(len(names), len(colors))
>>> for i in range(n):
...     print(names[i], colors[i])
... 
raymond red
rachel blue
mattew yellow
>>> # Better way to do this is to use zip function
... for name, color in zip(names, colors):
...     print(name, color)
... 
raymond red
rachel blue
mattew yellow
>>> 
>>> colors
['red', 'blue', 'yellow']
>>> for color in sorted(colors):
...     print(color)
... 
blue
red
yellow
>>> # sort colors by len
>>> for color in sorted(colors, key=len):
...     print(color)
... 
red
blue
yellow
>>> cities
['austin', 'dalls', 'ausetin', 'houston', 'chicago', 'dallas', 'autsitn']
>>> # print the cities with no dublicates
... for city in set(cities):
...     print(city)
... 
dallas
houston
ausetin
austin
chicago
autsitn
dalls
>>> for city in sorted(set(cities)):
...     print(city)
... 
ausetin
austin
autsitn
chicago
dallas
dalls
houston
>>> # This is like select in mysql
... # SELECT DINSTINCT city FROM cites ORDER BY city;
>>> for city in reversed(sorted(set(cities))):
...     print(city)
... 
houston
dalls
dallas
chicago
autsitn
austin
ausetin
>>> for city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
...     print(city)
... 
(0, 'HOUSTON')
(1, 'DALLS')
(2, 'DALLAS')
(3, 'CHICAGO')
(4, 'AUTSITN')
(5, 'AUSTIN')
(6, 'AUSETIN')

>>> import collections
>>> c = collections.Counter()
>>> c['red'] += 1
>>> c
Counter({'red': 1})
>>> c['blue'] += 1
>>> c['red'] += 1
>>> c
Counter({'red': 2, 'blue': 1})
>>> c.most_common(1)
[('red', 2)]
>>> c.most_common(2)
[('red', 2), ('blue', 1)]
>>> list(c.elements())
['red', 'red', 'blue']
>>> 
>>> ## Assertion
... assert 5 + 3 == 8
>>> assert 5 + 3 == 10

>>> import csv
>>> with open('congress.csv', encoding='utf-8') as f:
...     reader = csv.reader(f)
...     ## read two lines in ones
...     vote_topic = next(reader)
...     headers = next(reader)
...     # Read whole line in varialbes
...     for person, state, district, vote, name, party in reader:
...             print(person)

# Using tuples
# This will print out like
# Senator(name='Sen. Patty Murray [D, 1993-2022]', party='Democrat', state='WA')
# The original line in csv file will look like:
# 300002,TN,,Yea,Sen. Lamar Alexander [R],Republican
import csv
from collections import namedtuple

Senator = namedtuple('Senator', ['name', 'party', 'state'])
with open('congress.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    ## read two lines in ones
    vote_topic = next(reader)
    headers = next(reader)
    # Read whole line in varialbes
    for person, state, district, vote, name, party in reader:
    	senator = Senator(name, party, state)
    	print(senator)

# We can access now the senator by different fields.

>>> senator.name
'Sen. Benjamin Sasse [R]'
>>> senator.name
'Sen. Benjamin Sasse [R]'
>>> senator.party
'Republican'
>>> senator[1]
'Republican'
>>> senator[2]
'NE'
>>> senator[0]
'Sen. Benjamin Sasse [R]'


# We are using glob to be able to use filename as wild card and loop 
# Troughout all csv files in the directory
import glob
import csv
from collections import namedtuple, defaultdict
from pprint import pprint

Senator = namedtuple('Senator', ['name', 'party', 'state'])
accumulated_record = defaultdict(list)
for filename in glob.glob('con*.csv'):
	with open(filename, encoding='utf-8') as f:
	    reader = csv.reader(f)
	    ## read two lines in ones
	    vote_topic = next(reader)
	    headers = next(reader)
	    # Read whole line in varialbes
	    for person, state, district, vote, name, party in reader:
	    	senator = Senator(name, party, state)
	    	accumulated_record[senator].append(vote)
	
	pprint(accumulated_record)


# We are using glob to be able to use filename as wild card and loop 
# Troughout all csv files in the directory
import glob
import csv
from collections import namedtuple, defaultdict
from pprint import pprint

Senator = namedtuple('Senator', ['name', 'party', 'state'])
accumulated_record = defaultdict(list)
for filename in glob.glob('congress*.csv'):
	with open(filename, encoding='utf-8') as f:
	    reader = csv.reader(f)
	    ## read two lines in ones
	    vote_topic = next(reader)
	    headers = next(reader)
	    # Read whole line in varialbes
	    for person, state, district, vote, name, party in reader:
	    	senator = Senator(name, party, state)
	    	accumulated_record[senator].append(vote)
	
	pprint(accumulated_record, width=500)


# We are using glob to be able to use filename as wild card and loop 
# Troughout all csv files in the directory
import glob
import csv
from collections import namedtuple, defaultdict
from pprint import pprint

# Creating a structure for the data
## Load votes whick were arranged by topic and accumulate votes by senator
vote_value = {'Yea': 1, 'Aye': 1 'Nay': -1, 'No': -1, 'Not Voting': 0}

Senator = namedtuple('Senator', ['name', 'party', 'state'])
accumulated_record = defaultdict(list)
for filename in glob.glob('congress*.csv'):
	with open(filename, encoding='utf-8') as f:
	    reader = csv.reader(f)
	    ## read two lines in ones
	    vote_topic = next(reader)
	    headers = next(reader)
	    # Read whole line in varialbes
	    for person, state, district, vote, name, party in reader:
	    	senator = Senator(name, party, state)
	    	accumulated_record[senator].append(vote_value[vote])
	
	pprint(accumulated_record, width=500)




