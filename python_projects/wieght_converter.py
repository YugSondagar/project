weight = float(input("Enter your weight: "))

unit = input("Enter 'k' for kilogram and 'p' for pound:")

if unit == 'k':
    weight = weight * 2.205
    print(f"you are {weight} pound")
elif unit == 'p':
    weight = weight / 2.205
    print(f"you are {round(weight,2)} kg")
else:
    print("Invalid letter please enter k or p")


