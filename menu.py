
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

print(prices)

choice = input("What would you like to order? ").strip().title()

for item in categories[choice]:
    print(item)

# First order
orders = input("What would you like to order? ").strip().title()

while orders not in categories[choice]:
    print("Order not available")
    orders = input("What would you like to order? ").strip().title()

print(f"You ordered {orders}: ₦{prices[orders]}!")

# Ask if customer wants another item
again = input("Do you want to order another item? yes/no: ")

while again == "yes":
    more_orders = input("What would you like to order again? ").strip().title()

    # Check the second order
    while more_orders not in categories[choice]:
        print("Your order is not available in this category")
        more_orders = input("What would you like to order? ").strip().title()

    print(f"You ordered {more_orders}: ₦{prices[more_orders]}!")

    again = input("Do you want another item? yes/no: ")
