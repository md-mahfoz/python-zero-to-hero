# Tax + Discount Calculation
Price = float(input("Enter The Price: "))
Quantity = float(input("Enter The Quantity: "))
Discount_Rate = float(input("Enter The Discount Rate (%): "))
Tax_Rate = float(input("Enter The Tax Rate: (%): "))
# First Subtotal Calculation
total = Price * Quantity 
after_discount = total - (total * Discount_Rate /100 )
after_tax = after_discount + (after_discount * Tax_Rate /100)

print(f"The Subtotal Prize :{after_tax} ")