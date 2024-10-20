#Code that introduces the variables needed to decide whether the student has passed or not
Exam_Score=float(input("Enter your exam score"))
Assistance=float(input("Enter the percent of classess you´ve assisted to"))
Minimum_assistance= Assistance*0.8

#Explaining the criteria used
print("The criteria applied to decided whether you´ve passed or not is:")
print("Exam score>=70 percent and assistance percent >=80%")

#Establishing the condition to pass the term, the year or whatever
if Exam_Score>=70 and Assistance>=Minimum_assistance:
 print(f"Congratulations. You´ve passed")
else:
 print(f"You haven´t fullfiled at least one of the conditions, so you´ve failed")

