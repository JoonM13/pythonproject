print("account number is '41693'")
def help():
  print("Press 'b' to display balance.")
  print("Press 'd' to deposit money.")
  print("Press 'w' to withdrawal from your account.")
  print("Type 'help' to display these commands again.")
  print("Type 'exit' to leave this ATM.")
  print("When in withdrawal or deposit, type 0 to do nothing.")

def balance():
  print("You currently have", "$", money)

def deposit():
  global money
  global d
  d = 0
  try:
    d = float(input("How much would you like to deposit? : "))
  except:
    print("Unknown value entered, returning to menu.")
  if type(d) == float:
    if d < 0:
      print(d, "is a negative, if you want to withdrawal, you should exit and go to withdrawal.")
    else:
      money = money + d
      print("Current balance :", money)

def withdrawal():
  global money
  global w
  w = 0
  try:
    w = float(input("How much would you like to withdraw? : "))
  except:
    print("Unknown value entered, returning to menu.")
  if type(w) == float:
    if w > money:
      print(w, "exceeds your current balance of", money)
      withdrawal()
    else:
      money = money - w
      print("Current balance :", money)





global action
global accountnumber
global money
money = 0
action = "N/A"
accountnumber = -17


while accountnumber == -17:
    accountnumber = input("Input account number : ")
    if accountnumber != "41693":
        print("Accessing account : ", accountnumber)
        print("Invalid account, please try again")
        accountnumber = -17
    else:
        break
  
print("Welcome account number : ", accountnumber)
help()
  
while action != "exit":
  action = input("What do you want to do? : ")
  if action == "b":
    balance()
  elif action == "w":
    withdrawal()
  elif action == "d":
    deposit()
  elif action == "help":
    help()
  elif action == "exit":
    print("Exiting . . .")
  else:
    print("Unknown option chosen, try again.")





print("Thank you for using COMPANY_NAME_ATM. Goodbye.")
exit()


