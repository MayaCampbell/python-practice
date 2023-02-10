#for all numbers inclusive 1-50 give a list og all the prime numbers
# prime= [for num,num2 in range (1,51)]

def prime_function(num,num2)

prime = []

for i in range (1,51):
    for j in range (2,i):
        if i%j == 0:
            break
        else:
            prime.append(i)