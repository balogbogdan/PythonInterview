lst = list()
total = 0
count = 0
largest = "None"
smallest = "None"
while True:

    try:
        line = input('> ')
        if line == 'done':
            break
        line = int(line)
        lst.append(line)
        total = total + line
        count = count + 1

    except:
        print("You have not entered a number!")

for numbers in lst:
    if largest == "None" or numbers>largest:
        largest = numbers
    if smallest == "None" or numbers<smallest:
        smallest = numbers
print(total, count, largest, smallest)