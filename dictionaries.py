print("containers:dictionaries")
d=dict()
d={'cat':'cute','dog':'fury'}
print("dictionary:",d)
print("is the dictionary has the key 'cat'?",'cat' in d)
d['fish']='wet'
print("after adding new entry to 'd':",d)
print("get an element monkey:",d.get('monkey','N/A'))
print("get an element fish:",d.get('fish','N/A'))
del d['fish']
print("after deleting the newly added entry from 'd':",d)
print("demo of dictionary comprehension:")
squares={x:x*x for x in range(10)}
print("squares of integers of range 10:")
for k,v in squares.items():
    print(k,":",v)
