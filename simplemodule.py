#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a simple module example. It has a few functions and some data.

You can import this module if you are in the same directory by doing:
    
    import simplemodule

The functions and data variables declared in this file can then be used by
typing: 
    
    simplemodule.FUNCTIONNAME()
    simplemodule.VARIABLENAME
    
where FUNCTIONNAME and VARIABLENAME are replaced by the respective function
and variable names that you are interested in using.

If you want to know what functions or variables are available, look in the
respective FUNCTIONS and DATA sections by caling help(simplemodule)
"""

simplestring = "This is a string. It can be used in your module. Just import it"

def printhello():
    '''
    prints the string "hello
    '''
    print("Hello")

def returnhello():
    '''
    returns the string "hello"
    '''
    return "Hello"

def printsimplestring():
    '''
    prints the simplestring variable
    '''
    print(simplestring)     
    
def returnsimplestring():
    '''
    returns the simplestring variable
    '''
    return simplestring 

def returnsentences():
    '''
    returns a list of sentences split() from the simplestring variable
    each sentence in the list of sentences is a string.
    '''
    # split simple string on the period/full stop
    sentences = simplestring.split('. ')
    return sentences
    
def generatesentences():
    '''
    returns a generator. the generator yields a sentence.
    the sentence was split() from the simplestring variable
    '''
    # split simple string on the period/full stop
    sentences = simplestring.split('. ')
    for sentence in sentences:
        yield sentence

