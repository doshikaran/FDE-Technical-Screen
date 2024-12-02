def sort(width, height, length, mass):
    """
    Determines the stack for a package based on its dimensions and mass.

    Parameters:
    width (float): Width of the package in cm.
    height (float): Height of the package in cm.
    length (float): Length of the package in cm.
    mass (float): Mass of the package in kg.

    Returns:
    str: The stack where the package should go ("STANDARD", "SPECIAL", or "REJECTED").
    """
    # Calculate volume
    volume = width * height * length
    
    # Define bulky condition
    is_bulky = volume >= 1_000_000 or any(dimension >= 150 for dimension in [width, height, length])
    
    # Define heavy condition
    is_heavy = mass >= 20
    
    # Determine the stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Main execution with user input
if __name__ == "__main__":
    print("Enter the dimensions and mass of the package:")
    try:
        width = float(input("Width (cm): "))
        height = float(input("Height (cm): "))
        length = float(input("Length (cm): "))
        mass = float(input("Mass (kg): "))
        
        # Call the function and display the result
        result = sort(width, height, length, mass)
        print(f"The package should go to the '{result}' stack.")
    except ValueError:
        print("Invalid input. Please enter numerical values for dimensions and mass.")
