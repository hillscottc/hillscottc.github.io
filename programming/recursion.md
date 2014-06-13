---
layout: default
title: Recursion
---

Like the robots of Asimov, all recursive algorithms must obey three important laws:  

    1. Must have a base case. Typically a problem that is small enough to solve directly.  
    2. Must change its state and move toward the base case. Usually, data getting smaller.  
    3. A recursive algorithm must call itself, recursively.  

### Sum of a List of Numbers
We will begin our investigation with a simple problem that you already know how to solve without using recursion. Suppose that you want to calculate the sum of a list of numbers such as: [1,3,5,7,9]. An iterative function that computes the sum is shown. The function uses an accumulator variable (theSum) to compute a running total.

We could rewrite the list as a fully parenthesized expression, like this:

    ((((1+3)+5)+7)+9) , or  (1+(3+(5+(7+9))))

See the innermost set of paren, `(7+9)` can be solved without a loop or any special constructs. 

To state it in a functional form:
    
    sum_nums(nums) = first(nums) + sum_nums(rest(nums))

There are two key ideas in this listing to look at.
- First, on line 2 is escape clause check. The sum of a list of length 1 is trivial.
- Then, it's a series of simplifications. Each recursive call solves a smaller problem, til it can't get any smaller.

    def sum_nums(nums):
        """
        >>> sum_nums([2, 20, 20])
        42
        """    
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + sum_nums(nums[1:])


### Factorial 

4! = 4 * 3 * 2 * 1

Recursive:

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

Iterative:

    def iterative_factorial(n):
        result = 1
        for i in range(2,n+1):
            result *= i
        return result

### Fibonacci

0,1,1,2,3,5,8,13,21,34,55,89, ...

The Fibonacci numbers are defined by:

    Fn = Fn-1 + Fn-2
    with F0 = 0 and F1 = 1

Recursive solution:

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

Iterative solution:

    def fibi(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

The iterative version fibi() is a lot faster than the recursive version fib().

### Compute an Exponent

    def exp(x, n):
        if n == 0:
            return 1
        else:
            return x * exp(x, n-1)

### Flatten a nested list

    def flatten_list(a, result=None):
        if result is None:
            result = []

        for x in a:
            if isinstance(x, list):
                flatten_list(x, result)
            else:
                result.append(x)

        return result