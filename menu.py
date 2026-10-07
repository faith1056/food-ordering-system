categories = {
    "Main Meals": ["Rice", "Beans", "Yam"],
    "Drinks": ["Coke", "Water", "Juice"],
    "Desserts": ["Cake", "Ice Cream", "Fruit"]
}

prices = {
    "Rice": 1500,
    "Beans": 1200,
    "Yam": 1000,
    "Coke": 500,
    "Water": 300,
    "Juice": 700,
    "Cake": 800,
    "Ice Cream": 1000,
    "Fruit": 600
}

customer_name = input("What is your name? ").strip().title()

choice = input("What would you like to order? ").strip().title()

# Check if category is valid
while choice not in categories:
    print("Error...!")
    choice = input("What would you like to order? ").strip().title()

# Display available foods
for item in categories[choice]:
    print(item)

# First order
total = 0
orders_list = []

orders = input("What would you like to order? ").strip().title()

while orders not in categories[choice]:
    print("Order not available")
    orders = input("What would you like to order? ").strip().title()

# Get valid quantity
while True:
    try:
        quantity = int(input("How many would you like? "))

        if quantity < 1:
            print("Quantity must be at least 1")
            continue

        break

    except ValueError:
        print("Please enter a number.")

total = total + prices[orders] * quantity

orders_list.append([orders, quantity])

print(f"You ordered {quantity} x {orders}: ₦{prices[orders] * quantity}!")

# Ask if customer wants another item
again = input("Do you want to order another item? yes/no: ").strip().lower()

while again == "yes":
    more_orders = input("What would you like to order again? ").strip().title()

    # Check the additional order
    while more_orders not in categories[choice]:
        print("Your order is not available in this category")
        more_orders = input("What would you like to order? ").strip().title()

    # Get valid quantity for additional order
    while True:
        try:
            more_quantity = int(input("How many would you like? "))

            if more_quantity < 1:
                print("Quantity must be at least 1")
                continue

            break

        except ValueError:
            print("Please enter a number.")

    total = total + prices[more_orders] * more_quantity

    orders_list.append([more_orders, more_quantity])

    print(
        f"You ordered {more_quantity} x {more_orders}: "
        f"₦{prices[more_orders] * more_quantity}!"
    )

    again = input("Do you want another item? yes/no: ").strip().lower()

payment_method = input(
    "How would you like to pay? Cash, Transfer, or POS: "
).strip().title()

while payment_method not in ["Cash", "Transfer", "Pos"]:
    print("Invalid payment method.")
    payment_method = input(
        "Please choose Cash, Transfer, or POS: "
    ).strip().title()


print("\n========== RECEIPT ==========")
print(f"Customer:  {customer_name}")

for order in orders_list:
    food = order[0]
    quantity = order[1]
    subtotal = prices[food] * quantity

    print(f"\n{food}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ₦{subtotal}")

print("\n-----------------------------")
print(f"PAYMENT METHOD: {payment_method}")
print(f"TOTAL: ₦{total}")
print("=============================")

