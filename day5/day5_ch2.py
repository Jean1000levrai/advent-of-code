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


def main() -> None:
    ranges = load_ranges_only("id_test.txt")

    a = valid(ranges)

    code = 0

    for rang in a:
        for nb in range(rang[0], rang[1]+1):
            pass

    print(code)

if __name__ == "__main__":
    main()