import numbers
import sys


class DenominatorZero(Exception):
    def __init__(self, denominator):
        super.__init__()
        self.denominator = denominator

    def __str__(self):
        return "Denominator cannot be Zero."


class NotIntError(Exception):
    def __init__(self, numerator, denominator):
        super.__init__()
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "Numerator {} and Denominator {}  must be integers.".format(self.numerator, self.denominator)


class NotProperFraction(Exception):
    def __init__(self, numerator, denominator):
        super.__init__()
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "The fraction {} / {} is not proper.".format(self.numerator, self.denominator)


class ProperFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        try:
            if not isinstance(numerator, numbers.Integral) or not isinstance(denominator, numbers.Integral):
                raise NotIntError(numerator, denominator)
            if self.denominator == 0:
                raise DenominatorZero(denominator)
            if abs(numerator / denominator) > 1:
                raise NotProperFraction
        except NotIntError as err:
            print(err)
            return sys.exit
        except DenominatorZero as err:
            print(err)
            return sys.exit()
        except NotProperFraction as err:
            print(err)
            return sys.exit()

    def __str__(self):
        return "[{}/{}]".format(self.numerator, self.denominator)

    def set_common_denominator(self, other):
        if isinstance(other, ProperFraction):
            new_denom = self.denominator * other.denominator
            self.numerator = self.numerator * other.denominator
            other.numerator = other.numerator * self.denominator
            self.denominator = new_denom
            other.denominator = new_denom
            return self, other
        else:
            NotImplemented

    def __add__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            self.numerator = self.numerator + other.numerator
            return self
        else:
            NotImplemented

    def __sub__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            self.numerator = self.numerator - other.numerator
            return self
        else:
            NotImplemented

    def __mul__(self, other):
        if isinstance(other, ProperFraction):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
            return self
        else:
            NotImplemented

    def __truediv__(self, other):
        if isinstance(other, ProperFraction):
            self.numerator *= other.denominator
            self.denominator *= other.numerator
            return self
        else:
            NotImplemented

    def __eq__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator == other.numerator
        else:
            NotImplemented

    def __ne__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator != other.numerator
        else:
            NotImplemented

    def __gt__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator > other.numerator
        else:
            NotImplemented

    def __lt__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator < other.numerator
        else:
            NotImplemented

    def __ge__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator >= other.numerator
        else:
            NotImplemented

    def __le__(self, other):
        if isinstance(other, ProperFraction):
            ProperFraction.set_common_denominator(self, other)
            return self.numerator <= other.numerator
        else:
            NotImplemented
