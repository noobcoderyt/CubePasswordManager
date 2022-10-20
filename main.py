user_input = input("Welcome To The Safe And Secure, Cube Password Manager\nType 'passwords' to see the list of the passwords use stored\nType 'add' to add a new password to the database\nType 'remove' to remove a password from database\n")


if user_input == ("passwords"):
    f = open('passwords.txt','r')
    content = f.read()
    print(f"The Stored Passwords Are :\n{content}")
    f.close()

else:
    username = input("Enter The Username Of The Account\n")
    password = input("Enter The Password Of The Account\n")

    f = open('passwords.txt','a')
    new_password = f"{username} = {password}\n"
    f.write(new_password)

input()