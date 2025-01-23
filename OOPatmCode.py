class Atm:

  def __init__(self):
    self.pin=''
    self.balance=0
    self.menu()

  def menu(self):
    user_input=input("""
    Hello how can I help you:
    1.Press 1 to create Pin
    2.Press 2 to change pin
    3.Press 3 to check balance
    4.Press 4 to withdraw amount
    5. Press 5 to exit

    """)

    if user_input=='1':
      self.create_pin()
    elif user_input=='2':
      self.change_pin()
      pass
    elif user_input=='3':
      self.check_balance()
      
    elif user_input=='4':
      self.withdraw_amount()
    else:
      exit()



  def create_pin(self):
    user_pin = input(('Enter pin number :'))
    self.pin=user_pin
    user_balance = int (input("enter balance : "))
    self.balance=user_balance
    print('Pin created successfully')
    print('Balance is :',self.balance)
    self.menu()

  def change_pin(self):
    user_pin = input('Enter previous pin :')
    if user_pin== self.pin:
      self.pin=input('Enter new pin : ')
      print('Pin changed successfully.')
    else:
      print('Please try again')
    self.menu()

  def check_balance(self):
    user_pin = input('Enter  pin :')
    if user_pin== self.pin:
      print("Available balance is :",self.balance)
    else:
      print('Unable to fetch balance .')
    self.menu()

  def withdraw_amount(self):
    user_pin = input('Enter  pin :')
    if user_pin== self.pin:
      user_amount= int(input("Enter amount to withdraw :"))
      if user_amount<=self.balance:
        self.balance-=user_amount
        print("Cash debited Successfully . Remaining balance  is :",self.balance)
      else:
        print("Insufficiant Funds available.")
    else:
      print("Incorrect Pin , Pleas try again.")
    self.menu()

