
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
    for i in range(i_l, n):
        if int(jolt[i]) > int(largest2):
            largest2 = jolt[i]
    
    return int(largest1) + int(largest2)
    


def main() -> None:
    pass

def main_test():
    # a = load_jolts("jolts_test.txt")
    # print(a)
    # code = 0
    # for jolt in a:
    #     code = code + get_largest(jolt)
    # print(code)
    b = get_largest('987654321111111')
    print(b)

if __name__ == "__main__":
    main_test()
    # main()