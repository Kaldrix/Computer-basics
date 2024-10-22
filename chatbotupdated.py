#Starting with a simple greeting
greeting=str(input("Hey there human! What´s your name?"))

#It activates what happens if a name isn´t introduced
while greeting=="":
 print("Bro, I wanna talk with you, but at least answer my question!")
 exit()

#This is the normal procedure. The process will be the same except a few puntual exceptions
else:
 print (f"Oh, nice to meet you {greeting}!")
 year_of_birth=str(input("Ok, I want to know your year of birth to! I was born in 2024 "))
 
#This process is the same as the previous one, but adding a code to handle nonsense ages
while year_of_birth=="" or year_of_birth>"2024" or year_of_birth<"1905":
 print("Bro, I wanna talk with you, but at least answer my question!")
 exit()

else:
 print(f"Oh, {year_of_birth} I see. Then you are way older than me...")
 month_of_birth=str(input("And what about your month of birth tho? I wanna know it too if we are gonna be friends"))
 
#Same as with the year, but this time with non-existing months
while month_of_birth=="" or month_of_birth>"12" or month_of_birth<"1":
 print("Bro, I wanna talk with you too, but at least answer my question!")
 exit()

else:
 print(f"{month_of_birth}. Ok cool I guess")
 day_of_birth=str(input("And finally your day of birth"))
 
#I won´t take into account leap years. It would be something too complex to handle
while day_of_birth=="" or day_of_birth>"31" or day_of_birth<"1":
 print ("Bro, I wanna talk with you too, but at least answer my question!")
 exit()

else:
 print(f"{day_of_birth} Ok. Good to know your date of birth. Mine is 19/10/2024. I was created by a human called Eduardo. He is kind of my god")
 hobbies=str(input("Ok, what if we move on to our hobbies next? Tell me, tell me"))
 
while hobbies=="":
 print ("Bro, I wanna talk with you too, but at least answer my question!")
 exit()

else:
 print(f"{hobbies}, interesting. Good for you. After all, I am a robot so I don´t have hobbies... Oh, wait, I do have one. Greeting and talking to people like you {greeting}. I guess it is my job and my hobbie at the same time")
 print(f"Now bye, {greeting}. My creator ordered me to stop. I wish we could have kept speaking, but it was a true pleasure to meet you. Take care, {greeting}")