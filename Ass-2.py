"""
Assignment-2
Statement-Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****

"""

def ptn_pyd(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")

n=int(input("Enter the number of Rows="))
ptn_pyd(n)
