import math

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stddev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)
