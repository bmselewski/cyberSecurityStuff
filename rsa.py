#Brendan Selewski 11/12/2021

#sympy includes functions deal with prime numbers

from sympy import *

#getting m from user input
m = int(input("Enter a message to encrypt: "))

#generating random prime <10000 for p using sympy's randprime
p = randprime(0, 10000)
q = p

#making sure q is not the same value as p
while p==q:
    q = randprime(0, 10000)


x = p*q
phi = (p-1)*(q-1)




#Getting a coprime value e, starting at 3 and going until a coprime is found
e = 3

while phi % e == 0:
    #using sympy's next prime to find the next value of e
    e = nextprime(e)

#calculating d
k=0
d = (1+(k*phi))/e

while d % 1 !=0:
    k = k+1
    d = (1+(k*phi))/e

d = int(d)

#calculating the encrypted and decrypted message
encrypted = pow(m, e, x)
decrypted = pow(encrypted, d, x)


print("p:", p)
print("q:", q)
print("e:", e)
print("d:", d)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
