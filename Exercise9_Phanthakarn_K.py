print("Login form")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("username or password was wrong !")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Login success")