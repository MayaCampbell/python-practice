import reduce

prog_lang= [('Python', 3.8), ('Java', 13), ('JavaScript',2019), ('Scala', 2.13)]
# 1. Sort the list by each language's version in ascending order
sort_asc = sorted(prog_lang, key=lambda x: x[1], reverse=False)
print(sort_asc)

# 2. Sort the list by the length of the name of each language in descending order
sort_length = sorted(prog_lang, key=lambda x: len(x[0]), reverse=True)
print(sort_length)

# 3. Filter the list so that it only contains languages with 'a' in it
filter_a = list(filter(lambda x: "a" in x[0], prog_lang))
print(filter_a)

# 4. Filter the list so that it only containcs languages whose version is in integer form
filter_int= list(filter(lambda x: type(x[1])== int, prog_lang))
print(filter_int)
# 5. Transform the list so that it contains the tubles in the form,
# ("language in all lower case", length of the language string)
lower_length = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang))
print(lower_length)

# 6. Generate a tuple in the form 
# ("All languages seperated by commas", "All versions seperated by commas")

#tuple= list(reduce(lambda x: (",".join(x[0])), prog_lang))