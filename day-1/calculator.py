op1=int(input("Enter first integer: "))
op2=int(input("Enter secoand integer: "))
op=str(input("Enter Operator: "))

if op=="+":
    print("Result", op1+op2)
elif op=="-":
    print("Result", op1-op2)
elif op=="*":
    print("Result", op1*op2)
elif op=="/":
    print("Result", op1/op2)
else:
    print("Operator not found")
