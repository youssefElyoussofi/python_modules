import sys

def command_quest():
    print("=== Command Quest ===")
    total = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    for item in sys.argv:
        if item == sys.argv[0]:
            continue
        print(f"Argument {total}: {item}")
        total += 1
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    command_quest()