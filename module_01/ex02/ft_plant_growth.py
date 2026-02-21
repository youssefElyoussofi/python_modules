class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self._age = age
        self.day = 1
        
    def grow(self):
        self.height += 6
    def age(self):
        self._age += 6
    def display(self):
         print(f"=== Day {self.day} ===")
         print(f"{self.name}: {self.height} cm, {self._age} days old")
    def get_into(self):
        self.day += 6
        self.grow()
        self.age()
        self.display()
        print(f"Growth this week: +6cm")

if (__name__ == "__main__"):
    p1 = Plant("Rose",25,30)
    p1.display()
    p1.get_into()
    p1.age()
    p1.get_into()