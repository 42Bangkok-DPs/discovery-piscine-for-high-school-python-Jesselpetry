#!/usr/bin/env python3
print("Enter the first number : ")
n1 = int(input())
print("Enter the second number : ")
n2 = int(input())

mult = n1 * n2

print(f"{n1} x {n2} = {mult}")

if mult < 0:
    print("This number is negative.")
elif mult > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
    