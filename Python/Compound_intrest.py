principal = 0
time = 0
rate = 0

while True:
    principal = int(input("Enter the Amount:"))
    if principal < 0:
        print("Enter +ve Amount")
    else:
        break

while True:
    rate = float(input("Enter the intrest rate:"))
    if rate < 0:
        print("Enter either 0 or +ve intrest:")
    else:
        break

while True:
    time = int(input("Enter the time in Years:"))
    if time < 0:
        print("Enter Valid time: ")
    else:
        break

total = principal * pow((1+rate/100), time)
print(f"The Compound Interest is: {total:.2f}")