thisdict = {
    "title" : "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year_published": "1955"
}

thisdict["genre"] = "fantasy"
print(thisdict)

thisdict["year_published"] = "1954"
print(thisdict)

thisdict.pop("author")
print(thisdict)

print("1) print all the keys\n2) print all the values\n3) print all the keys and values.")

scelta = input("Insert 1, 2, 3 for your choice: ")
if scelta == "1":
    for x in thisdict.keys():
        print(x)
elif scelta == "2":
    for x in thisdict.values():
        print(x)
elif scelta == "3":
    for x, y in thisdict.items():
        print(x, y)
else:
    print("Error")
