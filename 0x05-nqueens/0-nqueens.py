#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard
Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, 
followed by a new line, and exit with the status 1
"""

import sys

if __name__ == '__main__':
    """
    Command line args
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    p_queens = []
    stop = False
    r = 0
    c = 0

    """
    processing the row
    """
    while r < n:
        goback = False
        while c < n:
            safe = True
            for cord in p_queens:
                col = cord[1]
                if(col == c or col + (r-cord[0]) == c or
                        col - (r-cord[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            cords = [r, c]
            p_queens.append(cords)
            if r == n - 1:
                solutions.append(p_queens[:])
                for cord in p_queens:
                    if cord[1] < n - 1:
                        r = cord[0]
                        c = cord[1]
                for i in range(n - r):
                    p_queens.pop()
                if r == n - 1 and c == n - 1:
                    p_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        if goback:
            r -= 1
            while r >= 0:
                c = p_queens[r][1] + 1
                del p_queens[r] 
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    """
    Printing solutions
    """
    for s in solutions:
        print(s)
