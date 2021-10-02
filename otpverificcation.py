import random
w = 3

def otp_verify():
    w = 3
    otp = random.normalvariate(1000,9999)
    otp = abs(otp)
    otp  = int(otp)
    print("your otp is: ",otp)
    while w!=0:
        o = int(input("Enter otp:"))
        if otp ==o:
            print("loading")
            break
        else:
            print("try again!")
            w =w-1
    if w ==0:
        print("Your faild in entering otp")
    if w!=0:
        print("your sucessfully logedin")
otp_verify()




