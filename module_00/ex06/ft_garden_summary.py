def ft_garden_summary():
    inputdata = input("Enter garden name: ")
    name = str(inputdata)
    inputdata = input("Enter garden age: ")    
    age = int(inputdata)
    print(f"Garden {name}")
    print(f"Age {age}")
    print("Status: Growing well!")