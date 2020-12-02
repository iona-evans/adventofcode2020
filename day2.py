filename = "day2_input.txt"
items = []

with open(filename) as f:
    for line in f.readlines():
        key, password = line.strip().split(':')
        frequency, char = key.split(" ")
        firstpos,secondpos = [int(i) for i in frequency.split("-")]
        items.append((password, char, firstpos, secondpos))


validpassword = 0

for key, val in enumerate(items):
    password = val[0]
    char = val[1]
    firstpos = val[2]
    secondpos = val[3]

    if char not in password:
        print("not valid")
        print (password,char)
    elif (char in password[firstpos]) and (char not in password[secondpos]):
        print("valid")
        print(password[firstpos],password[secondpos],char)
        validpassword = validpassword + 1
    elif (char not in password[firstpos]) and (char in password[secondpos]):
        print ("valid")
        validpassword = validpassword + 1
        print(password[firstpos], password[secondpos], char)

print(validpassword)