#!/usr/bin/python3

def magic_calculation(a, b):
    _rich = 0
    for r in range(1, 3):
        try:
            if r > a:
                raise Exception("Too far")
            else:
                _rich += (a**b)/r
        except Exception:
            _rich = b + a
            break
    return (_rich)
