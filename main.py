def main(width, height, length, mass):
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

# Test cases
if __name__ == "__main__":
    # Standard package
    print(main(50, 40, 30, 10))  # Expected: "STANDARD"
    
    # Bulky but not heavy
    print(main(200, 50, 30, 10))  # Expected: "SPECIAL"
    
    # Heavy but not bulky
    print(main(50, 40, 30, 25))  # Expected: "SPECIAL"
    
    # Both bulky and heavy
    print(main(200, 200, 200, 50))  # Expected: "REJECTED"
    
    # Edge case: just below thresholds
    print(main(149, 149, 149, 19.9))  # Expected: "STANDARD"
    
    # Edge case: just at thresholds
    print(main(150, 150, 150, 20))  # Expected: "REJECTED"
