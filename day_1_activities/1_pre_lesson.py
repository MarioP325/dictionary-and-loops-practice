# this is what we will use for the video intro to dictionaries a
#dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates
capitals= {"USA": "Washington DC", "India": "New Delhi", "China": "Beinjing", "Russia": "Moscow"}
# print(capitals.get("Japan"))
# if capitals.get("Japan"):
#     print("That capital exists")
# else: 
#     print("That capital doesn't exist")
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals)
# capitals.pop # or popitem for latest entry
# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)
# values = capitals.values()
# for value in capitals.values():
#     print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
