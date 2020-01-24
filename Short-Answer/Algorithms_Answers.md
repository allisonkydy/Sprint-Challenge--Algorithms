#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime: O(n)

    Although the loop is running until a hits n^3, a is increasing by n^2 each time. n^3 / n^2 is equal to n^1, so the loops runs n times.


b) Runtime: O(n*log(n))

    The for loop runs n times and the inner while loop runs approximately log(n) times. This is because the variable j increments exponentially until it reaches n for each value between 0 and n. The sum is counting the number of times j is being doubled, which is essentially the function of a logarithm.

c) Runtime: O(n)

    The function will be recursively called n+1 times (the length of n plus the zero base case) and the operation it performs is fixed. Ignoring the (+1) constant, this give a runtime of n.

## Exercise II


