def roundup(num, place):
    return (num // place + 1) * place

products = set()
for x in range(2, 100):
    str_x = str(x)
    if '0' not in str_x and len(str_x) == len(set(str_x)):
        y = x + 1
        str_y = str(y)
        while True:
            while True:
                for i in range(len(str_y)):
                    if str_y[i] in (str_x + '0'):
                        y = roundup(y, 10**(len(str_y)-i-1))
                        str_y = str(y)
                        break
                else:
                    break
  
            str_xyprod = str_x + str_y + str(x * y)
            if '0' not in str_xyprod and len(set(str_xyprod)) == 9:
                print(x, y, x * y)
                products.add(x * y)
            if len(str_xyprod) > 9:
                break
            y += 1
            str_y = str(y)
            
print(sum(products))
        

