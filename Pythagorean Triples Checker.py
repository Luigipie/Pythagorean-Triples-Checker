import math

print ('Do you want check a series of three numbers?')
answer = input()
if answer == 'yes':
    iteration = True
while iteration == True:
    print ('Hi,if you wanna try the program, insert a number in A minor of other two ')
    print ("Insert the value of A")
    a = input()
    print ("Insert the value of B")
    b = input()
    print ("Insert the value of C")
    c = input()
    x = pow (int(b),2)   #with this you can calculate the exponentiation for 2 of the number
    y = pow (int(c),2)   #with this you can calculate the exponentiation for 2 of the number
    z = pow (int(a),2)   #with this you can calculate the exponentiation for 2 of the number
    if int(z) == int(x) + int(y):       #this is the equation to calculate the Pythagorean triple
        print ('The value of A is ' , float(z) , 'higher of', float(x), 'and',float(y), ',Congrats, this is a Pythagorean triple!')
    else:
        print ("I'm sorry, but this isn't a  Pythagorean triple! because A is ", float (z),"while B is", float (x), 'eand C', float(y))
    print ('Do you want do another check?')   #Recursion of the loop
    answer = input ()
    if answer == 'no':
        print ('GoodBye and thank you!')
        exit ()



    

