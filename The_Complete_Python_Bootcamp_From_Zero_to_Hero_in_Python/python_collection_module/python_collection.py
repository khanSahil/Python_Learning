from collections import Counter


mylist = [1,1,1,2,2,3,4,5,6,6,6,6,7]
print(Counter(mylist))

charlist = ['a','b','a','a','a','b','c']
print(Counter(charlist))

strlist = ["Sahil", "Sahil", "Sahil", "Kahkeshan"]
print(Counter(strlist))

strchar = "aaaaaaaarrddeeeeeeeess"
print(Counter(strchar))

sentence = "How many times does each word show up in this sentence with a word"
print(sentence.split())
print(Counter(sentence.lower().split()))

c = Counter(mylist)
print(c.most_common())

from collections import defaultdict
d = {'a': 10}
print(d['a'])
#print(d['WRONG'])

default_d = defaultdict(lambda: 0)
default_d["correct"] = 20
print(default_d['correct'])
print(default_d['wrong'])
print(d)

from collections import namedtuple

Dog = namedtuple("Dog",['age','breed','name'])
sammy = Dog(age=5, breed = 'Husky', name = "Sam")
print(sammy)