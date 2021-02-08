''' 
# 0666 1666 2666 3666 4666 5666 6
6660 6661 6662 6663 6664 6665 6666 6667 6668 6669 10
# 10666 11666 12666 13666 14666 15666
16660 16661 16662 16663 16664 16665 16666 16667 16668 16669
# 20666 21666 22666 23666 24666 25666
26660 26661 26662 26663 26664 26665 26666 26667 26668 26669
# 30666
'''
import time
N = int(input())
#start = time.time()
lst = []
count = 0
anw = '666'
while True:
    for i in range(len(anw)-2):
        if anw[i] == '6' and anw[i+1] == '6' and anw[i+2] == '6':
            count += 1
            break
    if count == N:
        print(anw)
        break
    anw = str(int(anw) + 1)
     
#print(time.time()-start)