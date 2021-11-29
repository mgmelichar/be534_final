#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-18
Purpose: BE 534 Fall 2021, final project
"""

import argparse
import numpy as np
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probability of expected offspring genotype with punnett square',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('parent',
                        type=str,
                        nargs='+',
                        help='parent(s) genotypes (EX: AAxAa)')

    parser.add_argument('-p',
                        '--punnett',
                        help='Display punnett square',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------


def get_combos(parents):
    """Genotype Combinations"""

    combinations = []
    probability = {}

    combinations.append(parents[0][0]+parents[1][0])
    combinations.append(parents[0][0]+parents[1][1])
    combinations.append(parents[0][1]+parents[1][0])
    combinations.append(parents[0][1]+parents[1][1])

    combinations = ["Aa" if geno == "aA" else geno for geno in combinations]

    for geno in np.unique(combinations):
        probability[geno] = combinations.count(geno)/len(combinations)

    return probability, combinations


# --------------------------------------------------
def main():
    """Run main"""

    args = get_args()
    for couple in args.parent:
        parents = couple.split("x")
        p_child, combos = get_combos(parents)
        print("Child Genotype Probabilities: AA = {}, Aa = {}, aa = {}".format(
            p_child.get('AA', 0), p_child.get('Aa', 0), p_child.get('aa', 0)))

        if args.punnett:
            punnett_square = tabulate([["", parents[0][0], parents[0][1]], [
                                      parents[1][0], combos[0], combos[2]], [parents[1][1], combos[1], combos[3]]], tablefmt='grid')
            print(punnett_square)


# --------------------------------------------------
if __name__ == '__main__':
    main()
