# slowtype.py
# a library for printing a message to the console in a human way
# inspired by football 17776, a work by Jon Bois
# hesitate after commas half the time
# hestitate after periods for a short amount of time, 0.3 to 0.5 seconds.
# Written by starmaid
# Created 09/30/2019
# Edited 03/14/2020
# edited 09/30/2020 (wow a year exactly!)
# edited 12/20/2020
# (uploaded to github)

"""
Issues: sometimes newlines mess stuff up

"""

import time
import random
import sys
from colored import stylize, fg, bg, attr

class Slowtype():
    def __init__(self, definitions, speed=1):
        self.speed = speed
        self.tab = '    '
        # read definitons array and create dict
        with open('./chars.txt','r') as defsf:
            # make a matrix of it
            defarray = defsf.readlines()
            #turn the matrix into a dict
            self.defs = {}
            for l in defarray:
                l = l.strip('\n').split(',')
                self.defs[l[0]] = {'fg':l[1], 'bg':l[2], 'ind':l[3]}


    def hesitate(self, dur):
        time.sleep(dur * self.speed * 0.02)

    def iprint(self, thing, role=None):
        # instant print. normal printing waits until newlines
        # to flush the buffer
        if role is not None:
            thing = stylize(thing, fg(self.defs[role]['fg'])+bg(self.defs[role]['bg']))
        
        print(thing, sep='', end='', flush=True)
        sys.stdout.flush()

    def printchar(self, char, role=None):
        self.iprint(char,role=role)
        if char == '.':
            self.hesitate(random.randint(10,13))
        elif char == ',':
            self.hesitate(random.randint(8,10))
        elif char == '?':
            self.hesitate(random.randint(10,12))
        elif char == '!':
            self.hesitate(random.randint(8,10))
        elif char == ' ':
            self.hesitate(0)
        else:
            self.hesitate(random.randint(1,5))


    def maketypo(self, char):
        if char == ' ':
            typo = ''
        elif char == '.':
            typo = ','
        elif char == ',':
            typo = '.'
        elif 65 <= ord(char) <= 90:
            typo = chr(random.randint(65,91))
        elif 97 <= ord(char) <= 122:
            typo = chr(random.randint(97,123))
        else:
            typo = char
        return typo

    def slow_print(self, phrase, role=None, typos=True, typoRate=30):
        edited = phrase
        typo = False
        pos = 0

        if (len(phrase) == 0):
            #self.iprint('\n')
            self.hesitate(6)
        
        # print the indentation for the line
        if role is not None:
            self.iprint(self.tab * int(self.defs[role]['ind']))

        # print the content
        while pos < len(edited):
            if (random.randint(0,typoRate) == 0) and not typo and typos and pos < len(edited)-2 and (edited[pos+1] != '\n') and (edited[pos+2] != '\n'):
                # make a typo, edit the string, store its location
                edited = f'{edited[0:pos]}{self.maketypo(edited[pos])}{edited[pos+1:len(edited)]}'
                typo = True
            
            if typo and typos:
                # how to behave when a typo is active
                
                # first, keep printing letters until it notices or newline
                errorpos = pos
                while (random.randint(0,3) != 0) and (edited[errorpos+1] != '\n'):
                    self.printchar(edited[errorpos],role=role)
                    errorpos += 1
                
                i = 0
                diff = errorpos - pos
                
                while i <= diff:
                    # backspace
                    line = edited[0:errorpos-i].split('\n')[-1]
                    self.iprint(f'\r{line}'.ljust(len(line) + i + 1),role=role)
                    self.hesitate(3)
                    i += 1
                
                edited = phrase
                while i >= 0:
                    # catch up to where j is
                    self.iprint(f"\r{edited[0:errorpos-i].split(chr(10))[-1]}",role=role)
                    self.hesitate(3)
                    i -= 1
                typo = False
                pos = errorpos
            

            self.printchar(edited[pos],role=role)
            pos += 1
        
        # reset color
        self.iprint(attr('reset') + '\n')



if __name__ == '__main__':
    S = Slowtype('chars.txt',speed=1)

    #S.slow_print(msg, typos=True, typoRate=50)

    with open('./script.txt','r',encoding='utf-8', errors='ignore') as script:
        fscript = script.readlines()
        prev = None
        for line in fscript:
            if (line == '\n'):
                S.slow_print('')
            else:
                # REMOVE NEWLINE HERE
                line = line.strip('\n')
                role = line.split(': ')[0]

                if prev != role:
                    S.hesitate(20)
                    prev = role

                S.slow_print(line.split(': ')[1], role=role, typos=False, typoRate=50)