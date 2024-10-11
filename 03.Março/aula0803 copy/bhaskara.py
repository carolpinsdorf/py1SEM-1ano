import os
os.system("clear")

a= -1
b = 2
c = 3

x1 = (-b + ((b**2 - 4 *a*c)**0.5)) / 2*a
x2 = (-b - ((b**2 - 4 *a*c)**0.5)) / 2*a
delta = b**2 - 4 *a*c

print(f"""
      x1= {x1}
      x2 = {x2}
      delta = {delta}
""")
