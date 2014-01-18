def karatsuba(x,y):
    m,k = x.bit_length(), y.bit_length()

    # anchor
    if(m < 16 and k < 16): # if both integers have less then 16 bit
        result = 0
        for _ in range(abs(y)):
            if(y < 0):
                result -= x
            else:
                result += x

        return result

    #  divide

    center = max(m,k)
    center_2 = center//2


    # partion x & y

    x_h =   x>>center_2
    x_l =   x - (x_h<<center_2)
    y_h =   y>>center_2
    y_l =   y - (y_h<<center_2)


    # call recursions

    a = karatsuba(x_h, y_h)
    b = karatsuba(x_l, y_l)
    c = karatsuba((x_h+x_l),(y_h+y_l))

    # conquer
    return c - b - a

print(karatsuba(12,13))
print(karatsuba(-17,13))
