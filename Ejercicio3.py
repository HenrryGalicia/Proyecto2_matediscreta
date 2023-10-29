def euclides_mcd(x, b):
    if b == 0:
        return x
    else:
        return euclides_mcd(b, x % b)

numero1 = 150
numero2 = 39

mcd = euclides_mcd(numero1, numero2)

print("El MCD de", numero1, "y", numero2, "es:", mcd)
