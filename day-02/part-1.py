from run import run


class Submarine:
    x: int = 0
    y: int = 0

    def forward(self, n: int):
        self.x += n

    def down(self, n: int):
        self.y += n

    def up(self, n: int):
        self.y -= n


def dive(input: list[str]):

    submarine = Submarine()

    for command in input:
        [word, amount] = command.split(' ')

        if (word == 'forward'):
            submarine.forward(int(amount))
        elif (word == 'down'):
            submarine.down(int(amount))
        elif (word == 'up'):
            submarine.up(int(amount))

    print(f"x: {submarine.x} y: {submarine.y}")
    return submarine.x * submarine.y


if __name__ == "__main__":
    run(dive, 2, 1)
