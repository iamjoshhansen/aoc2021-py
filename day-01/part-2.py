def solve(input: list[int], size: int):
    count = 0
    sum = input[0]
    for i in range(1, len(input)):
        last = sum
        sum += input[i]
        if (i > size-1):
            sum -= input[i-size]
            current = sum
            isIncreasing = current > last
            print(last, "➡️", current, "+" if isIncreasing else "-")
            if isIncreasing:
                count += 1
    return count


if __name__ == "__main__":
    with open("day-01/example.txt") as f:
        input = [int(line.strip()) for line in f]

    answer = solve(input, 3)
    print(answer)
