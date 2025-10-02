import random
def generate_pass(name):
    s = name + str(random.randint(1,10) )+str(chr(random.randint(ord('@'),ord('o'))))
    return s
    
    
print(generate_pass('Rahul'))