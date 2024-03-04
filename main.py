"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec

  if ((len(xvec) <= 1) | (len(yvec) <= 1)):
    return BinaryNumber(x.decimal_val * y.decimal_val)
  else:
    xvec, yvec = pad(xvec, yvec)
    A, B = split_number(xvec)
    C, D = split_number(yvec)
    AC = subquadratic_multiply(A, C)
    BD = subquadratic_multiply(B,D)
    
    AC_shift = bit_shift(AC, len(xvec))
    BD_shift = bit_shift(BD, len(yvec))

    Product_Sums = subquadratic_multiply((A.decimal_val + B.decimal_val),(C.decimal_val + D.decimal_val))

    Combined_Prod_Sums = (Product_Sums - AC - BD)

    New_A = pad(AC,BD)
    New_B = pad(Combined_Prod_Sums, BD)

    Final_Ans = New_A + New_B + BD


    return Final_Ans
    
    
    ### TODO
    pass
    ###



def time_multiply(x, y, f):
    start = time.time()
    subquadratic_multiply(x, y)# multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

