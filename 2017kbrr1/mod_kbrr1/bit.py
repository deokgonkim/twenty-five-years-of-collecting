#! -*- coding=utf-8 -*-

CONST_8BIT = [ 0x80, 0x40, 0x20, 0x10, 0x8, 0x4, 0x2 , 0x1 ]

if 'DEBUG' in globals():
    for i, n in enumerate(CONST_8BIT):
        print("%d %d" % (i, n))

def to_binary(number):
    '''This function returns binary string for the number
    '''
    assert number < 256, "Number is out of range 255"
    global CONST_8BIT
    str = ''
    for b in CONST_8BIT:
        str += '0' if b & number == 0 else '1'
    return str

def to_bitmap(number, sym_on = '1', sym_off = '0'):
    '''This function returns binary string for the number
    Substitude 1 with sym_on, 0 with sym_off
    '''
    assert number < 256, "Number is out of range 255"
    global CONST_8BIT
    str = ''
    for b in CONST_8BIT:
        str += sym_off if b & number == 0 else sym_on
    return str

