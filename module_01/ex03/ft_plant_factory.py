class Plant:
    total = 0
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1
        print(f"created: {name} ({height}cm {age}days)")

if (__name__ == "__main__"):
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose",30,16)
    p2 = Plant("Khobiza",50,4)
    p3 = Plant("chiba",15,30)
    p4 = Plant("na3na3",20,8)
    p5 = Plant("khorshof",80,3)
    print(f"total plants created {Plant.total}")
