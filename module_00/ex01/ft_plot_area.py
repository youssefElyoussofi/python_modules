def ft_plot_area():
    try:
        width = int(input("enter width : "))
        lenght = int(input("enter lenght : "))
        print(f"the plot area is : {width + lenght}")
    except ValueError as e:
        print(f"this input have : {e}")

