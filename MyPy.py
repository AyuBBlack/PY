# data = set('Hello')
data = {1,4,5,6,7,7,5,4,3}

data.add(23)
data.update([23, 4, 6, True, "Йоу"])

new = frozenset([1,4,5,6,7,7,5,4,3,23, 4, 6, True, "Йоу"])

print(new)