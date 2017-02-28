# Program to find hourly salary
import sys

print("hello")
hrs= raw_input("Give the number of Hours")
try:
    inp1= int(hrs)


except:
    inp=-1
    print("invalid number")
    sys.exit('error')

rate= raw_input("Give the rate")
try:
    inp2= float(rate)

except:
    inp2=-1
    print("invalid number")
    sys.exit('error')


if inp1 >= 40:
    final = 1.5*inp1*inp2
else:
    final = inp1*inp2

print final

