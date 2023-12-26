height = float(input('Insert your height: '))  
weight = float(input('Insert your weight: ')) 

BMI = weight / (height/100)**2

print(BMI)

if BMI < 18.5: 
    print(f'Your BMI is {BMI}, and is classified  as thinness') 
    
elif BMI >= 18.5 and BMI < 24.9: 
    print(f'Your BMI is {BMI}, and is classified as normal') 
    
elif BMI >= 25 and BMI < 29.9: 
    print(f'Your BMI is {BMI}, and is classified as overweight') 
    
elif BMI >=30 and BMI < 39.9: 
    print(f'Your BMI is {BMI}, and is classified as obesity') 
    
else: 
    print(f'Your BMI is {BMI}, and is classified as severe obesity') 

        
#SMALLER THAN 18.5 THINESS 0 
#BETWEEN 18,5 AND 24,9 NORMAL 0 
#BETWEEN 25,0 AND 29,9  NORMAL I
#BETWEEN 30,0 AND 39,9  OBESITY I 
#BIGGER THAN 40,0 SEVERE OBESITY II