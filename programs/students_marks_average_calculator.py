#Simple Login System
def exit():
   
        print("GoodBye!")

print("Welcome!")
while True:

    
    choice = input("Type '1' to register.'2' to login.'3' to exit:")
    if choice == "3":
          
        exit()
        break
    if choice =="1":
         username = input("Enter a username:")
         password = input("Enter a password:")
         print("Account created!")
    elif choice =="2":
         check_username=input("Enter username:")
         if check_username == username:
              check_password = input("Enter your password:")
              if check_password == password:
                   print("Successfull login!")
              else:
                   print("Incorrect username or password!")
    else:
         print("Invalid Option!")
         
        
         

