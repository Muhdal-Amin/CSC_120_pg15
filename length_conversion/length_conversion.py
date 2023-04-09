# CSC_120 Logbook : Pg15, Exercise 1

# Start Program

length_cm = float(input("Enter a length in centimeters: ")) # Prompts user to input length in centimeters

if length_cm < 0:
        print("Invalid entry. Length must be positive.") # Checks if length is negative and outputs an error message if it's negative

else:
        length_in = length_cm / 2.54 # Converts length to inches
        
        print(f"{length_cm:.2f} centimeters is equal to {length_in:.2f} inches.") # Outputs the length in inches

# End program
