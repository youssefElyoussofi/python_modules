# def recursive(nb,day):
#     if nb != 0:
#         print(f"Day {day}")
#         recursive(nb - 1,day + 1)

# def ft_count_harvest_recursive():
#     try:
#         nb = int(input("Days until harvest: "))
#         if (nb < 0):
#             raise Exception(nb)
#         recursive(nb,1)
#     except Exception as e:
#         print(f"Invalid Input {e}")
#         ft_count_harvest_recursive()


def ft_count_harvest_recursive():
    while True: # i am using while here instead recursive because recursive limited in python about 1000 frame
        try:
            nb = str(input("Days until harvest: "))
            if not nb:
                raise Exception("EOF")
            if (nb < 0):
                raise Exception(nb)
            def recursive(nb,day)-> None:
                if nb > 0:
                    print(f"Day {day}")
                    recursive(nb - 1,day + 1)
            recursive(nb,1)
            break
        except ValueError as e:
            print(f"Value Error : {e}")
        except RecursionError as e:
            print(f"Recursion Error : {e}")
        except Exception as e:
            print(f"Invalid Input {e}")
        

