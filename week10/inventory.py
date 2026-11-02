#inventory.py

#Reflection 1 : What suprised me most about how lists work in Python 
# The main thing to understand when looking at a list is they are easily editable. 
# We can edit the list by adding, removing, or changing the order of items without having to make a new list.


#Reflection 2 : A business situation where a python list would have saved me time
# I can use the Python list to keep track of product sales. This makes it much easier 
# than inputting it manually into Excel. I can use Python to generate totals and then figure out which product
# had the highest sales.

print("---Exercise 1: Build the list---")

inventory = ["pen", "notebook", "stapler","tape","marker"]
print(inventory)
print(len(inventory))


print("--- Exercsie 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory)//2
print(inventory[middle]) # middle item


print("--- Exercise 3: Slicing ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("--- Exercise 4: Modifying the list---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)

try:
    coords[0]=99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Reflection: Average List of Sales ---")
sales= [100,250,75,480,200]
total= sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discounted)

print("--- Exercise 8: Filter above a threshold")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales= []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("high sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {round(sum(high_sales) / len(high_sales), 2)}")