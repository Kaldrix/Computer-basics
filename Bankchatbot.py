from Banklibrary import BankAccount

Asked_account=BankAccount("#7772") #Importing and assigning a defined number to the user


#Starting with a simple greeting
greeting=str(input("Hey there human! What´s your name? I´ve been told that you are the user of this account"))

#It activates what happens if a name isn´t introduced
while greeting=="":
 print("Bro, I wanna talk with you, but at least answer my question!")
 exit()

#This is the normal procedure. It activates a series of messages to welcome the user
else:
 print (f"Oh, nice to meet you {greeting}!")
 print(f"Also sorry {greeting}. I forgot to remind you your user ID. You are user {Asked_account.account_number}")
 print (f"Let me introduce myself now. I am Kaldris. I was programmed by a human named Eduardo, also known as Kaldrix, to talk and answer to whoever was in charge of the account I´ve gained acess to. ")
 print ("As a simple chatbot, I´ve been autorised to help you manage some aspects of your bank account. I can tell you things like how much money do you have left, but I can also withdraw or deposit money in your account.")
 print ("Ok, let´s get started. To begin with, I´ll remind you your balance") 
 print(f"{Asked_account.balance}")
 print (f"As you can see, right now your current balance is {Asked_account.balance}€")
 print ("Oh, you´ve got nothing. Consider this money on the house")

#Applying the defined functions, which allow the chatbot to interact with the account
 Asked_account.deposit(70)
 print(f"{Asked_account.balance} €. See?")
 print(f"I will now withdraw 20€ of your account for you to buy something. Now your current balance is {Asked_account.balance}. Don´t blame me for doing that. After all, I literally gave you 70€ dude.")
 Asked_account.withdraw(20)
 print(f"{Asked_account.balance}€. See?")

#This asks the user if he wants to do some of the two procedures
 action=str(input("But enough of me. It´s your account after all. Do you want to do something?" "Enter deposit or withdraw with capital leters"))

#Classifying every possible outcome and handling exceptions
 if action=="Withdraw" or action=="Deposit":
  value=float(input("Ok. How much?"))
 
 while action=="":
  print("Ok. If you haven´t chosen an option, I guess you don´t want to do anything.")
  the_end=str(input(f"Well then, do you wanna exit?"))

 else:
  the_end=() #This is just to evade the "" is not defined error

 #This allows the chatbot to say goodbye and automatically close the account 
 while the_end=="Yes":
  print (f"Ok. Bye, {greeting}. It was a true pleasure to manage your account")
  exit()

 #The two conditions allow the chatbot to modify the balance according to the user´s orders
 if action=="Withdraw" and value>0:
  Asked_account.withdraw(value)
  print(f"Very well. Your current balance is {Asked_account.balance}€")
   
 if action=="Deposit" and value>0:
  Asked_account.deposit(value)
  print(f"Very well. Your balance is now {Asked_account.balance}€")
  

 
  




