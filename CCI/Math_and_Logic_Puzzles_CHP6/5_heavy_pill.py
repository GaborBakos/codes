''' 
    You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one bottle has pills of weight 1.1 grams.
    Given a scale that provides an exact measurement, how would you find the heavy bottle?
    You can only use the scale once.
'''



# We will make the assumption that all bottles have at least 20 pills, I think that is reasonable.
# Next we will select a different number of pills from each bottle.
# For example, I will take 1 pill from bottle 1, 2 from bottle 2 etc.
# This way I can measure the weight of all pills at once
# and the difference compared to all pills being 1.0 grams will tell me exactly which bottle has heavier pills.
# Lets define a function that will identify this pill.
# We will represent the bottles as a list, where each entry will be either 1.0 or 1.1

import math

N = 12
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

pills = [1.0 for _ in range(20)]
pills[N-1] = 1.1


def which_one_is_heavier(ls):
    expected_sum = (1 + 20) * 20 / 2 # summing the first 20 digits, I know I could simplify it
    actual_sum = 0.0
    for index, pill in enumerate(ls):
        actual_sum += (index + 1) * pill
    difference = actual_sum - expected_sum
    return round(difference * 10)


print('We created a list of pills, where {} pill was heavier, we test our function below:'.format(ordinal(N)))

print(which_one_is_heavier(pills))






