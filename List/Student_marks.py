
marks = int(input("Kitne Students Marks"))

total = 0
Store = []
for i in range(1 , marks + 1):
    num = int(input(f"Enter {i} students marks  " ))

    Store.append(num)

print(Store)

for i in Store:
    total += i

print(f"The Total marks is :{total}")

avg = (total / marks)

print(f"Total Average is :{avg}")

# Higest marks tooper students

# Pass a single list as the argument
top_score = max(Store)
lowest_score = min(Store)

print("Higest Score is = ",top_score)
print("Lowest Score is = ",lowest_score)
