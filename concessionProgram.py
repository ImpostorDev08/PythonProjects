menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "sode": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

for key, value in menu.items():
        print(f"{key}: ${value:.2f}")

while True:
        food = input("Select an item from the menu enter q to quit: ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print(f"\nTotal is: ${total:.2f}")