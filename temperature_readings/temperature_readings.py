# CSC_120 Logbook : Pg15, Exercise 3

# Start Program

temperature = float(input("Enter temperature in Celsius: ")) # Prompts user for input

if temperature < -273.15:
        print("The temperature is invalid because it is below absolute zero.")
        
elif temperature == -273.15:
        print("The temperature is absolute zero.")
        
elif temperature > -273.15 and temperature < 0:
        print("The temperature is below freezing.")
        
elif temperature == 0:
        print("The temperature is at freezing point.")
        
elif temperature > 0 and temperature < 100:
        print("The temperature is in the normal range.")
        
elif temperature == 100:
        print("The temperature is at the boiling point.")
        
else:
        print("The temperature is above the boiling point.")

# End Program
