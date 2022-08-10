print("\nHello, this program will allow you to draw a pyramid!\n")


def introduction_and_input():
    try:
        size = int(input("Please enter the size you wish to make your pyramid: "))
        return size
    except ValueError:
        print("Only enter a whole number")
        introduction_and_input()


size = introduction_and_input()
print(f"size is {size}")
spacing = int(size/2)
counter = 1


while counter < spacing:
    print("  " * spacing, " *" * counter, "  " * spacing)
    spacing -= 1
    counter += 2
