#
# Name Wolfgang Meyer
# Date 3-13-25
# ShiftSupervisor Class Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.

class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, department, job_title):
        super().__init__(name, id_number, department, job_title)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus
    def display_info(self):
        base_info = super().display_info()
        print (f"annual salary: ${self.annual_salary: .2f}")
        print (f"annual bonus: ${self.annual_bonus: .2f}")
        print ("-" * 40)
