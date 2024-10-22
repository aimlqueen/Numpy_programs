import numpy as np

# Create a 3D array
a = np.array([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]])

# Perform operations
addition = a + 1            # Adds 1 to each element
subtraction = a - 1         # Subtracts 1 from each element
multiplication = a * 2      # Multiplies each element by 2
division = a / 2            # Divides each element by 2
exponentiation = a ** 2     # Squares each element
square_root = np.sqrt(a)    # Square root of each element
