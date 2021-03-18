#!/usr/bin/env python

"""Definitions of CBM algorithm properties (variants and optimization criteria).
"""

def enum(**enums):
    """
    Defines ENUM type.

    | Usage:
    | enum(name1=value1, name2=value2)
    """
    return type('Enum', (), enums)


problem_variants = enum(CLASSIC=0, OPEN=1)
problem_criteria = enum(TIME=1, COST=2, TIMECOST=3)