def Multiplication(a , b):
    Mul=int(a)*int(b)
    return Mul


def main():
    num1=input("Enter 1st number: ")
    
    
    num2=input("Enter 2nd number: ")
    
    print("Sum of ",num1,"&",num2,"is" , Multiplication(num1 , num2))

main()