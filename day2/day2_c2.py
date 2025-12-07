from day2_c1 import load_products

def valid_debug(s: str) -> str:
    n = len(s)
    good = True
    for i in range(1, n//2 + 1):
        print(f"iteration {i}", f"n % {i} = ", n%i)
        if n % i == 0:
            print("  loops : ", n//i,";i = ", i)
            # if n//i == 2:
            #     print(f"    {s[:i]} == {s[i:]}")
            #     if s[:i] == s[i:]:
            #         return s
            for j in range(2, (n//i) + 1):
                print(f"    {s[:i]} == {s[i*(j-1):i*j]}")
                if s[:i] == s[i*(j-1):i*j]:
                    print("      good")
                    good = True
                else:
                    print("      break")
                    good = False
                    break
            if good:
                return s
    return '0'

def valid(s: str) -> str:
    n = len(s)
    good = True
    for i in range(1, n//2 + 1):
        if n % i == 0:
            if n//i == 2:
                if s[:i] == s[i:]:
                    return s
            for j in range(2, (n//i) +1):
                if s[:i] == s[i*(j-1):i*j]:
                    good = True
                else:
                    good = False
                    break
            if good:
                return s
    return '0'

def check_one_range(range_product: str, code: int) -> int:
    print("init code: ", code)
    init_code = code
    dash = range_product.index('-')
    left = range_product[:dash]
    right = range_product[dash+1:]
    print(range_product)
    for i in range(int(left), int(right)+1):
        print("  ", i)
        if valid(str(i)) != '0':
            print("---    ",valid(str(i)))
        code = code + int(valid(str(i)))
        print("      code: ", code)
    print("output code: ", code)
    return code - init_code

def main():
    products = load_products("product.txt")
    code = 0
    for prod in products:
        code = code + check_one_range(prod, code)
    print(code)

def main_test():
    products = load_products("new_test.txt")
    code = 0
    for prod in products:
        code = code + check_one_range(prod, code)
    print(code)

if __name__ == "__main__":
    main()