import random
random.randint(3,17)

min = int(raw_input('min='))
max = int(raw_input('max='))
n = int(raw_input('n='))
a = 0
summa = 0
while a < n:
        summa= summa + random.randint(min, max)
      
        a = a + 1

keskmine = float(summa) / n
print 'praktiline keskmine={:.2f}'.format(keskmine)
print "teoreetiline keskmine={:.2f}".format((max+min)/2)


        
