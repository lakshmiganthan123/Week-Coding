Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 

Unit                                                     Charge / Unit

Upto 199                                             @1.20

200 and above but less than 400        @1.50

400 and above but less than 600        @1.80

600 and above                                    @2.00

If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 

Sample Test Cases

Test Case 1 

Input

50 

Output

100.00 

Test Case 2

Input 

300

Output 

517.50
a=float(input())
if(a<200):
    x=a*1.20
    if(x<100):
        print("100")
    else:
        print(x)
elif(200<=a<400):
        y=a*1.50
        if(y>=400):
            print(y*15/100+y)
        else:
            print(y)
elif(400<=a<600):
        z=a*1.80
        print(z*15/100+z)
else:
        w=a*2.00
        print(w*15/100+w)
        
