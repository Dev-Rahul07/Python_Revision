# we can make custom excepion by  inherting the Exception class and raise keyword


class My_exp(Exception):
    pass

try:
    
    raise My_exp('this is a Exception')
    
except My_exp as e:
    print("exption handle",e)