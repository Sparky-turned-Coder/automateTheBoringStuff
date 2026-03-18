password_file = open("SecretPasswordFile.txt")
secret_password = password_file.read()
typed_password = input("Enter your password:")

# print(secret_password)

if typed_password == secret_password:
    print("Access Granted...")
    if typed_password == "12345":
        print(
            "That password is stupid as shit. For your own safety, you should not have access to the internet."
        )
else:
    print("Access Denied...")
