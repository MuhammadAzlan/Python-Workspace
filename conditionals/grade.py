# and operator

score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    print("You got an A")
elif score >= 70 and score < 80:
    print("You got a B")
elif score >= 60 and score < 70:
    print("You got a C")
elif score >= 50 and score < 60:
    print("You got a D")
else:
    print("You got an F")
            

#other way  
if 80 <= score and score <= 100:
    print("You got an A")
elif 70 <=score and score < 80:
    print("You got a B")
elif 60<=score and score < 70:
    print("You got a C")
elif 50<=score and score < 60:
    print("You got a D")
else:
    print("You got an F")
    
 #other way  
if 80 <= score <= 100:
    print("You got an A")
elif 70 <=score < 80:
    print("You got a B")
elif 60<=score < 70:
    print("You got a C")
elif 50<=score < 60:
    print("You got a D")
else:
    print("You got an F")   
    
if score >= 80:
    print("You got an A")
elif score >= 70:
    print("You got a B")
elif score >= 60:
    print("You got a C")
elif score >= 50:
    print("You got a D")
else:
    print("You got an F")       