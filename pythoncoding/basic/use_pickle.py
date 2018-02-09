import pickle

d = dict(name='Bob', age=20, score=88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f1 = open('dump.txt', 'rb')
d = pickle.load(f1)
f1.close()
print(d)