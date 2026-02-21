class Plant:
    def __init__(self, name,height,age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.height }cm, {self.age }days old"
    

if (__name__ == "__main__"):
    p1 = Plant("Rose",30,2)
    p2 = Plant("Sunflower",80,45)
    p3 = Plant("Cactus",15,120)
    print(p1)
    print(p2)
    print(p3)
    
    
        