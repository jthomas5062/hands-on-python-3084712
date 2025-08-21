# Concession stand program

menu = {"pizza" : 2.50, 
        "hot dog": 1.50, 
        "soda": 1.00, 
        "chips": 1.25,
        "candy": 0.75,
        "water": 1.00,
        "nachos": 2.00,
        "pretzel": 1.75
        }

cart = []
total = 0

print("--- Welcome to the Concession Stand ---")
for key, value in menu.items():
  print(f"{key:10}: ${value:.2f}")
print("---------------------------------------")

while True:
  food = input("Select an item (q to quit): ").lower()
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

print("---------------------------------------")
for food in cart:
  total += menu[food]
  print(food, end=" ")

print()
print(f"Total: ${total:.2f}")