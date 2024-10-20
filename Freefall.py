#Introducing the variables needed
Gravity=9.81
initial_height=float(input("Enter the initial height where the object is thrown"))
time=float(input("Enter a time >=0"))

#Defining and calculating the final position of the object as wanted
Position=initial_height- (0.5* Gravity* time**2)
print ("The final position of the object is calculated by the formula x=x0-0.5gt^2")
print("Take into account that when we throw an object, we supose v0=0")
print(f"The final position is {Position}")

#Extra. Same as the previous one, but with the speed
Speed=-(Gravity* time**2)
print ("The speed is calculated by the formula v=gt^2")
print (f"The final speed is {Speed}")