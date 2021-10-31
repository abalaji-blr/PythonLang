# EPAi4 Session5 - Higher Order Function - time_it

This assignment is about defining the higher order functions. Before we go specific about the definition of the higher order function for this assignment, let's understand what higher order function means.

### About Higher Order

A function is called as higher order function if **it contains other function as a parameter or returns function as an output.** ie., functions that operate with another function are called as higher order function.

The following are some of the higher order functions in Python:

* map(), filter(), reduce()
* Decorators.

### About Assignment

This assignment is to define the higher order function **time_it**, which can take other function as argument.

And also define the following functions as well.

	* squared_power_list()
	* polygon_area()
	* temp_converter()
	* speed_converter()

Let's look at each function in detail.

### time_it

* time_it(fn, *args, repetitions= 1, **kwargs)

```
time_it(fn: 'function', *args, repetitions: int = 1, **kwargs) -> float
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
```



### squared_power_list

```
squared_power_list(number: int, *args, start: int = 0, end: int = 5, **kwargs) -> list
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
```



### polygon_area

```
polygon_area(length: int, *args, sides: int = 3, **kwargs) -> float
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
```



### temp_converter

```
temp_converter(temp: 'float / int', *args, temp_given_in: str = 'f', **kwargs) -> float
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
```



### speed_converter

```
speed_converter(speed, *args, dist='km', time='min', **kwargs)
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
```



## Tests & Results

```
collected 48 items 

test_session5_readme_exists 											PASSED 				[  2%]
test_session5_readme_500_words 										PASSED  			[  4%]
test_session5_readme_proper_description 					PASSED 				[  6%]
test_session5_readme_file_for_more_than_10_hashes PASSED   			[  8%]
test_session5_indentations 												PASSED  			[ 10%]
test_session5_function_name_had_cap_letter 				PASSED 				[ 12%]
test_session5_time_it_print 											PASSED 				[ 14%]
test_session5_time_it_squared_power_list 					PASSED				[ 16%]
test_session5_time_it_polygon_area 								PASSED  			[ 18%]
test_session5_time_it_temp_converter 							PASSED				[ 20%]
test_session5_time_it_speed_converter 						PASSED   			[ 22%]
test_session5_time_it_no_args 										PASSED   			[ 25%]
test_session5_time_it_incorrect_pos_args 					PASSED				[ 27%]
test_session5_time_it_zero_rep 										PASSED  			[ 29%]
test_session5_squared_power_list_no_args 					PASSED				[ 31%]
test_session5_squared_power_list_incorrect_pos_args PASSED 			[ 33%]
test_session5_squared_power_list_incorrect_start__end PASSED   	[ 35%]
test_session5_squared_power_list_start_gt_end 				PASSED   	[ 37%]
test_session5_squared_power_list_number_gt_10 				PASSED   	[ 39%]
test_session5_squared_power_list_unwanted_args 				PASSED  	[ 41%]
test_session5_squared_power_list_output 							PASSED 		[ 43%]
test_session5_polygon_area 														PASSED  	[ 45%]
test_session5_polygon_area_length 										PASSED   	[ 47%]
test_session5_polygon_area_sides 											PASSED		[ 50%]
test_session5_polygon_area_sides_values 							PASSED 		[ 52%]
test_session5_polygon_area_length_values 							PASSED		[ 54%]
test_session5_polygon_area_unwanted_args 							PASSED		[ 56%]
test_session5_polygon_area_output 										PASSED   	[ 58%]
test_session5_temp_converter 													PASSED		[ 60%]
test_session5_temp_converter_temp 										PASSED   	[ 62%]
test_session5_temp_converter_temp_given_in 						PASSED  	[ 64%]
test_session5_temp_converter_temp_values_in_celsius 	PASSED 		[ 66%]
test_session5_temp_converter_temp_values_in_fahrenheit PASSED  	[ 68%]
test_session5_temp_converter_unwanted_args 						PASSED  	[ 70%]
test_session5_temp_converter_output_in_fahrenheit 		PASSED   	[ 72%]
test_session5_temp_converter_output_in_celsius 				PASSED  	[ 75%]
test_session5_speed_converter 												PASSED   	[ 77%]
test_session5_speed_converter_speed 									PASSED 		[ 79%]
test_session5_speed_converter_dist 										PASSED  	[ 81%]
test_session5_speed_converter_time 										PASSED  	[ 83%]
test_session5_speed_converter_speed_allowed_values 		PASSED  	[ 85%]
test_session5_speed_converter_time_allowed_values 		PASSED   	[ 87%]
test_session5_speed_converter_dist_allowed_values 		PASSED   	[ 89%]
test_session5_speed_converter_unwanted_args 					PASSED 		[ 91%]
test_session5_speed_converter_output_km_to 						PASSED  	[ 93%]
test_session5_speed_converter_output_m_to 						PASSED   	[ 95%]
test_session5_speed_converter_output_ft_to 						PASSED  	[ 97%]
test_session5_speed_converter_output_yrd_to 					PASSED 		[100%]

============================= 48 passed in 0.17 seconds  ==========================================

```

