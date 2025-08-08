Food = []
Price = []
total = 0

while True:
    food = input("Enter the item u want to add(Q to Quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}:₹"))
        Food.append(food)
        Price.append(price)

print("\n-------- Your Shopping List --------")

for food, price in zip(Food, Price):
    print(f"{food} --- ₹{price}")
    total += price

print(f"\nYour total is: ₹{total}")