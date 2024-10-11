#!/usr/bin/env python3
print("Enter a number less than 25")
n = int(input())
if n <= 25:
    for i in range(26-n):
        print(f"Inside the loop, my variable is {n}")
        n = n+1
else:
    print("ERROR")