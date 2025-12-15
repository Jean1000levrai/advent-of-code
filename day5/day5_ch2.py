from day5_ch1 import *

def load_ranges_only(file: str):
    i = 0
    char = ''
    with open(file, "r") as f:
        content = f.read()
        while char != ' ':
            char = content[i]
            if char == ' ':
                print
                break
            i += 1
        return [line.strip() for line in content[:i].splitlines() if line.strip()]

def valid(ranges: list[str]) -> tuple[tuple[int, int], ...]:
    rep = []
    for rang in ranges:
        left, right = map(int, rang.split('-'))
        rep.append((left, right))
        
    return tuple(rep)


def main() -> None:
    ranges = load_ranges_only("id_test.txt")

    a = []

    code = 0

    for rang in ranges:
        left, right = map(int, rang.split('-'))
        for r in a:
            if True:pass


if __name__ == "__main__":
    main()