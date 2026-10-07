import random

def birthday_probability(people):
    if people > 365:
        return 1
    elif people == 1:
        return 0
    else:
        buffer = 1
        pip = 365
        for i in range(people):
            buffer *= (pip)/365
            pip -= 1
        res = 1 - buffer
        return(res)

def simulate_birthday(people, trials):
    cnt = 0
    for i in range(trials):
        mass = []
        for i in range(people):
            mass.append(random.randint(1,365))
        if len(set(mass)) < len(mass):
            cnt +=1
    res = cnt/trials
    return(res)

if __name__ == "__main__":
    people = int(input())
    trials = int(input())
    print (birthday_probability(people))
    print (simulate_birthday(people, trials))