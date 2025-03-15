#
# Name Wolfgang Meyer
# Date 3-14-25
# Plant Information Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def print_info(self):
        print(f"Plant Information:\nPlant name: {self.name}\nCost: {self.cost}\n")

class Flower(Plant):
    def __init__(self, name, cost, annual, color):
        super().__init__(name, cost)
        self.annual = annual
        self.color = color
    
    def print_info(self):
        print(f"Plant Information:\nPlant name: {self.name}\nCost: {self.cost}\nAnnual: {self.annual}\nColor of flowers: {self.color}\n")

def print_list(garden):
    for i, plant in enumerate(garden, 1):
        print(f"Plant {i} Information:")
        plant.print_info()

def main():
    my_garden = []
    
    # Simulated input instead of input() due to I/O error
    user_input = "plant Spirea 10 flower Hydrangea 30 false lilac flower Rose 6 false white plant Mint 4 -1".split(" ")
    
    i = 0
    while i < len(user_input) and user_input[i] != "-1":
        if user_input[i] == "plant":
            name = user_input[i+1]
            cost = int(user_input[i+2])
            my_garden.append(Plant(name, cost))
            i += 3
        elif user_input[i] == "flower":
            name = user_input[i+1]
            cost = int(user_input[i+2])
            annual = user_input[i+3] == "true"
            color = user_input[i+4]
            my_garden.append(Flower(name, cost, annual, color))
            i += 5
    
    print_list(my_garden)

if __name__ == "__main__":
    main()
