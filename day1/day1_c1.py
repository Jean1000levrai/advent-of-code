def load_rotations(file: str) -> list[str]:
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def exe_one_rotation(rotation: str, dial: int, code: int) -> tuple[int, int]:
    value = int(rotation[1:])
    if rotation[0] == 'L':
        dial = (dial - value) % 100
    else:  # 'R'
        dial = (dial + value) % 100

    if dial == 0:
        code += 1

    return dial, code


def main() -> None:
    rotations = load_rotations("./passcode.txt")
    dial = 50
    code = 0

    for rot in rotations:
        dial, code = exe_one_rotation(rot, dial, code)

    print(code)

if __name__ == "__main__":
    main()
