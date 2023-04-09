3# CSC_120 Logbook : Pg15, Exercise 2

# Start Program

# ask the user for the temperature and unit
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ").upper()

# convert the temperature to the other unit
if unit == "C":
            converted_temp = (temp * 1.8) + 32
            new_unit = "F"

elif unit == "F":
            converted_temp = (temp - 32) / 1.8
            new_unit = "C"

else:
        print("Invalid unit.")
        exit()

# print the converted temperature
print(f"{temp:.1f}{unit} is {converted_temp:.1f}{new_unit}")
