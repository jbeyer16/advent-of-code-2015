from pathlib import Path


def read_file(filename):
    input_file = Path(__file__).parent / filename

    with open(input_file, "r") as fobj:
        line = fobj.readlines()

    return line


def main():
    dimensions = [dimension.strip().split("x") for dimension in read_file("input")]

    total = 0

    for dimension in dimensions:
        l, w, h = [int(val) for val in dimension]

        surface_area = 2 * l * w + 2 * w * h + 2 * h * l

        extra = min([l * w, w * h, l * h])

        total += surface_area + extra

    return total


if __name__ == "__main__":
    print("\n~~ Day 2 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
