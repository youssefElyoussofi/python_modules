def check_temperature(temp_str :str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        tmp = int(temp_str)
        if tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {tmp}°C is perfect for plants")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
    except Exception as e:
        print(e)

def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_temperature_input()