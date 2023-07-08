def num2(**x):
    print(type(x))

    # print(x[0]+x[1])
    ss =  x['num']
    sa = x['num1']
    # c = x[0]+x[1]+x[2]+x[3]
    # print(ss)
    return ss,sa
v = num2(num = 90,num1 = 80)
print(v)
