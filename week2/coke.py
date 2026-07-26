total = 0
while total < 50:
    coin = int(input("Insert Coin:"))
    if coin == 5 or coin == 10 or coin == 25:
        total += coin
    if total < 50:
        print("Amount Due:", 50 - total)
    if total >= 50:
        print("Change Owed:", total - 50)
