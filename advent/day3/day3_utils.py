import numpy as np
import time

from advent import io_utils


def claim_to_dict(claim):
    claim = claim.replace('@', '')
    claim = claim.replace(':', '')
    spl = claim.split(' ')
    _id = spl[0][1:]
    cords = spl[2].split(',')
    cords = [int(cord) for cord in cords]
    sizes = spl[3].split('x')
    sizes = [int(size) for size in sizes]
    return {'id': _id, 'cords': tuple(cords), 'sizes': tuple(sizes)}


claims = io_utils.load_txt('/home/hannes/repos/advent/advent/day3/input.txt')
claims = [claim_to_dict(claim) for claim in claims]


def init_fabric(size):
    return np.zeros((size, size))


def add_claim_to_fabric(claim, fabric):
    claim_shape = (claim['sizes'][1], claim['sizes'][0])
    fabric[claim['cords'][1]:claim_shape[0]+claim['cords'][1],
           claim['cords'][0]:claim_shape[1]+claim['cords'][0]] += 1
    return fabric


def claim_to_matrix(claim):
    return np.ones((claim['sizes'][1], claim['sizes'][0]))


def add_claims_to_fabric(claims, fabric):
    for claim in claims:
        fabric = add_claim_to_fabric(claim, fabric)
    return fabric


def is_claim_free(claim, fabric):
    claim_shape = (claim['sizes'][1], claim['sizes'][0])
    bool_fab = fabric[claim['cords'][1]:claim_shape[0]+claim['cords'][1],
                      claim['cords'][0]:claim_shape[1]+claim['cords'][0]] == 1
    return np.all(bool_fab)


def calc_part1(fabric):
    un, counts = np.unique(fabric, return_counts=True)
    return sum(counts[2:])


@io_utils.timeit
def calc_part2(claims):
    fabric = init_fabric(1000)
    fabric = add_claims_to_fabric(claims, fabric)
    for claim in claims:
        if is_claim_free(claim, fabric):
            return claim
