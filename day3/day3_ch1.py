
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
    largests = [0 for _ in range(12)]
    i = 0
    jolt_max = jolt[0]
    for j in range(12):
        print("iteration: ", j)
        while jolt_max < jolt[i] and n-i > j:
            
            print(".  jolt: ", jolt[i-1], i-1)
            print(".  largests: ", largests[j], j)
            largests[j] = jolt[i]
            i = i + 1

    s = ''
    for nb in largests:
        s = s + str(nb)
    return int(s)


def main() -> None:
    jolts = load_jolts("jolts.txt")
    code = 0
    for jolt in jolts:
        code = code + get_largest(jolt)
    print(code)

def main_test():
    jolts = load_jolts("jolts_test.txt")
    code = 0
    for jolt in jolts:
        code = code + get_largest_12(jolt)
    print(code)

def main_test2():
    a = "234234234234278"
    print(get_largest_12(a))


if __name__ == "__main__":
    # main()
    main_test2()