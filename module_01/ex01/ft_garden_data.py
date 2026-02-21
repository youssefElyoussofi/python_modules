class Plant:
    def __init__(ad, name,height,age):
        
        ad.name = name
        ad.height = height
        ad.age = age

    def __str__(ad):
        return f"{ad.name}: {ad.height }cm, {ad.age }days old"
    

if (__name__ == "__main__"):
    p1 = Plant("Rose",30,2)
    p2 = Plant("Sunflower",80,45)
    p3 = Plant("Cactus",15,120)
    print(p1)
    print(p2)
    print(p3)
    
    
    
        