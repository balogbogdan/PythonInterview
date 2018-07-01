def count(string, choice):


    count = 0
    for letter in string:
        if letter == choice:
            count = count + 1
    print(count)


string = input("Input the string: ")
letter = input("Input the letter you want to count: ")

count(string,letter)

#the "in" operator
print("is a in banana?  : ", 'a' in "banana")



