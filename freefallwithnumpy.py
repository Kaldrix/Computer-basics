#Basic step. Importing the libraries needed
import numpy as np
import matplotlib.pyplot as plt

#Defining every measure needed to calculate the position of an object in free fall
#To make the results more acurrate, I´ve done it on Earth
Gravity = 9.81
Height = float(input("Enter the initial height where the object is thrown: "))
Time = np.linspace(0, 999)  

#Formula needed and specifying to Python the limit point where the grafic will stop
Position = Height - 0.5 * Gravity * Time**2
Limit = 0 
Time_filtered = Time[Position >= Limit]
Position_filtered = Position[Position >= Limit]

#Calculating the difference between intevals and its average

Difference=np.abs(np.diff(Position_filtered))
Average=np.mean(Difference)
print(f"Difference between continous values of time: {Difference}")
print(f"Average of those intervals: {Average}")

#Generating the graphic
plt.plot(Time_filtered, Position_filtered, color="black", label="Position")
plt.title("Position of an object in free fall over time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid()
plt.show()