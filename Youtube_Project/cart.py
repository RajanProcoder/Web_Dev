Food = []
price = []
total = 0


while True:
    food = input("What Food Do y exist for Q  ")

    if food.lower() == "q":
        break
    else:
        price1 = float(input("Enter Food Price"))

        Food.append(food)
        price.append(price1)

for food in Food:
    print(f"{food}")

for price1 in price:
    total += price
    print(f"{total}")
