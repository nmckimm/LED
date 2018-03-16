import pprint
import numpy as np
x = 10
y = 10
b = [[True]*x for _ in range(x)]
a = [list(range(i*x, i*x + x)) for i in range(x)]
b1 = np.array(b)
pprint=pprint.pprint
pprint(b)
# sums all True values
pprint(sum(sum(b, [])))
print(b1)
print(b1[0:4, 5:9]) #All rows, first four columns [row][col]
pprint(a)


b2 = np.copy(b1)
b2[4:6, 5:9] = False
print(b2)
#pprint(sum(b2, []))
print(np.sum(b2))

## if numarray[0] = switch 