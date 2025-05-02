English = float(input("\t\t\t\tEnter your English marks: "))
Maths = float(input("\t\t\t\tEnter your Maths marks: "))
Urdu = float(input("\t\t\t\tEnter your Urdu marks: "))
Science = float(input("\t\t\t\tEnter your Science marks: "))
Programming = float(input("\t\t\t\tEnter your Programming marks: "))
grade = " "

total = English + Urdu + Maths + Programming + Science
print("\n\t\t\t\t***YOUR TOTAL MARKS ARE " + str(total)+ " out of 500***")

percentage = total / 500 * 100
roundOff = round(percentage,2)

if percentage >= 90:
    grade= "A+"
    
    
elif percentage >= 80:
    grade = "A"
    
    
elif percentage >= 70:
    grade = "B"
    
    
elif percentage >= 60:
    grade = "C"
    
elif percentage >= 50:
    grade = "D"
    
    
else:
    grade = 'F'
    print("\t\t\t\tSorry! You can't promote to another class.")
    

    
print("\n\t\t\t\tYour total marks are: " + str(total) + "\n\t\t\t\tYour percentage is " + str(roundOff) + "%\n\t\t\t\tYour grade is " + str(grade) +".")

