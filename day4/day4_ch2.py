from day4_ch1 import *

def main() -> None:
    temp = load_rolls("rolls.txt")
    rows = len(temp)
    cols = len(temp[0])
    grid = [[] for i in range(rows)]
    for i in range(rows):
        for char in temp[i]:
            grid[i].extend(char)

    itera = 0

    accessible = 0
    removed = 0
    while True:
        accessible = 0
        itera += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@' and count_adj(i, j, grid) < 4:
                    accessible += 1
                    removed += 1
                    grid[i][j] = '.'

        if accessible == 0 or itera > 999999:
            break
    
    print(removed)

if __name__ == "__main__":
    main()