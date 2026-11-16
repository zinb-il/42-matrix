import math

class Complex():
    """mon propre calss pour des nombres complex
    """
    
    def __init__ (self, re: float = 0.0, im:float = 0.0):
        self.re = re
        self.im = im
    
    def __add__(self, c:'Complex'):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return Complex(self.re + c.re, self.im + c.im)

    def __iadd__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return self + c
        
    def __sub__(self, c:'Complex'):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return Complex(self.re - c.re, self.im - c.im)

    def __rsub__(self, c:'Complex'):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return Complex(c.re - self.re, c.im - self.im)

    def __isub__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return self - c

    def __mul__(self, c:'Complex'):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        re = self.re * c.re - self.im * c.im
        im = self.re * c.im + self.im * c.re
        return Complex(re, im)

    def __truediv__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        denom = c.re ** 2 + c.im ** 2
        re = (self.re * c.re + self.im * c.im) / denom
        im = (self.im * c.re - self.re * c.im) / denom
        return Complex(re, im)

    def __rtruediv__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return c / self
    
    def __repr__(self):
        return f"Complex({self.re!r}, {self.im!r})"

    def __eq__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return self.re == c.re and self.im == c.im


    def __str__(self):
        re = int(self.re) if isinstance(self.re, float) and self.re.is_integer() else self.re
        im = int(self.im) if isinstance(self.im, float) and self.im.is_integer() else self.im

        if im == 0:
            return f"({re}+0i)"
        if re == 0:
            return f"{im}i"
        
        signe = "+" if im >= 0 else "-"
        return f"({re}{signe}{abs(im)}i)"
    
    def _my_abs__(self):
        return(self.re ** 2 + self.im ** 2) ** 0.5

    def __gt__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return self._my_abs__() > c._my_abs__()

    def __lt__(self, c):
        if isinstance(c, (int, float)):
            c = Complex(c)
        if not isinstance(c, Complex):
            return NotImplemented
        return self._my_abs__() < c._my_abs__()
    
    def __neg__(self):
        return Complex(-self.re, -self.im)
    
    def __pow__(self, n: float):
        r = ((self.re ** 2 + self.im ** 2) ** 0.5) ** n
        theta = math.atan2(self.im, self.re) * n
        r_n = r * math.cos(theta)
        im_n = r * math.sin(theta)
        return Complex(r_n, im_n)
        
        
    
    __radd__ = __add__
    __rmul__ = __mul__