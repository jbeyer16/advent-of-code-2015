from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        line = fobj.readline()

    return line


def main():
    instructions = read_file("input")

    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise NotImplementedError(f"Invalid instruction {instruction}.")

    return floor


if __name__ == "__main__":
    print("\n~~ Day 1 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
