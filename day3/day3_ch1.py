
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
    largests = [jolt[i] for i in range(12)]
    for i in range(12, 0, -1):
        print("iteration nb :", i)
        for j in range(abs(i-12)+1, n - i):
            print("  nb : ", jolt[j])
            if int(jolt[j]) > int(largests[abs(i-12)]):
                largests[abs(i-12)] = jolt[j]
    s = ''
    for nb in largests:
        s = s + nb
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

if __name__ == "__main__":
    # main()
    main_test()