word = 'ProgRaMMer,rOll,burGer'
a = (word.split(","))
for i in range(len(a)):
    a[i] = a[i].capitalize()
result = ", ".join(a)
print(result)