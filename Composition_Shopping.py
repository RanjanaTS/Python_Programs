# Function to calculate discounted price for a single item
def discounted_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

# Function to calculate total price of all discounted items
def total_price(prices, discount_percent):
    total = 0
    for price in prices:
        total += discounted_price(price, discount_percent)  # function composition here
    return total

# Example shopping cart
items = [100, 250, 300, 50]   # prices of items
discount = 10                 # 10% discount

# Calculate total
final_total = total_price(items, discount)

print("Total price after discount:", final_total)
