#70.Printing Square and Cube Values
n=int(input("Entrt the number:"))
terms = 10
result = list(map(lambda x: n ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print(f"{n} raised to power",i,"is",result[i])