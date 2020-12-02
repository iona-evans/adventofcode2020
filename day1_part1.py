
# coding: utf-8

input_file = open("puzzleinput.txt")

list1 = list(range(0))

line = input_file.readline()
res = 0
while line != "":
	num = int(line)
	print (num)
	res = 2020 - num
	line = input_file.readline()
	list1.append(res)

result = list(range(0))


input_file = open("day1_input.txt")
line = input_file.readline()

while line != "":
    for number in list1:
	    if int(line) == int(number):
                result.append(line)
    line = input_file.readline()

print (result)