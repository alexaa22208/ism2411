# --- Self Assessment questions --- 

# 1) The first bug I identified was the missing colon because of the traceback. I also noticed that the total 
# was too small and was not adding up. This tells me that reading the error message is the easiest way for me to identify
# errors

# 2) The function apply_discount(price, tier) would calculate the price of an item after a certain percentage
# discount based on a customer's tier. A colleague could use this function without reading the body because the name
# and inputs is self explanatory

# 3) I used ChatGPT to help me fix the errors in my code. This helped me understand and find the errors in my code
# because I was able to learn why the errors occurred. I also tested the code to make sure that the fixes worked

# --- Exercise 1 ---

# Define calculate tax functioon

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax (250, 0.08)

print (f"Tax on $100 at 7%: ${tax1:.2f}") #7.00
print (f"Tax on $250 at 8%: ${tax2:.2f}") #20.00
print(f"Another Tax: ${calculate_tax(150,0.05):.2f}") #7.50

# --- Exercise 2 ---

def apply_discount(price,tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}:${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---
# Write it out manually first, then refactor into a function

discounted = apply_discount(200,"gold") # used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print (f"Final price: ${final_price(200,'gold',0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80,"bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")



# --- Exercise 5 -----
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total+= sale # Bug- added each sale instead of replacing the total
print(f"Total: ${total}")

count = 0
for sale in sales: # Bug- added missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Bug- changed <= to <
    print(sales[i])
    i += 1


# -- Exercise 6 ---

x = 100 # apple # Global

def double_it():
    x = 999 # local another apple (not the same apple as above)
    return x * 2

print(x) # 100
print(double_it()) # 1998
print(x) # 100
# The x inside the function is still local, so it does not change the global x