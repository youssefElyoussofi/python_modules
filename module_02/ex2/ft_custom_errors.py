from typing import Any

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def plantCare(name:Any ,lastWater :int, waterStock : int)->None:
    try:
        _ = str(name)
        _ = int(waterStock)
        _ = int(lastWater)

        if lastWater > 5:
            raise PlantError(f"Caught PlantError: the {name} plant is wilting!")
        if waterStock <= 0:
            raise WaterError("Caught WaterError: Not enough water in the tank!")
    except PlantError as e:
        print(e)
    except WaterError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    plantCare(66,7,0)

    print("Testing PlantError...")
    plantCare("tomato",7,0)
    print("Testing WaterError...")
    plantCare("tomato",2,0)
    print("Testing catching all garden errors...")
    plantCare("tomato",7,0)
    plantCare("tomato",2,0)

    
