print("Type integers, each followed by Enter; ")

total = 0
count = 0

while True:
    line = input()
    try:
        number = int(line)
        total += number
        count += 1
    except ValueError as e:
        print(e)
        continue
    except EOFError:
        break


if count:
    print("count =", count, "total = ", total, "mean = ", total / count)
