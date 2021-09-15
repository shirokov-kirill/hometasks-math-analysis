import numpy.random
import math
import random


def SKO_a(n, theta, s, k_max):
    if theta < 0:
        print('Error, your max value is less then 0 while minimum is zero.')
        return None
    k = 1
    while(k < k_max):
        result = 0.0
        for number in range(s):
            input = generate_normal(n, theta)
            #print('Сгенерировано: ')
            #print(input)
            result_i = get_estimation(input, k)
            result_i *= (k + 1)
            result_i = pow(result_i, (1 / k))
            #print('Оценка theta*:')
            #print(result_i)
            result += (result_i - theta) * (result_i - theta)
        print('k = ' + str(k) + ', СКО_a = ' + str(result / s))
        k += 1
    return True


def SKO_b(n, lambd, s, k_max):
    if lambd < 0:
        print('Error, your max value is less then 0 while minimum is zero.')
        return None
    k = 1
    while(k < k_max):
        result = 0.0
        for number in range(s):
            input = generate_exponential(n, lambd)
            result_i = get_estimation(input, k)
            result_i /= math.factorial(k)
            result_i = pow(result_i, (1/k))
            result += (result_i - lambd) * (result_i - lambd)
        print('k = ' + str(k) + ', СКО_b = ' + str(result / s))
        k += 1
    return True


def generate_normal(n, theta):
    return numpy.random.uniform(0, theta, n)


def generate_exponential(n, lambd):
    return numpy.random.exponential(lambd, n)

def get_estimation(input, k):
    count = len(input)
    result = 0
    for i in range(count):
        result += pow(input[i], k)
    result /= count
    return result