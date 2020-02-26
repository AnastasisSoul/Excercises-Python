list = [0, 0, 0, 0, 0, 0, 0 ,0 ,0]
i = 0
f = open('my_file.txt', 'r')
list1 = f.read()
list2 = list1.split()
for i in range(0,8):
    list[i] =int(list2[i])
matrix = [list[0:3], list[3:6], list[6:9]]
for i in range(0,3):
    print(matrix[i])
D = 0
for i in range(0,3):
    if (i==0):
        D = D + list[i]*(list[i+4]*list[i+8]-list[i+5]*list[i+7])
    else:
        if (i==1):
            D = D - list[i]*(list[i+2]*list[i+7]-list[i+4]*list[i+5])
        else:
            D = D + list[i]*(list[i+1]*list[i+5]-list[i+2]*list[i+4])
print('D =',D)
f.close()
