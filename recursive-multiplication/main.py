#
# Name Wolfgang Meyer
# Date 3-17-25
# Recursive Multiplication Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 

def recursive_multiplication(x, y):
    if x == 1:
        return y
    else:
        return y + recursive_multiplication(x - 1, y)
    
print(recursive_multiplication(7, 4))  # Expected output: 28
print(recursive_multiplication(3, 5))  # Expected output: 15
