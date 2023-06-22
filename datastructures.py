# 1. tuples
cars = ("Mercedes","R34","Pagani","Supra","GTR")
print(cars)
print(cars[2])
# cars[0] = "Mercedes Benz" this is impossible
print(cars[1:4])
print(cars[1:])
for gari in cars:
    print(gari)

# 2. Lists
colours = ["red","green","purple","blue","orange"]
print(colours)
print(colours[2])
colours[3] = "dark blue"
print(colours[1:4])
print(colours[0:])
for rangi in colours:
    print(rangi)
print(colours)
colours.reverse()
print(colours)
colours.pop[2]
print(colours)
colours.sort()
print(colours)

# 3. Dictionaries
students = {"ADM1":"Tracy","ADM2":"Moses","ADM3":"Eugene"}
print(students["ADM1"])
for funguo in students.keys():
    print(funguo)

for jina in students.values():
    print(jina)

# 4. sets
ranks = {1,2,3,4,5,7,4,6,3,5,32,2,5,6,3,6,3,8,7,7,6,8,9,11}
print(ranks)
