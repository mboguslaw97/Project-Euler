
def multiply(numer1, denom1, numer2, denom2):
    return numer1 * numer2, denom1 * denom2

def equal(numer1, denom1, numer2, denom2):
    return numer1 * denom2 == numer2 * denom1

product = (1, 1)
for denom1 in range(11, 100):
    if denom1 % 10 != 0:
        numer1 = 11
        while numer1 < denom1:
            if numer1 % 10 != 0:
                str_numer1, str_denom1 = str(numer1), str(denom1)
                for c in str_numer1:
                    if c in str_denom1:
                        numer2 = int(str_numer1.replace(c, '', 1))
                        denom2 = int(str_denom1.replace(c, '', 1))
                        if equal(numer1, denom1, numer2, denom2):
                            product = multiply(product[0], product[1], numer2, denom2)
            numer1 += 1
print(product)
