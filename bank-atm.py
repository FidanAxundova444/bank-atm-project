balance = 5000
correct_pincode="6484"

for i in range(3):
    pincode = input("enter your pincode: ")
    if pincode==correct_pincode:
        print("1-check your balance ")
        print("2-deposit money ")
        print("3-withdraw money ")
        choice = int(input("enter your choice: "))

        if choice == 1:
            print("balance: ", balance)
        elif choice == 2:
            deposit = int(input("enter your deposit: "))
            balance += deposit
            print("balance: ", balance)

        elif choice == 3:
            if balance > 0:
                money = int(input("enter your money: "))
                balance -= money
                print("balance: ", balance)
            elif balance <= 0:
                print("there isn't enough money in your account")

        print("total balance: ", balance)
        break

    else:
        print("try again")





