import pprint

x = 10
y = 10
b = [[False]*x for _ in range(x)]
a = [list(range(i*x, i*x + x)) for i in range(x)]
pprint=pprint.pprint
pprint(b)
# sums all True values
pprint(sum(sum(b, [])))
