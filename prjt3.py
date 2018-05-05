r,c = int(input()),int(input())
a = [[0 for x in range(r+1)] for y in range(c+1)]
i = 0
j = 0
k = 0
def Matrix():
    for i in range(0,r):
        l = input()
        bd = list(l)
        length = len(bd)
        for j,k in zip(range(r+1),range(length)):
            a[i][j] = bd[k]
            j = j + 1
            k = k + 1
Matrix()
n = [[0 for x in range(r+1)]for y in range(c+1)]
p = 0
for i in range(0,r):
    for j in range(0,c):
        if i == 0:
            if a[i][j] != '*':
                p = p+1
                n[i][j] = p
                
        else:
            if a[i][j] != '*' and (j == 0 or a[i][j-1] == '*' or a[i-1][j] == '*'):
                p = p + 1
                n[i][j] = p
print ("PUZZLE #")                 
print("ACROSS")
str1 = ""
for i in range(0,r):
   for j in range(0,c):
       if a[i][j] !='*':
            str1 = str1 + (a[i][j])
       if a[i][j] == '*' or j == c-1:
           if a[i][j] == '*' and a[i][j-1] != '*' and j != 0 and j != c-1:
               print (str(n[i][j-len(str1)]) + '.' + str1)
               str1 = ""
           if j == c-1 and a[i][j] != '*':
               j = j+1
               print(str(n[i][j-len(str1)]) + '.' + str1)
               str1 = ""
           if j == c-1 and a[i][j] == '*' and a[i][j] != '*':
               print(str(n[i][j-len(str1)]) + '.' + str1)
               str1 = ""
           if j == c-1 and a[i][j] == '*':
               print(str(n[i][j-len(str1)]) + '.' + str1)
               str1 = ""
print("DOWN")
dic = {}
str2 = ""
for j in range(0,c):
    for i in range (0,r):
        if a[i][j] != '*':
            str2 = str2 + (a[i][j])
        if (a[i][j] == '*' and i != 0) or i == r-1:
            if a[i][j] == '*' and a[i-1][j] != '*' and i != r-1:
                dic[n[i-len(str2)][j]] = str2
                str2 = ""
            if i == r-1 and a[i][j] != '*' :
                i = i+ 1
                dic[n[i-len(str2)][j]] = str2
                str2 = ""
            if i == r - 1 and a[i][j] == '*' and a[i-1][j] != '*':
                dic[n[i-len(str2)][j]] = str2
                str2 = ""
cross_word = dic.keys()
for key in sorted(cross_word):
    print("%s.%s"%(key,dic[key]))        



 
