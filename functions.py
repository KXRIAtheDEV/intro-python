def motto():
    print("Hello there is our motto")


motto()
motto()
motto()
motto()


def vision():
    print("Hello, this is our vision")


vision()


def add():
    x = 10
    y = 20
    z = x + y
    print(z)


add()
add()
add()
add()


def average(x , y , z):
    average = (x + y + z) / 3
    print("Your average is "+str(average))


average(12 , 94 , 45)
average(12 , 37 , 45)
average(11 , 37 , 45)


def bmi(weight,height):
    bmi = weight / pow(height, 2)
    if bmi<= 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")
bmi(63, 1.7)


def grading(marks):
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
grading(65)


def login():
    userdtb = {
        'user@example.com': 'user123'
    }
    email = input("What is your email?")
    password = input("What's your password?")
    if email in userdtb:
        if password == userdtb[email]:
             def grading(marks):
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

             grading(40)
        else:
            print("Wrong login details")
    else:
        print("wrong")
login()









