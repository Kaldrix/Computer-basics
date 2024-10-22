#Importing the resources needed for the displaying the function
import matplotlib.pyplot as plt
import numpy as np

#For the first part, this code defines the variables with the value asked in the exercise
asked_P=250000 #in €
asked_years=30
asked_n=asked_years*12
asked_r=5/12/100

#Defining the main function to calculate the monthly payment asked
Asked_Monthly_loan_payment=asked_P*(asked_r*(1+asked_r)**asked_n) / ((1+asked_r)**asked_n - 1)

#Code that prints and shows the result, explaining the formula too
print ("The monthly payment is calculated with the formula:M = P[r(1+r)^n] / [(1+r)^n - 1]")
print ("Where P is the principal loan amount in €, n is the total months of the total years and r is the monthly interest rate")
print (f"For the designed values (250.000€ of principal loan amount, 5% annual interest rate and 360 total months, the monthly loan payment is {Asked_Monthly_loan_payment}")

#This code adds to the same concepts intervals of values for the graphical representation
P=250000
years=np.linspace(1, 70)
n=years*12
M_I_R=float(input("Enter the annual interest rate without the percentage")) 
r=M_I_R/12/100
Monthly_loan_payment=P*(r*(1+r)**n) / ((1+r)**n - 1)

#Second part. Creating and displaying the function
Graphic_monthly_payments=[Monthly_loan_payment]
plt.plot(years, Monthly_loan_payment, color="blue", label=f"Annual rate:{r}")
plt.title("Monthly loan payment depending on the total number of years")
plt.xlabel("Years")
plt.ylabel("Monthly loan payment (€)")
plt.grid(True)
plt.show()


