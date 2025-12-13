
def load_ids(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read()
        return [line.strip() for line in content.splitlines() if line.strip()]

def load_ranges(file: str):
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
        return ([line.strip() for line in content[:i].splitlines() if line.strip()], 
        [line.strip() for line in content[i:].splitlines() if line.strip()])

def valid(ranges: list[str]) -> str:
    pass

def is_valid(prod: int, ranges: str) -> int:
    pass

def main_test() -> None:
    ranges, ids = load_ranges("id_test.txt")

    print(ids, ranges)

def main() -> None:
    pass

if __name__ == "__main__":
    main_test()