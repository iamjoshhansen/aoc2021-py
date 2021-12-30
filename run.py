import time
import sys
import datetime


class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    DARK = f'\u001b[38;5;{232}m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = f'\u001b[38;5;{239}m'
    DIMBG = f'\u001b[48;5;{236}m'
    GREENBG = f'\u001b[48;5;{120}m'


def run(solve, day: int, part=1):
    print()
    partName = ("", " - part 2")[part-1]
    print(f"{clr.HEADER}Solving Day {day}{partName}{clr.RESET}")
    start = time.time()
    inputDir = 'input-examples'
    if len(sys.argv) > 1:
        inputDir = f"{sys.argv[1]}"
    inputPath = f"{inputDir}/{day:02}.txt"
    print(f"{clr.DIM}{inputPath}{clr.RESET}")
    with open(inputPath) as f:
        input = '\n'.join([line.strip() for line in f])
        answer = solve(input)
    end = time.time()
    duration = end - start
    print()
    print(f"{clr.DIM}Duration: {clr.BOLD}{datetime.timedelta(duration)}ms{clr.RESET}")
    print()
    print(f"{clr.DARK}{clr.GREENBG} {answer} {clr.RESET}")
    print()
