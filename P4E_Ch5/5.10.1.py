total = 0
count = 0
avg = 0
inp = ""

while True:

    try:
        line = input('> ')
        if line == 'done':
            break
        linie = int(line)
        total = total + linie
        count = count + 1



    except:
        print("You have not entered a number!")



avg = total / count
print(total, count, avg)

