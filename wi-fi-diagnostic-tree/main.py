#
# Name Wolfgang Meyer
# Date 1-22-2025
# Wi-Fi Diagnostic Tree Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.
def wifi_diagnostic():
    print("Reboot the computer and try to connect.")
    response = input("Did that fix the problem? (yes/no): ").strip().lower()
    if response == "yes":
        return
    
    print("Reboot the router and try to connect.")
    response = input("Did that fix the problem? (yes/no): ").strip().lower()
    if response == "yes":
        return
    
    print("Make sure the cables between the router and modem are plugged in firmly.")
    response = input("Did that fix the problem? (yes/no): ").strip().lower()
    if response == "yes":
        return
    
    print("Move the router to a new location.")
    response = input("Did that fix the problem? (yes/no): ").strip().lower()
    if response == "yes":
        return
    
    print("Get a new router.")
    
# Run the diagnostic program
wifi_diagnostic()
