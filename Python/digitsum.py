inputvalue='notsuccess'
while inputvalue!='success':
    n=int(input("Enter a number : "))
    total=0
    count=0

    while(n>0):
        dig=n%10
        total=total+dig
        count=count+1
        n=n//10

    if(count==0):
        print('Please enter a positive number')
    elif(count<3 or count>3):
        print('Please enter a 3 digit number')
    else:
        inputvalue='success'
        print('The total sum of digits is : ' , total)

