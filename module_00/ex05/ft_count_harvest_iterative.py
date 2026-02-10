def ft_count_harvest_iterative():
    try:
        nb = int(input("Days until harvest: "))
        if nb < 0:
            print("input number must be positive")
            raise Exception(nb)
        else:
            for i in range(nb):
                print(f"Day {i + 1}")
    except Exception as e:
        print(f"invalid input {e}")