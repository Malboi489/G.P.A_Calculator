x = float(input("Coefficent of x^2: "))
x1 = float(input("Coefficent of x: "))
x2 = float(input("Number adding on: "))
vertex1 = x2
vertex2 = 0
aos1 = x1*-1
aos2 = 2*x
aos = aos1/aos2
yv = aos**2*x+x*x1+x2
print "vertex: "+str(aos)+", " + str(yv)
import random
for i in range(10):
    val1 = random.randint(-10,10)
    val2 = val1**2*x+x1*val1+x2
    print "Random point " + str(i+1) + ": "+str(val1)+", "+str(val2)
bq = input("Would u like to input an x value: ")
while bq == "yes" or bq == "Yes" or bq == "y":
    rlx = int(input("Input x value: "))
    lol = rlx**2*x+x1*rlx+x2
    print "y = " + str(lol)
    bq = input("Would u like to input an x value: ")


