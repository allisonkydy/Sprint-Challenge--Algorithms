#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime: O(n)

    Although the loop is running until a hits n^3, a is increasing by n^2 each time. n^3 / n^2 is equal to n^1, so the loops runs n times.


b) Runtime: O(n*log(n))

    The for loop runs n times and the inner while loop runs approximately log(n) times. This is because the variable j increments exponentially until it reaches n for each value between 0 and n. The sum is counting the number of times j is being doubled, which is essentially the function of a logarithm.

c) Runtime: O(n)

    The function will be recursively called n+1 times (the length of n plus the zero base case) and the operation it performs is fixed. Ignoring the (+1) constant, this gives a runtime of n.

## Exercise II

Algorithm:

The start floor is floor 1.
The end floor is n.
Find the middle floor between the start and end floors. (If total floors is even, the middle skews low)

As long as there is more than one floor (end - start > 0), drop an egg from the middle floor.
    If there are only two floors left (i.e. end - start == 1) 
        and the egg breaks, the current middle floor (or start floor) is floor f.
        Otherwise if the egg doesn't break, the end floor is floor f.
        Stop dropping eggs.
    If the egg breaks, the current floor becomes the new ending floor. 
        Find the middle floor using the new ending floor. Continue dropping eggs.
    If it doesn't break, the floor above the current middle floor becomes the new staring floor
        Find the middle floor using the new starting floor. Continue dropping eggs.

If there is one floor (i.e. end - start == 0), then that floor is floor f.

Runtime complexity: O(log(n))

Functions like binary search. Better runtime than linear search, but has potential to break more eggs (linear search would only need to break one egg).

