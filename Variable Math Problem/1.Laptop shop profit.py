# Laptop shop profit variables
buy_price = 680
shipping = 35
tax_rate = 7
quantity = 24
selling_price = 899
main_price = buy_price + shipping
Tax_per_laptop = buy_price + tax_rate /100





print("Question :\n"
"buy_price = 680\n"
"shipping = 35\n"
"tax rate = 7\n"
"quantity = 24\n"
"selling_price = 899\n" 
"1.Cost of one laptop including shipping?\n"
"2.Tax on one laptop?\n"
"3.Total cost for 24 laptop?\n"
"4.Total revenue?\n"
"5.Profit per laptop?\n" \
"6.Profit percentage?")

print("1.ans:\n" \
"Each Laptop buy price including shipping price = "f" {buy_price} + {shipping}")
print("Final prize = "f"{main_price}") 

print("2.ans:\n" \
"cost before tax = "f"{buy_price} + {shipping}\n"
"                = "f"{buy_price + shipping}\n"
"tax on per laptop = "f"{main_price * tax_rate /100}")

print("3.ans:\n"
"total cost in one laptop = "f"{main_price } + 50.5\n"
"                         = "f"{main_price + 50.5}")