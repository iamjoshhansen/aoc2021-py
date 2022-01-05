from run import run


def solve(input: str):
    lines = input.splitlines()
    return len(lines)


if __name__ == "__main__":
    run(solve, 18, 1)
