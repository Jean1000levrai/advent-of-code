def load_rolls(file: str) -> list[str]:
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def count_adj(i: int, j: int, grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue

            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni][nj] == '@':
                    count += 1

    return count



def main() -> None:
    grid = load_rolls("rolls.txt")
    rows = len(grid)
    cols = len(grid[0])

    accessible = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@' and count_adj(i, j, grid) < 4:
                accessible += 1

    print(accessible)

if __name__ == "__main__":
    main()