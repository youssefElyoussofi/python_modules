
def ft_water_reminder():
    try:
        result = int(input("Days since last watering: "))
        (result > 2) or print("Water the plants!") and print("Plants are fine")
    except ValueError:
        print("Error")