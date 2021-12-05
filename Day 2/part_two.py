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

        smallest_perimeter = min([2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l])

        extra = w * l * h

        total += smallest_perimeter + extra

    return total


if __name__ == "__main__":
    print("\n~~ Day 2 - Part One ~~\n")

    answer = main()

    print(f"Answer guess: {answer}")

    print("\n~~~~~~~~~~~~~~~~~~~~~~\n")
