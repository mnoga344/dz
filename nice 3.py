import random

secret_number = random.randint(1, 10)
attempts = 10

for _ in range(attempts):
    guess = int(input("Вгадайте число від 1 до 10: "))

    if guess > secret_number:
        print("Менше")
    elif guess < secret_number:
        print("Більше")
    else:
        print("Вітаю, ви вгадали!")
        break
else:
    print(f"Ви не вгадали! Загадане число було: {secret_number}")
