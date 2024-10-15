#Program that asks the user to introduce the value of the variables needed
position0= float(input("Enter the intial position of the object (m)")) 
int (position0)

speed0= float(input ("Enter the initial value of the speed (m/s)"))
int (speed0)

time= float (input ("Enter the value of the time (s)"))
int (time)

acceleration= float (input ("Enter the value of the acceleration (m/s^2)"))
int (acceleration)

#This is just an addition to make the program more precise, checking if the time is >=0
if time>=0:
 print ("Values are correct")
else:
 print ("Time can never be below 0. Please introduce a value>=0") 

#Defining the final position and calculating it
Position= position0 + speed0*time + 0.5*acceleration*time**2
print (f"The final position is {Position}")

#Same as with the position, but with the speed
Speed= speed0 + acceleration*time
print (f"The final speed is {Speed}")
print ("The acceleration remains the same as it is a MRUA")
