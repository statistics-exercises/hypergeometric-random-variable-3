# Generating hypergeometric random variables

The code you wrote for the last computer programming exercise, which did selection with replacement, was essentially the same as the code that you wrote to generate binomial random variables.  In the same spirit, the code that you will write to do selection without replacement will generate the hypergeometric random variables that you have just learned about in the video.   

__To complete this exercise I would thus like you to complete the function called `hypergeometric_random_variable`__.  This function takes three arguments in input `M`, the number of balls you will draw from the urn, `R`, the number of green balls in the urn and  `N` the total number of balls in the urn.  It should return the total number of green balls that were drawn when the sampling is done __with replacement.__

Notice that, unlike the code you wrote for sampling with replacement, you are going to have keep track of the total number of balls that are left in the urn as well as the numbers of green and red balls that are left in the urn.
