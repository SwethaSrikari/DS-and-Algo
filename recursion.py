########################### 	SOME EXAMPLES OF RECURSION 		###########################

# Factorial
# Returns factorial of a number
def factorial(number):
	if number == 1:
		return 1
	else:
		return number * factorial(number - 1)

### CHECK ###
# Should print 120
print(factorial(5))

# Fibonacci sequence
# Returns a number at the given position from the fibonnaci sequence
def fibonacci(position):
	if position == 0 or position == 1:
		return position
	else:
		return fibonacci(position - 1) + fibonacci(position - 2)

### CHECK ###
# Should print 34
print(fibonacci(9))