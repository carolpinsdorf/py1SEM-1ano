import os
os.system ("clear")

# a= True b=False c=not True d=not False
#1. a and b or d
resp = True and False or not False
print(f"A resposta 1 é: ", resp)
#2. d or b and a
resp2 = not False or False and True
print(f"A resposta 2 é: ", resp2)
#3. c and a or b
resp3 = not True and True or False
print(f"A resposta 3 é: ", resp3)
#4. d or (a and b) or d
resp4 = not False or (True and False) or not False
print(f"A resposta 4 é: ", resp4)




