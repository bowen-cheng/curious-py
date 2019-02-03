# dicts (maps) are unordered mapping from unique, immutable keys to mutable values

# keys must be unique, values don't
# order of the entries is random and may change
age_dict = {
    "Bill": 23,
    "Anna": 20,
    "Jason": 15
}

# using construct function to create a dictionary from list of tuple
d_tuple = dict([('Bill', 23), ('Anna', 20), ('Jason', 15)])
print("d_tuple = dict([('Bill', 23), ('Anna', 20), ('Jason', 15)]):", d_tuple)

# copy dict
c1 = d_tuple.copy()
print("\nc1 = d_tuple.copy():", c1)
print("c1 is d_tuple:", c1 is d_tuple)
c2 = dict(d_tuple)
print("c2 = dict(d_tuple):", c2)
print("c2 is d_tuple:", c2 is d_tuple)

# update is used for merging dicts
age_dict.update({"Abby": 26})
print("\nage_dict.update({'Abby': 26}):", age_dict)

# use items function to access key values in a dict
print("\nage_dict.items():")
for key, value in age_dict.items():
    print(key, value, sep=", ")

# use in and not in to test membership
print("\n'Abby' in age_dict:", 'Abby' in age_dict)

# use del keyword to remove item from a dict
del age_dict['Abby']
print("\ndel age_dict['Abby']:", age_dict)
