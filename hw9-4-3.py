# Author: JD 01/14/2022

def count_e(word):
    num = 0
    for x in word:
        if x == "e":
            num += 1
    
    return num

a = count_e("apple")
b = count_e("especially")
c = count_e("eeeeeeeeee")
print(a,b,c)