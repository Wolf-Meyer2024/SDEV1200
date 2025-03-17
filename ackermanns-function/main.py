#
# Name Wolfgang Meyer
# Date 3 - 17 - 25
# Ackermann's Function Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

def ackermann(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m,n-1))
# Testing the function with small values of m and n
print(ackermann(0, 0))  # Expected output: 1
print(ackermann(1, 1))  # Expected output: 3
print(ackermann(2, 2))  # Expected output: 7
print(ackermann(3, 3))  # Expected output: 61
