for x in range(0,150):
    print(x)

for x in range(5, 1000, 5):
    print(x)

def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')

min = 0
max = 500000
Odd = 0

for number in range(min, max+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Odd = Odd + number

print("The Sum from {0} to {1} = {2}".format(min, max, Odd))

def down ():
    umber = 2018
    while number > 0:
        print (number)
        number = number - 4
        
down()   

def countdown(lowNum, highNum, mult):
    for i in range (lowNum, highNum):
        if i % mult == 0:
            print (i)
            
countdown(2, 9, 3)
