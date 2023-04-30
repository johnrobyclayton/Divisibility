#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:52:10 2019

@author: jclayton
"""
# variables
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def basesubtractor(divisoro=0, bitso=0):
    divisori = divisoro
    bitsi = bitso
    basesubtractori=0
    for index in range(bitsi):
        if index == 0:
            basesubtractori = (divisori + 1) >> 1
        else:
            if not(basesubtractori & 1):
                basesubtractori = basesubtractori >> 1
            else:
                basesubtractori = (basesubtractori + divisori) >> 1
    return basesubtractori


def intlog(numbero, base):
    logi=0
    numberi=numbero
    while numberi >= base:
        numberi = numberi // base
        logi +=1
    return logi

def doublemods(numbero, starto, limito):
    tr = starto
    found = False
    number=list(range(10000))
    for x in range(10000):
        number[x]=(numbero % (tr + x))
        for y in range(x):
            if number[x] == number[y]:
                print('1 '+str(tr+x) + ' '+str(number[x])+' '+str(tr+y)+' '+str(number[y]))
                found = True
    while not found and tr < limito:
        tr += 1
        for x in range(9999):
            number[x] = number[x + 1]
        number[9999] = numbero % (tr + 9999)
        for x in range(9999):
            if number[x] == number[9999]:
                print('2 '+str(tr+x) + ' '+str(number[x])+' '+str(tr+9999)+' '+str(number[9999]))
                found = True
        #print('3 '+str(tr)+' '+str(tr+x)+' '+str(number[9999]))


def getsmallmods(numbero):
    for x in range(1,40):
        if numbero % x == 1:
            print('number ' + str(x)+' mod '+str(1))
        if numbero % x == 3:
            print('number ' + str(x)+' mod '+str(3))
        if numbero % x == 5:
            print('number ' + str(x)+' mod '+str(5))
        if numbero % x == 7:
            print('number ' + str(x)+' mod '+str(7))
        if numbero % x == 11:
            print('number ' + str(x)+' mod '+str(11))
        if numbero % x == 13:
            print('number ' + str(x)+' mod '+str(13))
        if numbero % x == 17:
            print('number ' + str(x)+' mod '+str(17))
        if numbero % x == 19:
            print('number ' + str(x)+' mod '+str(19))
        if numbero % x == 23:
            print('number ' + str(x)+' mod '+str(23))
        if numbero % x == 29:
            print('number ' + str(x)+' mod '+str(23))
        if numbero % x == 31:
            print('number ' + str(x)+' mod '+str(23))
            


def getcoordinatemods(ao,bo,modo):
    for x in range(ao*bo):
        for y in range(ao*bo):
            if((x*y)%ao==(x*y)%bo and (x*y)%ao==modo):
                print('x '+str(x)+' y '+str(y))

def pqmnxyabD(Do=1,ao=1,bo=1,mo=1,no=1,yo=1):
    xo = ((((Do-(mo*no))/(ao*bo))-(mo*yo))/(no+(ao*bo*yo)))
    print('x '+str(xo))
    po = (mo+ao*bo*xo)
    qo = (no+ao*bo*yo)
    print('diff ')
    print(Do-int(po)*qo)
    print('isdiff '+str((Do-(po*qo))!=0))
    print('d '+str(Do))
    print('p '+str(po))
    print('q '+str(qo))
    print('pq '+str(int(po*qo)))
    

'''
    firstmod = numbero % (tr)
    secondmod=numbero % (tr + 1)
    while tr < limito:
        if firstmod == secondmod:
            print(str(tr))
        tr += 1
        firstmod = secondmod
        secondmod = numbero % (tr + 1)
'''
'''
def issquare(numbero):
    found = False
    log2i = intlog(numbero, 2)
    print('log2i: '+str(log2i))
    lowlogi = 0
    highlogi = 0
    if (log2i & 1):
        lowlogi = log2i - 1
        highlogi = log2i + 1
    else:
        lowlogi = log2i
        highlogi - log2i + 2
    print('lowlogi: '+str(lowlogi))
    print('highlogi: '+str(highlogi))
    highoddi = 2 ** (highlogi) + 1
    print('highoddi: '+str(highoddi))
    if lowlogi == 0:
        lowoddi = 1
    else:
        lowoddi = 2 ** (lowlogi) + 1
    print('lowoddi: '+str(lowoddi))
    thighoddi = highoddi
    print('thighoddi: '+str(thighoddi))
    tlowoddi = lowoddi
    print('tlowoddi: '+str(tlowoddi))
    tmidoddi = (((thighoddi+tlowoddi) >> 2) << 1) + 1
    print('tmidoddi: '+str(tmidoddi))
    diffi = 0
    for x in range(lowoddi, tmidoddi, 2):
        print('x: '+str(x))
        diffi = diffi + x
    print('diffi: '+str(diffi))
    resulti=numbero-diffi
    print('resulti: '+str(resulti))
    while not found:
        if resulti < (1 << lowlogi):
            thighoddi = tmidoddi
        if resulti > (1 << lowlogi):
            tlowoddi = tmidoddi
        if resulti == (1 << lowlogi):
            square = True
            found = True
        if (thighoddi - 2) <= tlowoddi:
            if not found:
                square = False
                found = True
        tmidoddi = tlowoddi + ((thighoddi-tlowoddi) >> 2) << 1
        diffi = 0
        for x in range(lowoddi, tmidoddi, 2):
            diffi = diffi + x
        resulti = numbero - diffi
    return square

'''
def powermodlen(multipliero=2, modo=3):
    logi = intlog(modo, multipliero)
    multiplyi = multipliero ** logi
    if((multipliero * multiplyi)% modo) == 1:
        return logi+1
    
    #print('1logi '+str(logi))
    posi = 1
    #print('2posi ' + str(posi))
    posi = (posi * multipliero * multiplyi) % modo
    
    #print('3posi ' + str(posi))
    counti = logi + 1
    #print('4counti ' + str(counti))
    logu = intlog(posi, multipliero)
    #print('7logu ' + str(logu))
    posu = multipliero ** logu
    #print('8posu ' + str(posu))
    while posi != posu:
        posi = (posi * multiplyi) % modo
        #print('10posi ' + str(posi)+'10post ' + str(post))
        counti += logi
        #print('9counti ' + str(counti))
        logu = intlog(posi, multipliero)
        #print('11logu ' + str(logu))
        posu = multipliero ** logu
        #print('12posu ' + str(posu))
    print('9counti ' + str(counti - logu))
    return counti-logu



def divides(dividendo=0, divisoro=0):
    if (divisoro == 0):
        print(str(divisoro))
        return False
    if (dividendo == 0):
        return True
    bitsi = 1
    divisorp = divisoro
    raisepoweri = 0
    while not (divisorp & 1):
        raisepoweri += 1
        divisorp = (divisorp >> 1)
    divisori = divisorp
    numberp = dividendo
    while (raisepoweri >= 1) and not (numberp & 1):
        raisepoweri -= 1
        numberp = numberp >> 1
    numberi = numberp
    if raisepoweri > 0:
        return False
    basesubtractori = basesubtractor(divisoro=divisori, bitso=bitsi)
    majorremainderi = 0
    truncatedi = numberi >> (bitsi)
    truncatei = numberi - (truncatedi << bitsi)
    testtruncatei = truncatei
    while testtruncatei >= divisori:
        testtruncatei -= divisori
    if testtruncatei == 0:
        subtractori = 0
    else:
        subtractori = basesubtractori * truncatei
        while subtractori >= divisori:
            subtractori -= divisori
        subtractori = divisori - subtractori
        if subtractori == divisori:
            subtractori = 0
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    while truncatedi > 0:
        numberi = truncatedi - subtractori
        truncatedi = numberi >> (bitsi)
        truncatei = numberi - (truncatedi << bitsi)
        testtruncatei = truncatei
        while testtruncatei >= divisori:
            testtruncatei -= divisori
        if testtruncatei == 0:
            subtractori = 0
        else:
            subtractori = basesubtractori * truncatei
            while subtractori >= divisori:
                subtractori -= divisori
            subtractori = divisori - subtractori
            if subtractori == divisori:
                subtractori = 0
        if truncatedi < subtractori:
            majorremainderi = numberi
            truncatedi = 0
    return majorremainderi == 0    


def oddremainder(dividendo=0, divisoro=0):
    if divisoro <= 0:
        return -4
    if dividendo == 0:
        return 0
    bitsi = 1
    divisorp = divisoro
    if not (divisorp & 1):
        return -5
    divisori = divisorp
    numberp = dividendo
    numberi = numberp
    basesubtractori = basesubtractor(divisoro=divisori, bitso=bitsi)
    majorremainderi = 0
    subtractori = 0
    stepsi = 0
    truncatedi = numberi >> (bitsi)
    truncatei = numberi - (truncatedi << bitsi)
    testtruncatei = truncatei
    while testtruncatei >= divisori:
        testtruncatei -= divisori
    if testtruncatei == 0:
        subtractori = 0
    else:
        subtractori = basesubtractori * truncatei
        while subtractori >= divisori:
            subtractori -= divisori
        subtractori = divisori - subtractori
        if subtractori == divisori:
            subtractori = 0
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    while truncatedi > 0:
        stepsi += 1
        numberi = truncatedi - subtractori
        truncatedi = numberi >> (bitsi)
        truncatei = numberi - (truncatedi << bitsi)
        testtruncatei = truncatei
        while testtruncatei >= divisori:
            testtruncatei -= divisori
        if testtruncatei == 0:
            subtractori = 0
        else:
            subtractori = basesubtractori * truncatei
            while subtractori >= divisori:
                subtractori -= divisori
            subtractori = divisori - subtractori
            if subtractori == divisori:
                subtractori = 0
        if truncatedi < subtractori:
            majorremainderi = numberi
            truncatedi = 0
    if majorremainderi == 0:
        return 0
    reducer = majorremainderi
    stepreducer = stepsi
    while reducer >= divisori or stepreducer > 0:
        while reducer >= divisori:
            reducer -= divisori
        if stepreducer >= 1:
            reducer = reducer << 1
            stepreducer -= 1
    return reducer


def divide(numbero=0, divisoro=0, bitso=0):
    if divisoro <= 0 or bitso <= 0:
        return -6
    if numbero == 0:
        divresult = {}
        divresult['dividend'] = numbero
        divresult['divisor'] = divisoro
        divresult['bits'] = bitso
        divresult['basesubtractor'] = 0
        divresult['quotient'] = 0
        divresult['majorremainder'] = 0
        divresult['minorremainder'] = 0
        divresult['steps'] = 0
        return divresult
    bitsi = bitso
    #print('1bits '+str(bitsi))
    raisepoweri = 0
    #print('2raisepoweri '+str(raisepoweri))
    divisorp = divisoro
    #print('3divisorp '+str(divisorp))
    while not (divisorp & 1):
        raisepoweri += 1
        #print('4raisepoweri '+str(raisepoweri))
        divisorp = divisorp >> 1
        #print('5divisorp '+str(divisorp))
    divisori = divisorp
    #print('6divisori '+str(divisori))
    numberp = numbero
    #print('7numberp '+str(bitsi))
    while (raisepoweri >= 1) and not (numberp & 1):
        raisepoweri -= 1
        #print('8raisepoweri '+str(raisepoweri))
        numberp = numberp >> 1
        #print('9numberp '+str(numberp))
    numberi = numberp
    #print('10numberi '+str(numberi))
    #print('1call basesubtractor divisor '+str(divisori)+' bits '+str(bitsi))
    basesubtractori = basesubtractor(divisoro=divisori, bitso=bitsi)
    #print('11basesubtractori '+str(basesubtractori))
    majorremainderi = 0
    minorremainderi = 0
    resulti = 0
    stepsi = 0
    truncatedi = numberi >> (bitsi)
    #print('12truncatedi '+str(truncatedi))
    truncatei = numberi - (truncatedi << bitsi)
    #print('13truncatei '+str(truncatei))
    if divides(truncatei, divisori):
        subtractori = 0
    else:
        #print('2call oddremainder number '+str(basesubtractori * truncatei)+' divisor '+str(divisori))
        subtractori = divisori - oddremainder((basesubtractori * truncatei) , divisori)
        #print('14subtractori '+str(subtractori))
        if subtractori == divisori:
            subtractori = 0
    resulti = resulti + (((truncatei + (subtractori << bitsi)) // divisori) << (bitsi * stepsi))
    #print('15resulti '+str(resulti))
    #print('16truncatedi '+str(truncatedi))
    #print('17subtractori '+str(subtractori))
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    #print('18truncatedi '+str(truncatedi))
    #print('19subtractori '+str(subtractori))
    while truncatedi > 0:
        stepsi += 1
        #print('20stepsi '+str(stepsi))
        numberi = truncatedi - subtractori
        #print('21truncatedi '+str(truncatedi))
        #print('22subtractori '+str(subtractori))
        #print('23numberi '+str(numberi))
        truncatedi = numberi >> (bitsi)
        #print('24truncatedi '+str(truncatedi))
        truncatei = numberi - (truncatedi << bitsi)
        #print('25truncatei '+str(truncatei))
        if divides(truncatei, divisori):
            subtractori = 0
        else:
            #print('3call oddremainder number '+str(basesubtractori * truncatei)+' divisor '+str(divisori))
            subtractori = divisori - oddremainder((basesubtractori * truncatei) , divisori)
            if subtractori == divisori:
                subtractori = 0
        #print('26subtractori '+str(subtractori))
        resulti = resulti + (((truncatei + (subtractori << bitsi)) // divisori) << (bitsi * stepsi))
        if truncatedi < subtractori:
            majorremainderi = numberi
            #print('22majorremainderi '+str(majorremainderi))
            truncatedi = 0
    if majorremainderi == 0:
        if raisepoweri > 0:
            minorremainderi = minorremainderi + ((resulti -((resulti >> raisepoweri) << raisepoweri)) * divisori)
            resulti = (resulti >> raisepoweri)
        divresult = {}
        divresult['dividend'] = numbero
        divresult['divisor'] = divisoro
        divresult['bits'] = bitso
        divresult['basesubtractor'] = basesubtractori
        divresult['quotient'] = resulti
        divresult['majorremainder'] = majorremainderi
        divresult['minorremainder'] = minorremainderi
        divresult['steps'] = stepsi
        return divresult
    #print('4call oddremainder number '+str((majorremainderi * pow(2, (bitsi*stepsi), divisori)))+' divisor '+str(divisori))
    t1=datetime.now()
    zeros=bitsi*stepsi
    while zeros>divisori:
        zoros-=divisori
    #minorremainderi= oddremainder((majorremainderi * pow(2, (bitsi*stepsi), divisori)) , divisori)
    minorremainderi= oddremainder(majorremainderi << zeros , divisori)
    t2=datetime.now()
    print('oddremainder',t2-t1)
    numberu = numberp - minorremainderi
    numberi = numberu
    majorremainderisave = majorremainderi
    majorremainderi = 0
    resulti = 0
    stepsi = 0
    truncatedi = numberi >> (bitsi)
    truncatei = numberi - (truncatedi << bitsi)
    if divides(truncatei, divisori):
        subtractori = 0
    else:
        #print('5call oddremainder number '+str(basesubtractori * truncatei)+' divisor '+str(divisori))
        subtractori = divisori- oddremainder((basesubtractori * truncatei) , divisori)
        if subtractori == divisori:
            subtractori = 0
    resulti = resulti + (((truncatei + (subtractori << bitsi)) // divisori) << (bitsi * stepsi))
    if truncatedi < subtractori:
        majorremainderi = numberi
        truncatedi = 0
    while truncatedi > 0:
        stepsi += 1
        numberi = truncatedi - subtractori
        truncatedi = numberi >> (bitsi)
        truncatei = numberi - (truncatedi << bitsi)
        if divides(truncatei, divisori):
            subtractori = 0
        else:
            #print('6call oddremainder number '+str(basesubtractori * truncatei)+' divisor '+str(divisori))
            subtractori = divisori - oddremainder((basesubtractori * truncatei) , divisori)
            if subtractori == divisori:
                subtractori = 0
        resulti = resulti + (((truncatei + (subtractori << bitsi)) // divisori) << (bitsi * stepsi))
        if truncatedi < subtractori:
            majorremainderi = numberi
            truncatedi = 0
    if majorremainderi != 0:
        print('Something bad happened')
        return -7
    if raisepoweri > 0:
        minorremainderi = minorremainderi + ((resulti -((resulti >> raisepoweri) << raisepoweri)) * divisori)
        resulti=(resulti >> raisepoweri) 
    divresult = {}
    divresult['dividend'] = numbero
    divresult['divisor'] = divisoro
    divresult['bits'] = bitso
    divresult['basesubtractor'] = basesubtractori
    divresult['quotient'] = resulti
    divresult['majorremainder'] = majorremainderisave
    divresult['minorremainder'] = minorremainderi
    divresult['steps'] = stepsi
    return divresult
def main():
    t1=datetime.now()
    print((123456789123456789123456789*123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789+1)//123456789123456789123456789)
    t2=datetime.now()
    print(divide((123456789123456789123456789*123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789+1),123456789123456789123456789,100))
    t3=datetime.now()
    print(t2-t1,' ',t3-t2)
if __name__ == "__main__":
    main()




