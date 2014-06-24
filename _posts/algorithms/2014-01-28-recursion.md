---
layout: post
markdown: redcarpet
category: algorithms
tagline: 
tags: [recursion]
---
{% include JB/setup %}

A recursive algorithm has these fundamental properties:  

  1. Must have a **base case**. Typically a problem that is small enough to solve directly.  
  2. Must change state moving towards the base case. Usually, data getting smaller.  
  3. An 'escape clause' check(s), returning the base case(s).

For example, consider the sum of a list of numbers.

Given: `[1, 3, 5, 7, 9]` 

As a parenthesized expression, would be:

`((((1+3)+5)+7)+9) , or  (1+(3+(5+(7+9))))`

Notice the innermost set of paren, `(7+9)` can be solved without a loop or any special constructs. That's the **BASE CASE**.

In a functional form, it's:
    
`sum_nums(nums) = first(nums) + sum_nums(rest(nums))`


#### Factorial 

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

#### Fibonacci

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

#### Compute an Exponent

    def exp(x, n):
        if n == 0:
            return 1
        else:
            return x * exp(x, n-1)

#### Flatten a nested list

    def flatten_list(a, result=None):
        if result is None:
            result = []

        for x in a:
            if isinstance(x, list):
                flatten_list(x, result)
            else:
                result.append(x)

        return result