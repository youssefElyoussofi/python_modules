
def garden_operations()->None:

    print("Testing ValueError..")
    try:
        _ = int("test")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    
    print("Testing ZeroDivisionError..")
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        file = open("note.txt")
        file.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file {e.filename}")
    
    print("Testing KeyError...")
    try:
        data = {"total":5,"students":3}
        m = data["mangers"]
    except KeyError as e:
        print(f"Caught KeyError: 'missing{e}'")

    print("Testing multiple errors together...")
    try:
        _ = int("test")
    except Exception:
        print("Caught an error, but program continues!")

def test_error_types()->None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()