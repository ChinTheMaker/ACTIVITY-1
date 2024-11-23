def calculator():
    while True:
        # Display menu
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        # Get user's choice
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ["1", "2", "3", "4"]:
            # Get the numbers from the user
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break  # If both inputs are valid, exit the loop
                except ValueError:
                    print("Invalid input! Please enter numeric values for both numbers.")
            
            # Perform the operation based on user's choice
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error! Division by zero.")
                    continue  # Skip this operation and ask for input again

            # Display result without decimal point if it's a whole number
            if result.is_integer():
                result = int(result)  # Convert to integer if no decimal
            print(f"The result of the operation is {result}")
            break  # Exit the loop after performing the operation
        else:
            print("INVALID input, please choose between 1-4.")

# Run the calculator
calculator()
