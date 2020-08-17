name = ("Darsan","Shifa","Christina","Nidhi")
place = ("Kochi","Aluva","Kasargod","tvm")

zipped = zip(name,place)
for (a,b) in zipped:
    print (a,b)
zipped2 = list(zip(name,place)) #can also use set, but it will show only unique values
print(zipped2)