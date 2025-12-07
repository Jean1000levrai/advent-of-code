def load_products(file: str) -> list[str]:
    with open(file, "r") as f:
        content = f.read()
        return [word.strip() for word in content.split(',')]

def valid(s: str) -> str:
    n = len(s)

    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    p = pi[-1]

    if p > 0 and n % (n - p) == 0:
        return s[:n - p]
    else:
        return 0

def check_one_range(range_product: str, code: int) -> int:
    dash = range_product.index('-')
    left = range_product[:dash]
    right = range_product[dash+1:]
    for i in range(int(left), int(right)):
        code = code + int(valid(str(i)))
    return code

def main() -> None:
    products = load_products("product.txt")
    code = 0
    for prod in products:
        code = code + check_one_range(prod, code)
    print(code)

if __name__ == "__main__":
    main()
