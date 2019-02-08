import math as m

class Complex:

    def __init__(self, re=None, im=None):
        if(type(re) == Complex):
            self.re = re.re
            self.im = re.im
        elif (re is None) and (im is None):
            self.re = 0.
            self.im = 0.
            #print("rise of evel")
        elif (re is not None) and (im is None):
            self.re = re
            self.im = 0.
        else:
            self.re = re
            self.im = im

    def __abs__(self):
        return (self.re**2 + self.im**2 )**0.5

    def __mul__(self, other):
        if type(other) == Complex:
            result = Complex()
            result.re = self.re*other.re - self.im*other.im
            result.im = self.re*other.im + self.im*other.re
        else:
            result = Complex()
            result.re = self.re * other
            result.im = self.im * other

        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if type(other) == Complex:
            result = Complex()
            result.re = self.re + other.re
            result.im = self.im + other.im
        #elif type(other) == str:

        else:
            result = Complex()
            result.re = self.re + other
            result.im = self.im
            return result
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        if self.im >= 0.:
            return str(self.re) + " + " + str(self.im) + "*i \n"
        else:
            return str(self.re) + " - " + str(abs(self.im)) + "*i \n"

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __invert__(self):
        return Complex(self.re, -self.im)

    def __truediv__(self, other):
        other = Complex(other)
        r = self * ~other
        d = (other * ~other).re
        return Complex(r.re/d, r.im/d)



def exp(arg : Complex) -> Complex:
    return m.exp(arg.re) * Complex(m.cos(arg.im), m.sin(arg.im))

def integration(function, a, b):
    N = 1000
    h = (b-a)/N



a = Complex(3,4)
b = Complex(-1,-1)
a.f()
print(a)