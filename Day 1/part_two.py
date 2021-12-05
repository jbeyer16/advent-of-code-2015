from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        line = fobj.readline()

    return line


def main():
    instructions = read_file("input")

    floor = 0
    for position, instruction in enumerate(instructions, start=1):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            raise NotImplementedError(f"Invalid instruction {instruction}.")

        if floor == -1:
            break

    return position


if __name__ == "__main__":
    print("\n~~ Day 1 - Part Two ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
