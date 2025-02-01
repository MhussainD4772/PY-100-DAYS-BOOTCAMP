print("Welcome to the best rollercoaster in town")
height = int(input("What is your height? "))
bill = 0


if height >= 120:
    print("You can enjoy the rollercoaster")
    age = int(input("What is your age? "))
    if age <12:
        bill = 5
        print("Kids ticket is 5$")
    elif age <=18:
        bill = 7
        print("youth ticket is 7$")
    else:
        bill = 12
        print("Adult ticket is 12$")

    wants_photo = input("Do you want a photo ticket if Yes type Y and if No type N ")
    if wants_photo == "Y":
        # Add 3 dollars to the bill
        bill += 3
    print(f"Your final bill is ${bill}")


else:
    print("Grow taller buddy")
