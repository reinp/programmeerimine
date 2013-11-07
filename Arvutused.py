import math

# Risttahukas
print "Risttahukas"
a = 10
b = 20
c = 30
servad= 4 * (a+b+c)
print "servad={}".format(servad)
pindala= 2 * (a*b + b*c + a*c)
print "pindala={}".format(pindala)
ruumala= a * b * c
print "ruumala={}".format(ruumala)

# Pyramiid
print "Pyramiid"
a = 15
h = 20
c = math.sqrt (2*a*a+h*h)
m = math.sqrt (h*h+a/2*a/2)
servad= 4*a*c
print "servad={}".format(servad)
Sp = a*a
Sk= Sp*m/2
pindala= Sp + Sk
print "Sp={}".format(Sp)
St= Sp + Sk
print "pindala{}".format(pindala)
ruumala= Sp*h/3
print "ruumala={}".format(ruumala)

# Silinder
print "Silinder"
r= 10
h= 20


