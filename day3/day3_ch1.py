
def load_jolts(file: str) -> list[int]:
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def get_largest(jolt: str) -> int:
    n = len(jolt)
    i_l = 0
    largest1 = jolt[i_l]
    for i in range(n-1):
        if int(jolt[i]) > int(jolt[i_l]):
            largest1 = jolt[i]
            i_l = i
    largest2 = jolt[i_l+1]
    for i in range(i_l+1, n):
        if int(jolt[i]) > int(largest2):
            largest2 = jolt[i]
    
    return int(largest1 + largest2)

def get_largest_12(jolt: str) -> int:
    n = len(jolt)
    result = []
    start = 0

    for remaining in range(12, 0, -1):
        # last index we can search
        end = n - remaining + 1

        max_digit = '0'
        max_index = start

        for i in range(start, end):
            if jolt[i] > max_digit:
                max_digit = jolt[i]
                max_index = i

        result.append(max_digit)
        start = max_index + 1

    return int(''.join(result))



def main() -> None:
    jolts = load_jolts("jolts.txt")
    code = 0
    for jolt in jolts:
        code = code + get_largest_12(jolt)
    print(code)


if __name__ == "__main__":
    # main()
    main()