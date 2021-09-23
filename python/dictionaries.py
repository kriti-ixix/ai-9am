d1 = {"name":"Kriti", "subject":"Python", "marks":45, True:1, False:0}
print(d1)

print(d1["name"])
print(d1[True])

d1["marks"] = 30
print(d1)

d1["gender"] = "F"
print(d1)

for x in d1.keys(): #This will return only the keys
    print(x)

for x in d1.values(): #This will return only the values
    print(x)

#Dictionary unpacking
for (x, y) in d1.items():
    print("Keys:", x)
    print("Values:", y)