age = 18
if age < 18:
    print("TRUE")
else:
    print("FALSE")

x = 10
y = 20
if x < y and y > 30:
    print("TRUE")
else:
    print("FALSE")

if x < y or y > 30:
    print("TRUE")
else:
    print("FALSE")

marks = 90
if marks < 40:
    print("E")
elif marks < 50:
    print("D")
elif marks < 60:
    print("C")
elif marks < 70:
    print("B")
else:
    print("A")

bettingNumber = 3
if bettingNumber == 1:
    print("You won a goat!!")
elif bettingNumber == 2:
    print("You won a cow!!")
elif bettingNumber == 3:
    print("You won 2 cows!!")
elif bettingNumber == 4:
    print("You won 5 cows!!")
else:
    print("Please enter a number from 1-4 to bet!!")


#1.
p = 200000
r = 12
t = 3
interest = (p * r * t)/100
if interest == 5000:
    print("Scam")
elif interest == 20000:
    print("Bad loan")
else:
    print("Good loan")

height = 1.85
weight = 110
BMI = (weight/(height * height))
if BMI <= 18:
    print("Underweight")
elif BMI <= 29.0:
    print("Normal weight")
elif BMI <= 34.0:
    print("Overweight")
else:
    print("Obese")