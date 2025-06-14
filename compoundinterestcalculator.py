amount = float(input("Enter principle amount: "))
rate = float(input("Enter interest rate: "))
time = int(input("Enter time in years: "))

finalamount = amount * pow(1 + rate / 100, time)
print (f"balance after {time} year/s: is {finalamount}")
