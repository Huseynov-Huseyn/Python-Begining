import math

# S=PI*R*R / C=2*PI*R
R = int(input("Please enter radius of circle: "))
Circumference = round(2 * R * math.pi, 2)
Area = round(math.pi * pow(R, 2), 2)
print(f"The Circumference of the circle is : {Circumference} sm")
print(f"The Area of the circle is : {Area} sm|2")

A = 9
B = 12
C = math.sqrt(pow(A, 2) + pow(B, 2))
print(C)
