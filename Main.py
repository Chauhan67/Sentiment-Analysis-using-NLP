#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:15:47 2020

@author: adarshperi
"""

import sentiment_mod as s

print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print("pos")
print()

print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
print("neg")
print()

print(s.sentiment("Not so bad"))
print("neg")
print()

print(s.sentiment("It was not that great"))
print("neg")
print()

print(s.sentiment("emerges as something rare , an issue movie that's so honest and keenly observed that it doesn't feel like one"))
print("pos")
print()

print(s.sentiment("it's so laddish and juvenile , only teenage boys could possibly find it funny"))
print("neg")
print()

print(s.sentiment("My experience has been okay I guess"))
print("neg")
print()

print(s.sentiment("The movie was fantastic"))
print("pos")
print()

print(s.sentiment("Your support team is useless"))
print("neg")
print()

print(s.sentiment("It was not a good movie "))
print("neg")
print()