

print("Type integers, each followed by Enter")

total = 0
count = 0

while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as e:
            print(e)
            continue

        total += number
        count += 1
    else:
        break

if count:
    print("count =", count, "total = ", total, "mean = ", total / count)
