balance = 5000
print("1-check your balance ")
print("2-deposit money ")
print("3-withdraw money ")
choice = int(input("enter your choice: "))
if choice == 1:
    print("balance: ", balance)
elif choice == 2:
    if balance > 0:
        deposit = int(input("enter your money: "))
        balance += deposit
        print("balance: ", balance)
    elif balance <= 0:
        print("there isn't enough money in your account")
elif choice == 3:
    money = int(input("enter your deposit: "))
    balance -= money
    print("balance: ", balance)

print("total balance: ", balance)
