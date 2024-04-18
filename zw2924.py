import numpy as np

# 1. Identify yourself
def WhoAmI():
    return('zw2924')


# 2. getBondPrice


def getBondPrice(face, y, couponRate, m, ppy=1):
    t = np.arange(1, ppy*m + 1)
    pv = (1 + y/ppy) ** -t
    bond_price = (np.sum(pv) * (couponRate/ppy) + pv[-1]) * face
    
    return round(bond_price)


# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

#ppy=1
bond_price = getBondPrice(face, y, couponRate, m, ppy=1)
print(bond_price)


# 3. getBondDuration

def getBondDuration(face, y, couponRate, m, ppy=1):
    
    coupon_payment = face * couponRate / ppy
    t = np.arange(1, m * ppy + 1)
    pv = (1 + y/ppy) ** -t
    cf = np.full(t.shape, coupon_payment)
    cf[-1] += face 
    pvcf = pv * cf
    w = t * pvcf
    bond_duration = np.sum(w) / np.sum(pvcf)
    
    return round(bond_duration, 2)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10

bond_duration = getBondDuration(face, y, couponRate, m, ppy=1)
print(bond_duration)


# 4. FizzBuzz
def FizzBuzz(start, finish):

    numbers = np.arange(start, finish+1)
    results = np.empty(numbers.shape, dtype=object)
    results[:] = numbers

    results[numbers % 3 == 0] = 'Fizz'
    results[numbers % 5 == 0] = 'Buzz'
    results[(numbers % 3 == 0) & (numbers % 5 == 0)] = 'FizzBuzz'
    
    return results

# Test
print(FizzBuzz(61, 75))
