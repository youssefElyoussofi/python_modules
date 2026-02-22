class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self._height = height
        self._age = age
    def get_new_attribute_info(self):
        return ""
 
    def display_info(self):
        plant_type = self.__class__.__name__
        base_info = f"{self.name} ({plant_type}): {self._height} cm, {self._age} days,"
        print(f"{base_info} {self.get_new_attribute_info()}")
    

    
class Flower(Plant):
    def __init__(self,name,height,age,color):
        super().__init__(name,height,age)
        self.color = color
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
    def get_new_attribute_info(self):
        return f"{self.color} color"
    
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        radius = self.trunk_diameter / 10
        shade = int(3.14 * (radius ** 2)) # (radius ** 2) => (radius * radius)
        print(f"{self.name} provides {shade} square meters of shade")
    def get_new_attribute_info(self):
        return f"{self.trunk_diameter} cm diameter"
    
class Vegetable(Plant):
    def __init__(self,name,height,age,harvest_season):
        super().__init__(name,height,age)
        self.harvest_season = harvest_season
    def get_new_attribute_info(self):
        return self.harvest_season
    def nutritional_value(self):
        print(f"{self.name} is rich in Vitamin C")
if __name__ == "__main__":
    f1 = Flower("Rose",25,5,"red")
    f1.display_info()
    f1.bloom()

    t1 = Tree("fig",500,1825,50)
    t1.display_info()
    t1.produce_shade()

    v1 = Vegetable("Tomato",50,30,"summer harvest")
    v1.display_info()
    v1.nutritional_value()

    

