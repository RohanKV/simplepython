def biggest(a,b,c):
    if a>b and a>c:
        print ("a is greater")
    elif b>a and b>c:
        print ("b is greater")
    else:
        print (" c is greater")

def main():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = int(input("enter third number"))
    biggest(a,b,c)

main()
    
   
