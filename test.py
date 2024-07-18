def divice(a, b):
    assert b!= 0, "除数不能为0"
    return a/b

def divice1(a:float, b:float)->float:
    '''
    计算两个数的商
    :param a: 被除数
    :param b: 除数
    :return: 商
    '''
    assert b!= 0, "除数不能为0"
    return a / b


print(divice(10, 2))
print(divice(10, '2'))
print(divice1(10, 2))

        
def print_upper(s:str)->str:
    '''
    打印字符串的大写版本
    :param s: 字符串
    :return: 字符串的大写版本
    '''
    return s.upper()