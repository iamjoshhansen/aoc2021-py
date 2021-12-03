def solve(input):
    count = 0
    for i in range(1, len(input)):
        current = input[i]
        last = input[i-1]
        isIncreasing = current > last
        print(last, "➡️", current, "+" if isIncreasing else "-")
        if isIncreasing:
            count += 1
    return count


if __name__ == "__main__":
    with open("day-01/example.txt") as f:
        input = [int(line.strip()) for line in f]

    answer = solve(input)
    print(answer)
