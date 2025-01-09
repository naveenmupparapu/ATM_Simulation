print("Welcome to the ATM")
accountno = "80968316280"
pin = "2580"

entered_accountno = input("Enter your account number: ")
entered_pin = input("Enter your PIN: ")


if entered_accountno == accountno and entered_pin == pin:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Available Balance")
    print("4. Exit")
    
    x = input("Enter your choice (1-4): ")
    Totalamount = 40000

    if x == '1':
        deposit = int(input("Enter the amount to deposit: "))
        Totalamount += deposit
        print("Total amount:", Totalamount)
    elif x == '2':
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw <= Totalamount:
            Totalamount -= withdraw
            print("Total amount:", Totalamount)
        else:
            print("Insufficient balance!")
    elif x == '3':
        print("Available balance:", Totalamount)
    elif x == '4':
        print("Exit")
        print("Thanks for visiting!")
    else:
        print("Invalid choice. Please try again.")
else:
    print("Invalid account number or PIN. Please try again.")
