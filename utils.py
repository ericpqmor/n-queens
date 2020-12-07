import itertools
import random

def is_pacific(pair, state):
    i,j = pair

    if state[i] == state[j]:
        return False

    difcol = abs(i-j)
    difrow = abs(state[i] - state[j])

    return difcol != difrow

def fitness(state):
    index_list = []

    for c in range(len(state)):
        index_list.append(c)

    pairs = list(itertools.combinations(index_list,2))

    ans = 0
    for pair in pairs:
        if is_pacific(pair, state):
            ans = ans + 1

    return ans

def random_position(num):
    l = [c+1 for c in range(num)]
    position = []
    for j in range(num):
        indexChosen = random.randint(0,len(l)-1)
        position.append(l[indexChosen])
        del l[indexChosen]
    return position

def random_swap(num):
    swap_num = random.randint(1,num//2)
    swaps = []

    for _ in range(swap_num):
        i,j = random.randint(0,num-1), random.randint(0,num-1)
        swaps.append((i,j))

    return swaps

def random_particle(num):
    particle = []

    for i in range(num):
        random_pos = random.randint(1,num)
        particle.append(random_pos)

    return particle

def random_genome(num):
    return random_particle(num)

def random_velocity(num):
    velocity = []
    velocity_limit = 7

    for i in range(num):
        random_velocity = random.randint(-velocity_limit,velocity_limit)
        velocity.append(random_velocity)

    return velocity

def bound_velocity(velocity):
    if velocity < -7:
        velocity = -7

    if velocity > 7:
        velocity = 7

    return velocity

def bound_position(position):
    if position < 1:
        position = 1

    if position > 8:
        position = 8

    return position
