import numpy.random
import math


def get_middles_first_part(s, n, k, lambd):
    if n > k:
        print("Here must be only n <= k")
        return None
    if lambd < 0:
        print('Error, your max value is less then 0 while minimum is zero.')
        return None
    answers = []
    for number in range(s):
        gates = generate_exponential(k, lambd)
        gates.sort()
        answers.append(gates)
    middle_answers = []
    for i in range(n):
        ans = 0.0
        for j in range(s):
            ans += answers[j][i]
        ans /= n
        middle_answers.append(ans)
    return middle_answers


def get_middles_second_part(s, n, k, lambd):
    if lambd < 0:
        print('Error, your max value is less then 0 while minimum is zero.')
        return None
    answers = []
    for number in range(s):
        gates = generate_exponential(k, lambd)
        print(gates)
        actual_gates_time = []
        for i in range(len(gates)):
            actual_gates_time.append(0)
        persons = []
        for i in range(n):
            persons.append(-1)
        for i in range(n):
           [persons, actual_gates_time] = place_person(persons, actual_gates_time, i, gates)
        answers.append(persons)
    middle_answers = []
    for i in range(n):
        ans = 0.0
        for j in range(s):
            ans += answers[j][i]
        ans /= n
        middle_answers.append(ans)
    return middle_answers


def get_min(actual_gates_time, gates):
    index = 0
    mn = +math.inf
    for i in range(len(actual_gates_time)):
        if mn > actual_gates_time[i]:
            index = i
            mn = actual_gates_time[i]
    for i in range(len(actual_gates_time)):
        actual_gates_time[i] -= mn
        if i == index:
            actual_gates_time[i] = gates[i]
    return [mn, actual_gates_time]


def place_person(persons, actual_gates_time, i, gates):
    [mn, actual_gates_time] = get_min(actual_gates_time, gates)
    if i == 0:
        persons[i] = mn
    else:
        persons[i] = persons[i - 1] + mn
    return [persons, actual_gates_time]


def generate_exponential(n, lambd):
    return numpy.random.exponential(lambd, n)