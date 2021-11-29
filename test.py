#!/usr/bin/env python3
"""
Author : madelinemelichar <madelinemelichar@localhost>
Date   : 2021-11-18
Purpose: test punnett.py
"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = './punnett.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_no_args():
    """ Dies on no args """

    rv, out = getstatusoutput(prg)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_parent():
    """Test for (1) parent genotype pair"""

    parents = "AAxAa"
    rv, out = getstatusoutput(f'{prg} {parents}')
    assert rv == 0
    assert re.search('Child Genotype Probabilities: AA = 0.5, Aa = 0.5, aa = 0', out)


# --------------------------------------------------
def test_parent_punnett():
    """Test for (1) parent genotype pair and punnett square"""

    parents = "AAxAa"
    rv, out = getstatusoutput(f'{prg} {parents} -p')
    assert rv == 0
    assert re.search('Child Genotype Probabilities: AA = 0.5, Aa = 0.5, aa = 0 '+
    '''
    +---+----+----+
    |   | A  | A  |
    +---+----+----+
    | A | AA | AA |
    +---+----+----+
    | a | Aa | Aa |
    +---+----+----+''', out)


    # --------------------------------------------------
def test_parents():
    """Test for (2) parent genotype pair"""

    parents = "AAxAa aaxaa"
    expected = '\n'.join([
        'Child Genotype Probabilities: AA = 0.5, Aa = 0.5, aa = 0',
        'Child Genotype Probabilities: AA = 0, Aa = 0, aa = 1.0'
    ])
    rv, out = getstatusoutput(f'{prg} {parents}')
    assert rv == 0
    assert re.search(expected, out)


# --------------------------------------------------
def test_parents_punnetts():
    """Test for (s) parent genotype pair and punnett square"""

    parents = "AAxAa aaxaa"
    expected = '\n'.join([
    'Child Genotype Probabilities: AA = 0.5, Aa = 0.5, aa = 0',
    '''
    +---+----+----+
    |   | A  | A  |
    +---+----+----+
    | A | AA | AA |
    +---+----+----+
    | a | Aa | Aa |
    +---+----+----+''',
    'Child Genotype Probabilities: AA = 0, Aa = 0, aa = 1.0',
    '''
    +---+----+----+
    |   | a  | a  |
    +---+----+----+
    | a | aa | aa |
    +---+----+----+
    | a | aa | aa |
    +---+----+----+'''
    ])
    rv, out = getstatusoutput(f'{prg} {parents} -p')
    assert rv == 0
    assert re.search(expected, out)