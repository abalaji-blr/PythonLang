"""This is the assignment about defining the higher order function called
    time_it, which can take other function as parameter and returns the run
    time taken to execute that function.
"""

import time
import math
import types

def time_it(fn : 'function', *args, repetitions : int = 1, **kwargs) -> float:
    """
    This is a genralized function to call any function with
    user specified number of times and return the average
    time taken for calls

    Inputs:
        fn:         function whose average run time to be determined.
        args:       positional args to be passed to the function
        repetitions:integer type, defaults to 1, 
                    specifies how many times to call the function.
        kwargs:     keyword arguments to be passed to the function.

    Returns:
        float value -   average time taken for a call.
                        determines it based on the 'repetition'
    """
    # Repetition should be positive number
    if repetitions < 0:
        raise ValueError('Repetition should be a positive number.')
    elif repetitions == 0:
        return 0

    # check whether the other function is a function or not
    if not( isinstance(fn, (types.FunctionType, types.BuiltinFunctionType))):
        raise TypeError(f'The funciton {fn} is not a function!')

    start = time.time()
    for i in range(repetitions):
        fn(*args, **kwargs)
    end = time.time()
    avg = (end-start) / repetitions
    return(avg)

def squared_power_list(number :int, *args, start : int =0, end : int =5,**kwargs) -> list:
    """
    Returns list by raising number to power from start to end
    -> number ** start to number ** end.  

    Inputs:
        number: base number for which powers to be calculated.
        args:   positional arguments
        start:  default = 0, start value for number ** start
        end:    default = 5, end power value for number ** end
        kwargs: keqword arguments

    Returns:
        list:   power list

    Example: squared_power_list(2) -> [1, 2, 4, 8, 16]
    """

    # Validations "if" block
    if type(number) is not int:
        raise TypeError('Only integer type arguments are allowed.')

    if len(args) > 0:
        raise TypeError(
            "The function squared_power_list takes maximum 1 positional arguments")

    if len(kwargs) > 0:
        raise TypeError(
            "The function square_power_list takes maximum 2 keyword/named arguments")

    if start < 0 or end < 0:
        raise ValueError('Value of start or end can\'t be negative.')

    if end < start:
        raise ValueError("Value of start should be less than end")

    if number > 10:
        raise ValueError("Value of number should be less than 10")

    # Return the list of number to the power of numbers from start to end
    return [number ** idx for idx in range(start, end)]

def polygon_area(length : int, *args, sides : int = 3, **kwargs) -> float:
    """
    Returns area of a regular polygon with number of sides between
    3 to 6 both inclusive.

    The area is calculated using the following formula:
    area of polygon = (0.25 * sides * length ** 2) / tan(pi/sides)

    Parameters:
        length: postive integer, length for the side 
        args:   positional args
        sides:  number of sides, default=3, range: 3 to 6(inclusive)
        kwargs: keyword args.

    Returns:
        float - area of the polygon

    Example:    polygon_area(15) -> float
    """

    # Validations
    ## Validate the types of inputs
    if type(length) is not int:
        raise TypeError("The type of argument length must be integer.")

    if length < 0:
        raise ValueError("The value for argument length can not be negative.")

    if type(sides) is not int:
        raise TypeError("The type of argument sides must be integer.")

    ## Validate the args and kwargs.
    if len(args) > 0:
        raise TypeError(
            "The polygon_area function takes maximum 1 positional arguments, more provided.")

    if len(kwargs) > 0:
        raise TypeError(
            "The polygon_area function take maximum 1 keyword/named arguments, more provided.")

    ## Validate the values for the inputs
    if sides < 3 or sides > 6:
        raise ValueError("The value for argument side must be between 3 and 6 inclusive.")

    area = (0.25 * sides * length ** 2) / math.tan(math.pi/sides)
    return area

def temp_converter(temp : 'float / int', *args, temp_given_in : str = 'f', **kwargs) -> float:
    """
    Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius

    Parameters:
        temp:   input temperature value, float/int type
        *args:  positional args
        temp_given_in:  input temperature scale
        **kwargs:   keyword args

    Returns:
        temperature - float value

    Example:
        temp_converter(100), default input temp scale is fahrenheit  -> float value in celsius.
    """
    # Validations
    if type(temp_given_in) is not str:
        raise TypeError("Charcater string expected for temp_given_in.")

    if not (temp_given_in.lower() == 'f' or temp_given_in.lower() == 'c'):
        raise ValueError(
            "In the temp_converter function, Only f or c is allowed.")

    if type(temp) not in [int, float]:
        raise TypeError("The value of temp should be integer or float value.")

    if temp_given_in.lower() == 'c' and temp < -273.15:
        raise ValueError(
            "Temperature can't go below -273.15 celsius = 0 Kelvin")
    elif temp_given_in.lower() == 'f' and temp < -459.67:
        raise ValueError(
            "Temperature can't go below -459.67 fahrenheit = 0 Kelvin")

    ## validate args & kwargs
    if len(args) > 0:
        raise TypeError(
            "The temp_converter function takes maximum 1 positional arguments, more provided")

    if len(kwargs) > 0:
        raise TypeError(
            "The temp_converter function take maximum 1 keyword/named arguments, more provided.")

    # compute other temperature.
    result = None
    if temp_given_in.lower() == 'f':
        # convert from fahrenheit to celsius
        result = (temp - 32) * (5/9)
    elif temp_given_in.lower() == 'c':
        # convert from celsius to farenheit
        result = (temp * 9/5) +32

    return result

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """
    Converts input speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day.

    Parameters:
        speed: float / int type, speed in kmph
        *args: positional args
        dist:   km / m / ft / yrd
        time:   ms / s / min / hr / day

    Returns:
        float value  - result speed in required units.

    Example: 
        speed_converter(100) -> speed float value in km/min (defaults for dist and time)
    """

    # Validations
    if type(speed) not in [int, float]:
        raise TypeError("Speed can be int or float type only.")

    if speed < 0:
        raise ValueError("Speed can't be negative")
    elif speed > 300000:
        raise ValueError("Speed can't be greater than speed of light.")

    if len(args) > 0:
        raise TypeError(
            "speed_converter function takes maximum 1 positional arguments, more provided.")

    if type(dist) is not str:
        raise TypeError('Charcater string expected for distance unit.')

    if type(time) is not str:
        raise TypeError("Charcater string expected.")

    if len(kwargs) > 0:
        raise TypeError(
            "speed_converter function take maximum 2 keyword/named arguments, more provided.")

    if dist.lower() not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError(
            "Incorrect unit of distance. Only km/m/ft/yrd allowed.")

    if time.lower() not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError(
            "Incorrect unit of Time. Only ms/s/min/hr/day allowed.")

    # the input speed is kmph.
    #for 1 km
    dist_dict = { 'km': 1, 'm' : 1000, 'ft': 3280.84, 'yrd': 1093.61 }

    # for 1 hour
    time_dict = { 's' : 3600, 'ms': 3600000, 'min': 60, 'hr': 1, 'day':0.0416667 }

    result = (speed * dist_dict[dist.lower()] ) / time_dict[time.lower()]
    return round(result)