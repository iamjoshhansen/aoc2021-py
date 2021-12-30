def numbers():
    for i in range(5):
        yield i


print("for loop")
for i in numbers():
    print(i)

print("to array")
print(list(numbers()))

print("To tuple")
print(tuple(numbers()))

print("len")
print(len(tuple(numbers())))
