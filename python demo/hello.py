

marks = int(input("Enter Student Markrs:"))    

if  90 <=  marks <= 100 :
    grade = "A"
elif  80 <=  marks <= 89 :
    grade = "B"
elif 70<=  marks <= 79 :
    grade = "C"
elif 60 <=  marks <= 69 :
    grade = "D"
elif 0 <=  marks <= 59 :
    grade = "F"
    
else :
    grade = "Invalid Grade."    
print("Grade of the student is :", grade)



