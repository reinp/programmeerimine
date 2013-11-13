import math
print "Arvuta x kui teada on a,b,c,d"
a= 10
b= -1
c= 0
d= 0
p= -b/(3.0*a)
q= (p**3)+(b*c-3*a*d)/(6*a*a)
r= c/(3*a)


x= (q +(q**2+(r-p**2)**3.0)**(1/2.0))**(1/3.0) + (q-(q**2+(r-p**2)**3.0)**(1/2.0))**(1/3.0) + p

print "x={}".format(x)
print "p={}".format(p)
print "q={}".format(q)
print "r={}".format(r)
