import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
b = np.array([[3, 6, 2],[6, 5, 4],[7, 6, 5]])
# Trigonometric functions for array `a`
sin_a = np.sin(a)
cos_a = np.cos(a)
tan_a = np.tan(a)

# Cosecant, Secant, Cotangent (derived)
cosec_a = 1 / sin_a  # Cosecant is the reciprocal of sine
sec_a = 1 / cos_a    # Secant is the reciprocal of cosine
cot_a = 1 / tan_a    # Cotangent is the reciprocal of tangent

# Print the results
print("Sine of a:\n", sin_a)
print("Cosine of a:\n", cos_a)
print("Tangent of a:\n", tan_a)
print("Cosecant of a:\n", cosec_a)
print("Secant of a:\n", sec_a)
print("Cotangent of a:\n", cot_a)
