import random
from decimal import *

class Qualean:
    '''
    This class is inspired by Boolean+Quantum Concepts.
    The Qualean variable can take only three values : True, False, and Maybe 
    represented as (1, 0, -1).'''
    QTrue = 1
    QFalse = 0
    QMaybe = -1
    MsgInvalid = 'Argument is of inappropriate type.'
    # constructor
    def __init__(self, state = QTrue):
        # sanity check the input
        if state > Qualean.QTrue or state < Qualean.QMaybe:
            raise ValueError('Inappropriate value for Qualean. Valid values are [-1, 0, 1].')
        # examine input
        if state == Qualean.QFalse:
            value = Qualean.QFalse
        elif state > 0:
            value = Qualean.QTrue
        else:
            value = Qualean.QMaybe
        # get the processed imaginary value and
        # store the imaginary state.
        self.number = self.gen_internal_state(value) 

    # generate the internal state.
    # Use ROUND_HALF_EVEN to perform banker's rounding to 10 decimal precision.
    # Get the random number random.uniform() distribution.
    def gen_internal_state(self, value):
        with localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = ROUND_HALF_EVEN
            dec = ctx.create_decimal_from_float(random.uniform(-1,1))
            #generate the imaginary state
            if value != Qualean.QFalse:
                return(dec * value)
            else:
                return(Decimal(Qualean.QFalse))

    # utility method - returns Decimal with appropriate prec and rounding
    def get_with_precision(self, b):
        with localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = ROUND_HALF_EVEN
            result = ctx.create_decimal(b)
            return result

    # utility method - returns Decimal from float with appropriate prec and rounding
    def get_with_precision_from_float(self, b):
        if type(b) != float:
            raise TypeError('Mismatch in datatype. Valid input type is float.')
        # gen decimal
        with localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = ROUND_HALF_EVEN
            result = ctx.create_decimal_from_float(b)
            return result

    # print and debug utilities
    def __repr__(self):
        return f'Qualean Class Instance'

    def __str__(self):
        return f'Qualean String for number: ' + str(self.number)

    def return_qualean(self):
        return float(self.get_with_precision(self.number))

    ## unary operations
    def __float__(self):
        return float(self.number)

    def __bool__(self):
        return bool(self.number)

    def __int__(self):
        return int(self.number)

    def __pos__(self):
        return self.number

    def __neg__(self):
        return self.number * -1

    ############# math operations
    # absolute
    def __abs__(self):
        return abs(self.number)

    # truncation operation
    def __trunc__(self):
        return self.number.__trunc__()

    # return with inverted sign
    def __invertsign__(self):
        return float(self.number * -1)

    # square root
    def __sqrt__(self):
        if self.number > 0:
            return self.number.sqrt()
        elif self.number < 0:
            # for negative numbers
            # make it postive and add i at the end
            res = (self.number * -1).sqrt()
            return str(round(res, 10)) + str('i')

    ########## comparison operations
    # equal-to
    def __eq__(self, b):
        if isinstance(b, Qualean):
            return self.number == b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return self.number == b
        else:
            raise TypeError(Qualean.MsgInvalid)

    # less than
    def __lt__(self, b):
        if isinstance(b, Qualean):
            return self.number < b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return self.number < b
        else:
            raise TypeError(Qualean.MsgInvalid)

    # less than or equal to
    def __le__(self, b):
        if isinstance(b, Qualean):
            return self.number <= b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return self.number <= b
        else:
            raise TypeError(Qualean.MsgInvalid)

    # greater than
    def __gt__(self, b):
        if isinstance(b, Qualean):
            return self.number > b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return self.number > b
        else:
            raise TypeError(Qualean.MsgInvalid)

    # greater than or equal to
    def __ge__(self, b):
        if isinstance(b, Qualean):
            return self.number >= b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return self.number >= b
        else:
            raise TypeError(Qualean.MsgInvalid)

    ## logical operations
    def __and__(self, b):
        if isinstance(b, Qualean):
            return self.number.__bool__() and b.__bool__()
        elif b is None:
            return self.number.__bool__() and bool(b)
        else:
            raise TypeError(Qualean.MsgInvalid)

    def __or__(self, b):
        if isinstance(b, Qualean):
            return self.number.__bool__() or b.__bool__()
        elif b is None:
            return self.number.__bool__() or bool(b)
        else:
            raise TypeError(Qualean.MsgInvalid)

    # math operations
    # multiplication
    def __mul__(self, b):
        if isinstance(b, Qualean):
            return float(self.number) * b.return_qualean()
        elif (type(b) == int) or (type(b) == float):
            return float(self.number) * b
        else:
            raise TypeError(Qualean.MsgInvalid)

    """ you can add two qualeans
    decimal + int  => allowed
    decimal + float => not allowed, need conversion.
    addition operation """
    def __add__(self, b):
        if isinstance(b, Qualean):
            return float(self.number) + b.return_qualean()
        elif type(b) == int:
            return float(self.number + b)
        elif type(b) == float:
            return float(self.number) + b
        else:
            raise TypeError(Qualean.MsgInvalid)

    # subtract operation
    def __sub__(self, b):
        if isinstance(b, Qualean):
            return float(self.number) - b.return_qualean()
        elif type(b) == int:
            return float(self.number - b)
        elif type(b) == float:
            return float(self.number) - b
        else:
            raise TypeError(Qualean.MsgInvalid)
