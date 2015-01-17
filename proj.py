#module for repetitive project euler tasks

#product of iterable
import operator
def product(it):
    return reduce(operator.mul,it,1)


"""
Pythagorean triple generator using euclid's formula
set by m and n bounds
returns tuple
"""

def triple(m,n):
    a = m**2 - n**2
    b = 2*(m*n)
    c = m**2 + n**2
    if a**2 + b**2 == c**2 and a > 0:  
        return (a,b,c)
    

#prime num generator using sieve of eratosthenes on n chains
def prime_gen(x):
    numlist = range(3, x+1, 2)
    counter = 0 # Keeps count of index in while loop
    backup = 0 # Used to reset count after each iteration and keep count outside of while loop
    for num in numlist:
        counter = backup
        if num != 0:
            counter += num
            while counter <= len(numlist)-1: # Sifts through multiples of num, setting them all to 0
                    numlist[counter] = 0
                    counter += num
        else: # If number is 0 already, skip
            pass
        backup += 1 # Increment backup to move on to next index
    return [2] + [x for x in numlist if x]


from math import sqrt
#non-recursive fibonacci sequence generator
def fibonacci(n):
    f = []
    if n == 0 or n == 1: return 1
    for i in range(n+1):
        f.append(i)
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


#factorization
def factors(n):    
    return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

#combinatorics rectangle
#finds all rectangles in n*m grid
def comb_rect(n,m):
    return (n * (n+1) * m * (m+1))/4
