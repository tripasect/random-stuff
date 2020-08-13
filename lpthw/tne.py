f = open("draft.txt")

list = [i.strip('-\n') for i in f.readlines()]
list2 = []

for i in list:
    list2.append(i + "pasect")

for i in list2:
    print(i, end=", ")
