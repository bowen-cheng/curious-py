from math import factorial, sqrt

# List comprehension: [expr(item) for item in iterable]
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
list_c = [len(word) for word in words]
print("[len(word) for word in words]:", list_c)

list_c2 = [len(str(factorial(x))) for x in range(0, 20)]
print("[len(str(factorial(x))) for x in range(0, 20)]", list_c2)

# Set comprehension: {expr(item) for item in iterable}
# duplicate values are omitted in sets
set_c = {len(str(factorial(x))) for x in range(0, 20)}
print("\n{len(str(factorial(x))) for x in range(0, 20)}", set_c)

# dict comprehension: {key_expr: value_expr for item in iterable}
country_to_capital = {'UK': 'London', 'China': 'Beijing', 'Japan': 'Tokyo', 'Sweden': 'Stockholm'}
# useful for looking up dict in reverse order by reversing the key value pairs
# use the dict.items() function to get keys and values
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print("\n{capital: country for country, capital in country_to_capital.items()}:", capital_to_country)

# if there are key conflicts in dict comprehension, the later keys overwrite earlier keys
words = ['hi', 'hello', 'hey', 'height', 'ocean']
dict_conflict = {word[0]: word for word in words}  # map the first letter to the word
print("{word[0]: word for word in words}", dict_conflict)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


# All comprehensions supports an additional predicate clause for filtering the source to be evaluated by expr
# E.g. for list comprehension: [expr(item) for item in iterable if predicate(item)]
predicate_c = [x for x in range(60) if is_prime(x)]
print("[x for x in range(60) if is_prime(x)]:", predicate_c)
