class GardenManager:
    total_mangers = 0
    def __init__(self,name):
        total_mangers += 1 # total_mangers = 0 + 1 = 1
        self.name = name
        self.plans = []
    def add_plant(self,plant):
        self.plans.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age

class FloweringPlant(Plant):
    def __init__(self,name,height,age,color):
        super().__init__(name,height,age)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize):
        super().__init__(name, height, age, color)
        self.prize = prize


if __name__ == "__main__":
    p1 = Plant("tomato",20,10)
    p2 = FloweringPlant("Rose",50,30,"red")
    p3 = PrizeFlower("Sunflower",20,10,"red",20)

    m1 = GardenManager("Alise")
    m1.add_plant(p1)
    m1.add_plant(p2)
    m1.add_plant(p3)
