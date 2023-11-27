print("Welcome to the Martian Cargo Finder Program!")
print("You need to find three boxes buried on the path.")
print("Each box has legs, so if you enter a wrong kilometer mark, the boxes will move to a new location.")
print("The goal is to find all three boxes with a total weight of 713 kilograms.\n")


cargo_kg = [0, 0, 0]
total_kg = 0

while True:
    try:
        kilometers = []
        for i in range(3):
            mark = int(input(f"Enter the kilometer mark for box {i + 1}: "))
            kilometers.append(mark)

        for i in range(3):
            cargo_kg[i] = int(input(f"Enter the weight for box {i + 1} at {kilometers[i]} kilometers: "))

        total_kg = sum(cargo_kg)

        if total_kg == 713:
            print("\nCongratulations! You found all the boxes.")
            break
        else:
            print(f"\nIncorrect total weight. Try again. Total weight is {total_kg}, but it should be 713.\n")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers.\n")
