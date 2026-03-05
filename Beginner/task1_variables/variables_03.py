# to calculate the simple interest for 3 years 
# formula for simple interest is SI = (P * R * T)/100
P=eval(input("Enter the principal amount :"))
R=eval(input("Enter the rate of interest : "))
T=3
SI=(P * R  * T)/100
print(f"simple interest for the given principal amount {P} at rate of interest {R} % for {T} years is : {SI}")