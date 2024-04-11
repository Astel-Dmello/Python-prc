d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}

x = 'b' 
y = 300  

for i, j in d1.items():
    if i == x:
        d3[i] = (j + y) 

print(d3)
