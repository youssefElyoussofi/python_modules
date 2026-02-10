def ft_harvest_total()->None:
    result = 0
    for i in range(3):
        result += int(input(f"day {i + 1} harvest : "))
    print(f"Total harvest: {result}")


if __name__ == "__main__":
    ft_harvest_total()