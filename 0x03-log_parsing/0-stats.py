#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {m: 0 for m in codes}

    def printstats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for m, n in sorted(stats.items()):
            if n:
                print("{}: {}".format(m, n))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                statuscode = data[-2]
                if statuscode in stats:
                    stats[statuscode] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                printstats(stats, filesize)
        printstats(stats, filesize)
    except KeyboardInterrupt:
        printstats(stats, filesize)
        raise
