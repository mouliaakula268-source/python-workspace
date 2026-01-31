import getpass

password = "Mouli"
attempts = 3

while attempts > 0:
    user_password = getpass.getpass("Enter the password: ")

    if user_password == password:
        name = input("Enter your name: ")
        print("Hi", name)

        age = input("Enter your Age: ")
        print(age)

        qualification = input("Enter your Qualification: ")
        print(qualification)

        break  

    else:
        attempts -= 1
        print(f"Wrong Password! Attempts left: {attempts}")

        if attempts == 0:
            print("\n Account Locked! Too many wrong attempts.")
