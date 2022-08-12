def introduction_and_input():
    try:
        global size
        size = int(input("Please enter the size you wish to make your pyramid: "))
    except ValueError:
        print("Only enter a whole number")
        introduction_and_input()


print("\nHello, this program will allow you to draw a pyramid!\n")


size = 0
introduction_and_input()
spacing = int(size/2)
counter = 1

print(size)

while counter < spacing:
    print("  " * spacing, " *" * counter, "  " * spacing)
    spacing -= 1
    counter += 2
