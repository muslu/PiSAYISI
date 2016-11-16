# -*- coding: utf-8 -*-

#from decimal import Decimal, getcontext

#getcontext().prec = 1000000

#print sum(1/Decimal(16)**k * 
          #(Decimal(4)/(8*k+1) - 
           #Decimal(2)/(8*k+4) - 
           #Decimal(1)/(8*k+5) -
           #Decimal(1)/(8*k+6)) for k in range(100))



import gmpy2
# See https://gmpy2.readthedocs.org/en/latest/mpfr.html
gmpy2.get_context().precision = 10000
pi = 0
for n in range(1000000):
    # Formula from http://en.wikipedia.org/wiki/Calculating_pi#Arctangent
    numer = pow(2, n + 1)
    denom = gmpy2.bincoef(n + n, n) * (n + n + 1)
    frac = gmpy2.mpq(numer, denom)
    pi += frac
    # Print every 1000 iterations
    if n % 1000 == 0:
        print(gmpy2.mpfr(pi))
