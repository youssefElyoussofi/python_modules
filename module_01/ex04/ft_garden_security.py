class SecurePlant:
    def __init__(self,name ,height,age):
        self.name = name
        self._age = 0
        self._height = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self,age):
        if age < 0:
            print("Error age cannot negative")
            return
        else:
            self._age = age
    def set_height(self,height):
        if height < 0:
            print("Error Height cannot negative")
            return
        else:
            self._height = height
    def get_age(self):
        return self._age
    def get_height(self):
        return self._height
    


if __name__ == "__main__":
    p1 = SecurePlant("khobiza",500,20)
    p1.set_age(-5)
    print(p1.get_age())
    p1.set_age(10)
    print(p1.get_age())


    
