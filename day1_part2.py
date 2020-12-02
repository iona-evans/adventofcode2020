input_file = open("day1_input.txt")

list1 = list(range(0))

line = input_file.readline()

while line != "":
    num = int(line)
    list1.append(num)
    line = input_file.readline()

print (list1)
print (len(list1))

def find3Numbers(A, arr_size, total):
    A.sort()
    for i in range(0, arr_size - 2):

        l = i + 1

        r = arr_size - 1
        while l < r:

            if A[i] + A[l] + A[r] == total:
                print("Triplet is", A[i],
                      ', ', A[l], ', ', A[r])
                return True

            elif A[i] + A[l] + A[r] < total:
                l += 1
            else:  
                r -= 1

    return False


A = list1
total = 2020
arr_size = len(A)

find3Numbers(A, arr_size, total)