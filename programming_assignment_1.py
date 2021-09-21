# Names: Jonathan Ramos
# Course: CS151, Dr.Rajeev
# Date: September 16th, 2021
# Programming Assignment: 1
# Program Inputs: User Dimensions of a room in Feet (length, width, height)
# Program Outputs: Total Area in Square Feet that needs to be painted, and the gallons of primer and paint needed

# User Inputs Dimensions in Feet
print("Enter values below in feet:")
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))

# Area calculations / Algorithm
area_ceiling = length * width
area_of_one_wall = width * height
total_area = (area_of_one_wall * 4) + area_ceiling

print("\nArea of the room excluding the floor is: " + str(total_area) + " Square Feet")

# Calculations for gallons of primer and paint needed based on the total area
primer_needed = total_area / 200
paint_needed = total_area / 350

print("\nGallons of primer needed: %.2f" % primer_needed)
print("Gallons of paint needed: %.2f" % paint_needed)





