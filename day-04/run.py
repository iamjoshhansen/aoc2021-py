import time
import sys


class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = f'\u001b[38;5;{239}m'


def run(solve, day: int, part=1):
    print()
    partName = ("", " - part 2")[part-1]
    print(f"{clr.HEADER}Solving Day {day}{partName}{clr.RESET}")
    start = time.time()
    filename = 'example'
    if len(sys.argv) > 1:
        filename = f"{sys.argv[1]}"
    path = f"day-{day:02}/{filename}.txt"
    print(f"{clr.DIM}{clr.BOLD}{filename}{clr.RESET}{clr.DIM}.txt{clr.RESET}")
    with open(path) as f:
        input = '\n'.join([line.strip() for line in f])
        answer = solve(input)
    end = time.time()
    duration = end - start
    print()
    print(f"{clr.DIM}Program duration: {clr.BOLD}{duration * 1000}ms{clr.RESET}")
    print()
    print(f"{clr.OKGREEN}{answer}{clr.RESET}")
    print()
