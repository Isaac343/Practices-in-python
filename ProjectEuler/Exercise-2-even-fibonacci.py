# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 
# 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.


class Fibonacci():

    def __init__(self):
        self.Fib_one = 1
        self.Fib_two = 1
        self.result = 0
        while self.Fib_one < 4000000:
        	self.Fib_three = self.Fib_one + self.Fib_two
        	# print(self.Fib_three)
        	self.Fib_two = self.Fib_one
        	self.Fib_one = self.Fib_three
        	if (self.Fib_three % 2) == 0:
        		self.result = self.result + self.Fib_three
        	else: 
        		self.result = self. result + 0
        print(self.result)


Aa = Fibonacci()
