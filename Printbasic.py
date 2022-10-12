print ('%5.1f磅 %8.2f\n'*3%(1.5,2.35*1.5,5.5,2.35*5,10,2.35*10))
print ('%-15s%7.2f\n'*3 %('coffee',33,'Pie',2.5,'Coffee',5.2))
#Print a Pyramid

for n in range(10):
    print(" "*(9-n)+"$"*(2*n+1))

#Print 9*9 乘法表
for i in range(1,10):
    print(('┣'if i>1 else '┏')+('━'*8+'╋')*(i-1)+'━'*8+'┓')
    for j in range(1,i+1):
        print ("┃%2s×%-2s=%2s" % (j,i,i*j), end = "")
    print('┃')
print('┗'+('━'*8+'┻')*8+'━'*8+'┛')