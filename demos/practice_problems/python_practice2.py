prog_lang = [('Python', 3.8), ('Java', 13), ('Javascript', 2019), ('Scala', 2.13)]
# 1. Sort the list by each language's version in ascending order.
sort_asc=(sorted(prog_lang, key = lambda x: x[1]))
print(sort_asc)
# 2. Sort the list by the length of the name of each language in descending order
sort_len=(sorted(prog_lang, key = lambda x: len(x[0]), reverse=True))
print(sort_len)
# 3. Filter the list so that it only contains languages with 'a' in it
filter_a = list(filter(lambda x: True if 'a' in x[0] else False, prog_lang))
print(filter_a)
# 4. Filter the list so that it only contains languages whose version is in integer form.
filter_int= list(filter(lambda x: True if isinstance(x[1], int) else False, prog_lang))
print(filter_int)
# 5. Transform the list so that it contains the tuples in the form, ["language in all lower case", length of the language string]
transform = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang))
print(transform)

# 6. Generate a tuple in the form, ["All languages seperated by commas", "All versions seperated by commas"]
