def inputTo2dIntArray(input: str):
    return tuple(map(lambda row: tuple(map(int, row)), input.split('\n')))
