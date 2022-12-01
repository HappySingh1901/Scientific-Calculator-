def m():
    print("\n")
    print("*"*209)

    print("""
          
                                                      #######                    #####                     ######               ##            ##            ######                                ####              ###### 
                                                    ##########            ########                ########             ##            ##         ########                             ##  ##           ########
                                                  ##                              ##           ##             ##             ##          ##             ##        ##          ##                           ##   ##         ##              ##
                                                  ##                              ##           ##           ##                 ##        ##             ##        ##          ##                                   ##        ##              ##
                                                  ##        #####           #########           ##                 ##        ##              ##        ########             #####           ##         ##              ##
                                                  ##             ###          ##       ##                 ##              ##          ##             ##        ##                                                ##         ##              ##
                                                   ##########           ##         ##                 ########               ########           ##                                                ##           ########
                                                       ######                ##            ##                ######                   ######             ##                                                ##               #####
                                                                                              """)

    print("*"*209)

import math

sub=0
add=0
mul=1

ch=0
while ch !=5:
    m()
    print("*"*88+"SCIENTIFIC CALCULATOR"+"*"*89)
    print("*"*209)
    print("\n")
    print("1.Elementary Functions(+,-,*,/,%)","2.Exponential Function(sqrt,^,!)","3.Trigonometric Functions(Sin,Cos,Tan)","4.Transformation(Degree-Radians,Radians-Degrees)","5.Exit",sep="\n\n")
    try:
        print("\n")
        ch=int(input("Enter Choice of Function to be Performed: "))
        print("\n")
    except:
        pass
    #Elementary Functions(+,-,*,/,%)
    if ch==1:
        ch=0
        while ch!=6:
            print("1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Mod","6.Main Menu",sep="\n")
            try :
                print("\n")
                ch=int(input("Enter Choice of Function to be Performed: "))
                print("\n")
            except:
                pass
            # 1.Addition
            if ch==1:
                n=int(input("Enter the number of values to be entered for addition : "))
                for i in range(0,n):
                    n1=float(input("Enter the number: "))
                    add=add+n1
                print("The addition of ",n,"digits is",'%.2f'%add,"\n")
                

            #2.Subtraction
            elif ch==2:
                n1 = float(input("Enter the number: "))
                n2 = float(input("Enter the number:"))
                sub =n1 - n2
                print("\n")
                print("The subtraction of ", n1,"and",n2,"is", '%.2f' % sub,"\n")
                    
                
                    

            #3.Multiplication    
            elif ch==3:
                n=int(input("Enter the number of values to be entered for multiplication : "))
                print("\n")
                for i in range(0,n):
                    n1=float(input("Enter the number: "))
                    mul=mul*n1
                    print("\n")
                print("The multiplication of ",n,"digits is",'%.2f'%mul,"\n")



            #4.Division
            elif ch==4:     
                n1=float(input("Enter the dividend: "))
                n2=float(input("Enter the divisor: "))
                div=n1/n2
                print("\n")
                print("The quotient of division is",'%.2f'%div,"\n")



            #5.Mod 
            elif ch==5:
                n1=int(input("Enter the number1: "))
                n2=int(input("Enter the number2: "))
                modv=n1%n2
                print("\n")
                print("The valiue of",n1,"mod (%)",n2,"is",'%.0f'%modv,"\n")
            elif ch!=6:
                print("enter your choice btw 1-6")



    #Exponential Function(sqrt,^,!)
    elif ch==2:
        ch=0
        while ch!=4:
            print("1.SquareRoot","2.Exponent","3.Factorial","4.Main Menu",sep="\n")
            try:
                ch=int(input("enetr your choice::>>"))
            except:
                pass
            #6.SquareRoot 
            if ch==1:
                n1=float(input("Enter the number"))
                sqrt=math.sqrt(n1)
                print("\n")
                print("The square root of",n1,"is",'%.2f'%sqrt,"\n")



            #7.Exponent
            elif ch==2:
                n1=float(input("Enter the base: "))
                n2=float(input("Enter the exponent:"))
                exp=math.pow(n1,n2)
                print("\n")
                print("The exponent of  base",n1,"and power",n2,"is",exp,"\n")



            #8.Factorial
            elif ch==3:
                n=int(input("Enter the Number: "))
                fact=(math.factorial(n))
                print("\n")
                print("The factorial of",n,"is",fact,"\n")
            elif ch!=4:
                print("enter your choice btw 1-4 only")

    
     #Trigonometric Functions(Sin,Cos,Tan)
    elif ch==3:
        ch=0
        while ch!=4:
            print("1.Sine","2.Cosine","3.Tangent","4.Main Menu",sep="\n")
            try:
                ch=int(input("enetr your choice::>>"))
            except:
                pass
             #9.Sine
            if ch==1:
                rad=int(input("Enter the radians: "))
                s=math.sin(rad)
                print("\n")
                print("The Sine of",rad,"is",s,"\n")



            #10.Cosine
            elif ch==2:
                rad=int(input("Enter the radians: "))
                c=math.cos(rad)
                print("\n")
                print("The Cosine of",rad,"is",c,"\n")



            #11.Tangent
            elif ch==3:
                rad=int(input("Enter the radians: "))
                t=math.tan(rad)
                print("\n")
                print("The Tangent of",rad,"is",t,"\n")

            elif ch!=4:
                print("enter your choice btw 1-4 only")

    #Transformation(Degree-Radians,Radians-Degrees)
    elif ch==4:
        ch=0
        while ch!=3:
            print("1.Degree to Radians","2.Radians to Degrees","3.Main Menu",sep="\n")
            try:
                ch=int(input("enetr your choice::>>"))
            except:
                pass
            #12.Degree to Radians
            if ch==1:
                deg=int(input("Enter the degrees to convert into radians: "))
                rad=math.radians(deg)
                print("\n")
                print("The value of",deg,"degrees in radians is",'%.2f'%rad,"\n")




            #13.Radians to Degrees        
            elif ch==2:
                rad=int(input("Enter the radians to convert into degrees: "))
                deg=math.degrees(rad)
                print("\n")
                print("The value of",rad,"radians in degree is",'%.2f'%deg,"\n")
            elif ch!=3:
                print("enetr your choice btw 1-3 only")


    elif ch==5:
            print("*"*209)

            print("*******************************************************************THANK YOU FOR USING OUR SCIENTIFIC CALCULATOR*********************************************************")
            print("********THIS CALCULATOR WAS GENERATED BY THE COLABORATION OF RAVI MAURYA(12212181) , HAPPY SINGH(12212159) AND MAHEK(12212106).*********")
            print("*"*209)
    else:
        print("PLEASE ENTER YOUR CHOICE BETWEEN 1 TO 5 ONLY ")
        a=input("PRESS ENTER TO MOVE ON")




