#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:52:10 2019

@author: jclayton
"""
# variables


def defactorsum(numbero=0, addo=0, divo=0, counto=0):
    numberi = numbero
    addi = addo
    divi = divo
    counti = counto
    for index in range(counti):
        while numberi % divi != 0:
            numberi = numberi + addi
        numberi = numberi // divi



def basesubtractor(divisoro=0, bitso=0):
    divisori = divisoro
    bitsi = bitso
    for index in range(bitsi):
        if index == 0:
            basesubtractori = (divisori + 1) >> 1
        else:
            if basesubtractori % 2 == 0:
                basesubtractori = basesubtractori >> 1
            else:
                basesubtractori = (basesubtractori + divisori) >> 1
    return basesubtractori


def divide(numbero=0, divisoro=0, bitso=0):
    if divisoro <= 0 or bitso <= 0 or numbero <= 0:
        return -1
    divisori = divisoro
    bitsi = bitso
    raisepoweri = 0
    while divisori % 2 == 0:
        raisepoweri += 1
        divisori = divisori >> 1
    numberi = numbero
    basesubtractori = basesubtractor(divisoro=divisori, bitso=bitsi)
    majorremainderi = 0
    minorremainderi = 0
    resulti = 0
    remaindi = 0
    stepsi = 0
    truncatei = numberi % (2 ** bitsi)
    truncatedi = numberi >> (bitsi)
    if (truncatei % divisori) == 0:
        subtractori = 0
    else:
        subtractori = divisori - ((basesubtractori * truncatei) % divisori)
        if subtractori == divisori:
            subtractori = 0
#    resulti = resulti + ((truncatei * divisori) % (2 ** bitsi)) * (2 ** (bitsi * stepsi))
    resulti = resulti + (((truncatei + (subtractori * (2 ** bitsi))) // divisori) * (2 ** (bitsi * stepsi)))
    remaindi = remaindi + ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
    remi = ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
    print('truncate: '+str(truncatei)+' rem: '+str(remi))
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    while truncatedi > 0:
        stepsi += 1
        numberi = truncatedi - subtractori
        truncatei = numberi % (2 ** bitsi)
        truncatedi = numberi >> (bitsi)
        if (truncatei % divisori) == 0:
            subtractori = 0
        else:
            subtractori = divisori - ((basesubtractori * truncatei) % divisori)
            if subtractori == divisori:
                subtractori = 0
        resulti = resulti + (((truncatei + (subtractori * (2 ** bitsi))) // divisori) * (2 ** (bitsi * stepsi)))
        remaindi = remaindi + ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
        remi = ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
        print('truncate: '+str(truncatei)+' rem: '+str(remi))
        if truncatedi < subtractori:
            majorremainderi = numberi
            truncatedi = 0
    if majorremainderi == 0:
        if raisepoweri > 0:
            minorremainderi = minorremainderi + ((resulti % (2 ** raisepoweri)) * divisori)
            resulti=(resulti >> raisepoweri) 
        print('quotient= '+str(bin(numbero)))
        print('divisor= '+str(bin(divisoro)))
        print('dividend= '+str(bin(resulti)))
        print('remainder= 0')
        print('majorremainder= 0')
        print('bits= '+str(bin(bitso)))
        print('quotient= '+str(numbero))
        print('divisor= '+str(divisoro))
        print('dividend= '+str(resulti))
        print('remainder= '+str(minorremainderi))
        print('majorremainder= 0')
        print('bits= '+str(bitso))
        print('remaindi= '+str(remaindi))
        print('remaindi= '+str(remaindi%divisori))
        return 0
    minorremainderi= (majorremainderi * pow(2, (bitsi*stepsi), divisori)) % divisori
    numberu = numbero - minorremainderi
    numberi = numberu
    majorremainderisave = majorremainderi
    majorremainderi = 0
    resulti = 0
    remaindi=0
    stepsi = 0
    print('\n')
    truncatei = numberi % (2 ** bitsi)
    truncatedi = numberi >> (bitsi)
    if (truncatei % divisori) == 0:
        subtractori = 0
    else:
        subtractori = divisori- ((basesubtractori * truncatei) % divisori)
        if subtractori == divisori:
            subtractori = 0
    resulti = resulti + (((truncatei + (subtractori * (2 ** bitsi))) // divisori) * (2 ** (bitsi * stepsi)))
    remaindi = remaindi + ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
    remi = ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
    print('truncate: '+str(truncatei)+' rem: '+str(remi))
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    while truncatedi > 0:
        stepsi += 1
        numberi = truncatedi - subtractori
        truncatei = numberi % (2 ** bitsi)
        truncatedi = numberi >> (bitsi)
        if (truncatei % divisori) == 0:
            subtractori = 0
        else:
            subtractori = divisori - ((basesubtractori * truncatei) % divisori)
            if subtractori == divisori:
                subtractori = 0
        resulti = resulti + (((truncatei + (subtractori * (2 ** bitsi))) // divisori) * (2 ** (bitsi * stepsi)))
        remaindi = remaindi + ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
        remi = ((truncatei + (subtractori * (2 ** bitsi))) // divisori)
        print('truncate: '+str(truncatei)+' rem: '+str(remi))
        if truncatedi < subtractori:
            majorremainderi = numberi
            truncatedi = 0
    if majorremainderi != 0:
        print('Something bad happened')
        return -1
    if raisepoweri > 0:
        minorremainderi = minorremainderi + ((resulti % (2 ** raisepoweri)) * divisori)
        resulti=(resulti >> raisepoweri) 
    print('quotient= '+str(bin(numbero)))
    print('divisor= '+str(bin(divisoro)))
    print('dividend= '+str(bin(resulti)))
    print('remainder= '+str(bin(minorremainderi)))
    print('majorremainder= '+str(bin(majorremainderisave)))
    print('bits= '+str(bin(bitso)))
    print('quotient= '+str(numbero))
    print('divisor= '+str(divisoro))
    print('dividend= '+str(resulti))
    print('remainder= '+str(minorremainderi))
    print('majorremainder= '+str(majorremainderisave))
    print('bits= '+str(bitso))
    print('remaindi= '+str(remaindi))
    print('remaindi= '+str(remaindi%divisori))
    return 0




