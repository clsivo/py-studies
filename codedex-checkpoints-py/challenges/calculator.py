import math

print("Welcome to the calculator challenge!")
print("==================")
print("Area Calculator")
print("==================")
print("1. Triangle"
      "\n2. Rectangle"
      "\n3. Square"
      "\n4. Circle"
      "\n5. Quit")

choice = int(input("Please select a shape to calculate the area: "))
if choice == 1:
    base = float(input("Please enter the base: "))
    height = float(input("Please enter the height: "))
    area = (base * height) / 2
    print("The area of the triangle is: ", area)
elif choice == 2:
    base = float(input("Please enter the base: "))
    height = float(input("Please enter the height: "))
    area = base * height
    print("The area of the rectangle is: ", area)
elif choice == 3:
    side = float(input("Please enter the side length: "))
    area = math.pow(side, 2)
    print("The area of the square is: ", area)
elif choice == 4:
    radius = float(input("Please enter the radius: "))
    area = math.pi * math.pow(radius, 2)
    print("The area of the circle is: ", area)
elif choice == 5:
    print("Goodbye!")
else:
    print("Invalid choice. Please select a valid option.")