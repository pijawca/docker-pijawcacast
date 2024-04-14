# -*- coding: utf-8 -*-


def rank(experience):
    if experience > 50000:
        return '10'
    elif experience > 20000:
        return '9'
    elif experience > 15000:
        return '8'
    elif experience > 10000:
        return '7'
    elif experience > 7500:
        return '6'
    elif experience > 5000:
        return '5'
    elif experience > 2500:
        return '4'
    elif experience > 1250:
        return '3'
    elif experience > 750:
        return '2'
    elif experience > 250:
        return '1'
    return '0'