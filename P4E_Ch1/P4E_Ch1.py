#name = input('Enter file:')
handle = open("Ch1.txt", 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

print("Ridicarea la putere ", 2 ** 4)

print("Qoutient " , 7 // 3) # e 2 quotient
print("Remainder" , 7%3) #e 1 remainder


#ask user for input
inp = input("Input o ceva: ")
print("Asta a bagat in input: " + inp)