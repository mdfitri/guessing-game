import random

def main():
    """Start guessing a elements and number of periodic table game."""
    print("Guess the number!")

    periodic = [
        "titanium",
        "hydrogen",
        "carbon",
        "nitrogen",
        "zinc",
        "krypton",
        "magnesium",
        "neon",
        "sodium",
        "litium",
    ]
    
    x = random.choice(periodic)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("what a elements am I thinking of? "))

        if x == guess:
            print("you are genius but you dont be proud.!")
        elif x == "titanium":
             print("this elements is with the symbol Ti and atomic number 22. ")
        elif x == "hydrogen":
             print("this elements is with the symbol H and atomic number 1. ")
        elif x == "carbon":
             print("this elements is with the symbol C and atomic number 6. ")
        elif x == "nitrogen":
             print("this elements is with the symbol N and atomic number 7. ")
        elif x == "zinc":
             print("this elements is with the symbol Zn and atomic number 30. ")
        elif x == "krypton":
             print("this elements is with the symbol Kr and atomic number 36. ")
        elif x == "magnesium":
             print("this elements is with the symbol Mg and atomic number 12. ")
        elif x == "neon":
             print("this elements is with the symbol Ne and atomic number 10. ")
        elif x == "sodium":
             print("this elements is with the symbol Na and atomic number 11. ")
        elif x == "litium":
             print("this elements is with the symbol Li nf atomic number 3. ")
        


    
main()
