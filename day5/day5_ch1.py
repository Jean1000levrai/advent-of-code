
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

def valid(ranges: list[str]) -> tuple[tuple[int, int], ...]:
    rep = []
    for rang in ranges:
        left, right = map(int, rang.split('-'))
        rep.append((left, right))
        
    return tuple(rep)



def main() -> None:
    ranges, ids = load_ranges("id.txt")

    # print(ids, ranges)

    a = valid(ranges)

    print("valid ok")
    code = 0

    n = len(ids)
   
    for i in range(n):
        print("iterated: ", i)
        for rang in a:
            if rang[0] <= int(ids[i]) <= rang[1]:
                code += 1
                break

    print(code)
if __name__ == "__main__":
    main()