#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:41:58 2019

@author: jclayton
"""
while True:
    reply = input('Enter text:')
    if(reply=='stop'): break
    try:
        print(float(reply)**2)
    except:
        print(reply.upper())
print('Bye')
