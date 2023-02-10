prime = []
for i in range(1,51):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
#print(prime)

letters= ['a', 'b', 'c', 'd']
dict = {}
n = 1
    for letter in letters:
        dict[n] = i
        n += 1
print(dict)

#Comprehension Exercise
list = []
for x in range(1,101):
    if x % 3 == 0:
        list.append("Fizz")
    elif x % 5 == 0:
        list.append("Buzz")
    elif x%3==0 and x %5==0:
        list.append("FizzBuzz")
#print(list)

my_list = ['python', 'java', 'scala', 'javascript']
for e in my_list:
    print(e)
my_iter = iter(my_list)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break

def primes_gen():
    gen = primes_gen()
    for _ in range(2,10):
        print(next(gen), end = ' ')