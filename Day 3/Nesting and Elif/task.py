print("Yo welcome to the biggest rollercoaster in town")
height =  int(input("What is your height? "))

if height >= 120:
    print("You can enjoy the ride")
    age = int(input("What is your age? "))
    if age <12:
        print("Please pay 5$ kiddo")
    elif age <=18:
        print("Please pay 7$ champ")
    else:
        print("Please pay $12 young man")
else:
    print("You gotta grow taller buddy")
