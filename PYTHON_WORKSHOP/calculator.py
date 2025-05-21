a=float(input("enter the first operand:"))
b=float(input("enter the second operand:"))
operator=input("enter the operator:")
while operator!=0:
    match operator:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)        
        case '/':
            print(a/b)
        case '%':
            print(a%b)
        case '^':
            print(pow(a,b))
        case '//':
            print(a//b)
        case default:
            print("invalid operator")                    